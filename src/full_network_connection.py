import httplib
import json


path_switches = '/wm/core/controller/switches/json'
path_rules = '/wm/firewall/rules/json'


def full_network_connection(server):
    conn = httplib.HTTPConnection(server, 8080)
    conn.request('GET', path_switches)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    switches = json.loads(ret[2])

    print (len(switches))
    for i in range(len(switches)):
        switch = json.dumps({"switchid":switches[i]['dpid'],"priority":9})
        conn = httplib.HTTPConnection(server, 8080)
        conn.request('POST', path_rules, switch)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret[2]

