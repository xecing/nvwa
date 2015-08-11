import os
import sys

import socket
import Queue
import thread

from httpresponse import HttpResponse

class HttpClient:
	def __init__(self):
		self.connect = 0
		self.address = 0

	def make(self, accept):
		self.connect = accept[0]
		self.address = accept[1]



class HttpSrv:
	def __init__(self):
		self.socket  = 0
		self.queue   = 0
		self.maxsize = 0

	def init(self, address, port, maxs):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((address, port))
		self.socket.listen(maxs)
		self.queue = Queue.Queue(maxs)
		self.maxsize = maxs
		sys.path.append('./subroutine')

	def start(self):
		for i in range(0, self.maxsize):
			thread.start_new_thread(self.run, ())


	def run(self):
			httpclient = self.queue.get()

			recv = httpclient.connect.recv(1024)
			print recv
			httpersponse = HttpResponse(module='plugin_time', clazz='Time')
			resp = httpersponse.run()

			httpclient.connect.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n%s' % (len(resp),resp))
			
			httpclient.connect.close()
			self.queue.task_done()

	def accept(self):
		while True:
			httpclient = HttpClient()
			httpclient.make(self.socket.accept())
			print '[connect]: ',  httpclient.address
			self.queue.put(httpclient)



def main():
	_httpsrv = HttpSrv()
	_httpsrv.init('',80,64)
	_httpsrv.start()
	while True:
		_httpsrv.accept()



if __name__ == '__main__':
	main()