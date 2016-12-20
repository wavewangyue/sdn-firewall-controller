import httplib  
import json  
  
class StaticFlowPusher(object):  
  
    def __init__(self, server):  
        self.server = server  
  
    def get(self, data):  
        ret = self.rest_call({}, 'GET')  
        return json.loads(ret[2])  
  
    def set(self, data):  
        ret = self.rest_call(data, 'POST')  
        return ret[0] == 200  
  
    def remove(self, objtype, data):  
        ret = self.rest_call(data, 'DELETE')  
        return ret[0] == 200  
  
    def rest_call(self, data, action):  
        path = '/wm/staticflowentrypusher/json'  
        headers = {  
            'Content-type': 'application/json',  
            'Accept': 'application/json',  
            }  
        body = json.dumps(data)  
        conn = httplib.HTTPConnection(self.server, 8080)  
        conn.request(action, path, body, headers)  
        response = conn.getresponse()  
        ret = (response.status, response.reason, response.read())  
        print ret  
        conn.close()  
        return ret  
  
pusher = StaticFlowPusher('192.168.0.93')  
  
flow1 = {  
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"flow-mod-1",  
    "cookie":"0",  
    "priority":"32768", 
    "src-ip":"192.168.0.0/24",
    "dst-ip":"192.168.1.1",  
    "active":"true",  
    "actions":"output=3"  
    }  
      
flow2 = {  
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"2",  
    "active":"true",  
    "actions":"output=flood"  
    }  

flow3 = {  
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"3",  
    "active":"true",  
    "actions":"output=flood"  
    }  
    
flow4 = {  
    'switch':"00:00:00:00:00:00:00:02",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"1",  
    "active":"true",  
    "actions":"output=flood"  
    }  
    
flow5 = {  
    'switch':"00:00:00:00:00:00:00:02",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"2",  
    "active":"true",  
    "actions":"output=flood"  
    }
    
flow6 = {  
    'switch':"00:00:00:00:00:00:00:02",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"3",  
    "active":"true",  
    "actions":"output=flood"  
    }

flow7 = {  
    'switch':"00:00:00:00:00:00:00:02",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"4",  
    "active":"true",  
    "actions":"output=flood"  
    }
    
flow8 = {  
    'switch':"00:00:00:00:00:00:00:03",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"1",  
    "active":"true",  
    "actions":"output=flood"  
    }  
    
flow9 = {  
    'switch':"00:00:00:00:00:00:00:03",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"2",  
    "active":"true",  
    "actions":"output=flood"  
    }  
    
flow10 = {  
    'switch':"00:00:00:00:00:00:00:03",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"3",  
    "active":"true",  
    "actions":"output=flood"  
    }
    
flow11 = {  
    'switch':"00:00:00:00:00:00:00:03",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"4",  
    "active":"true",  
    "actions":"output=flood"  
    }

flow12 = {  
    'switch':"00:00:00:00:00:00:00:03",  
    "name":"flow-mod-2",  
    "cookie":"0",  
    "priority":"32768",  
    "ingress-port":"5",  
    "active":"true",  
    "actions":"output=flood"  
    }  
pusher.set(flow1)  
pusher.set(flow2)  
pusher.set(flow3)  
pusher.set(flow4)  
pusher.set(flow5)  
pusher.set(flow6)  
pusher.set(flow7)  
pusher.set(flow8)  
pusher.set(flow9)  
pusher.set(flow10)  
pusher.set(flow11)  
pusher.set(flow12)  
