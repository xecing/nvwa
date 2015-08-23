import time
import json

class remote:
	def __init__(self, kwargs):
		self.kwargs = kwargs

	def run(self):
		remote_cfg = {
			"host" : self.kwargs['_httpclient'].address[0],
			"port" : self.kwargs['_httpclient'].address[1],
			"timestamp" : int(time.time())
		}
		return json.dumps(remote_cfg)
