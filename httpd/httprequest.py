from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
 

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
    	
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()
    	
    	self.request = {}
    	self.request['command'] = self.command
    	self.request['path'] = self.path
    	self.request['request_version'] = self.request_version
    	self.request['protocol_version'] = self.protocol_version
    	print self.request

 
    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message
