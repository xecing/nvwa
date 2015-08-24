import os
import sys
import re

from httprequest import HTTPRequest
from urls import Urls
from urls import Action
from conf import CONF

class HttpResponse:
	def __init__(self, httprequest, **kwargs):
		self.kwargs = kwargs
		self.httprequest = httprequest
		Urls.Ready(self)

	def run(self):
		return Urls.Transform(self.httprequest.request['path'])

	def handlePlugin(self, action):
		_module = action.url.sub(r'\1', self.httprequest.request['path'])
		_class = action.url.sub(r'\2', self.httprequest.request['path'])

		module = __import__(_module ,globals={}, locals={}, fromlist=[], level=-1)
		reload(module)

		_class = getattr(module,_class)

		instance = _class(self.kwargs)
		result = instance.run()

		del sys.modules[_module]
		return result

	def handleFile(self, action):
		request = action.url.sub(r'\1', self.httprequest.request['path'])
		try:
			with open('%s/%s' % (CONF.site, request), 'rb') as fp:
				resp = fp.read()
				return resp
		except:
			print 'handleFile Error Cannot Open [%s]' % request

