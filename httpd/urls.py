import re

class Action:
	def __init__(self, url, call):
		self.url = re.compile(url)
		self.call = call

	def match(self, request):
		return self.url.match(request) is not None

class Urls:
	ResponseHandle = None
	verifyUrls = None

	@staticmethod
	def Callable(func):
		if hasattr(Urls.ResponseHandle, func):
			return getattr(Urls.ResponseHandle, func)
		return None


	@staticmethod
	def Ready(handler):
		Urls.ResponseHandle = handler
		Urls.verifyUrls = [
			Action(r'/(.*?)/(.*)' ,Urls.Callable('handlePlugin')),
			Action(r'/(.*\..*)' ,Urls.Callable('handleFile')),
		]


	@staticmethod
	def Transform(request):
		for v in Urls.verifyUrls:
			if v.match(request):
				if v.call is not None:
					return v.call(v)
				

