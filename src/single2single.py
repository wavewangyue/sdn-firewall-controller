import httplib
import json


def allow_single2single(server,src,dst,prio=0):
    path = '/wm/firewall/rules/json'
    conn =  httplib.HTTPConnection(server, 8080)
    if (prio == 0):
        rule =json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst})
    else:
        rule =json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst,"priority":"%d"%prio})
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]


def deny_single2single(server,src,dst,prio=0):
    path = '/wm/firewall/rules/json'
    conn = httplib.HTTPConnection(server, 8080)
    if (prio == 0):
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst,"action":"DENY"})
    else:
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst,"priority":"%d"%prio,"action":"DENY"})
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]


