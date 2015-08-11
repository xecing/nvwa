import os
import sys

class HttpResponse:
	def __init__(self, **kwargs):
		self.kwargs = kwargs

	def run(self):
		module = __import__(self.kwargs['module'],globals={}, locals={}, fromlist=[], level=-1)
		# print modules
		# print self.kwargs['module']
		# module = modules[self.kwargs['module']]
		print module
		clazz = getattr(module,self.kwargs['clazz'])
		print dir(clazz)
		instance = clazz()
		result = instance.run()

		del sys.modules[self.kwargs['module']]
		return result