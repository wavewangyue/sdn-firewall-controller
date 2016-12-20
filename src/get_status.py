import httplib
import json


class FireWallInit(object):

    def __init__(self,server):
        self.server = server

    def get_status(self):
        path = '/wm/firewall/module/status/json'
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request('GET',path)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        return ret[2]

    def enable_firewall(self):
        path = '/wm/firewall/module/enable/json'
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request('GET', path)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        return ret[2]

    def disable_firewall(self):
        path = '/wm/firewall/module/disable/json'
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request('GET', path)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        return ret[2]

