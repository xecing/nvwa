import os
import sys
import re

from httprequest import HTTPRequest

class HttpResponse:
	def __init__(self, httprequest, **kwargs):
		self.kwargs = kwargs
		self.httprequest = httprequest

	def run(self):
		_path = re.compile(r'/(.*)/(.*)')
		_module = _path.sub(r'\1', self.httprequest.request['path'])
		_class = _path.sub(r'\2', self.httprequest.request['path'])


		module = __import__(_module ,globals={}, locals={}, fromlist=[], level=-1)
		reload(module)

		_class = getattr(module,_class)

		instance = _class(self.kwargs)
		result = instance.run()

		del sys.modules[_module]
		return result
