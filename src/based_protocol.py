import httplib
import json


def allow_protocol(server, src,dst,proto,prio=0):
    path = '/wm/firewall/rules/json'
    conn =  httplib.HTTPConnection(server, 8080)
    if (prio == 0):
        rule =json.dumps({"src-ip":"%s/32"%(src),"dst-ip":"%s/32"%(dst),"nw-proto":"%s"%proto})
        print rule
    else:
        rule =json.dumps({"src-ip":"%s/32"%(src),"dst-ip":"%s/32"%(dst),"nw-proto":"%s"%proto,"priority":"%d"%prio})
        print rule
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]


def deny_protocol(server,src,dst,proto,prio=0):
    path = '/wm/firewall/rules/json'
    conn = httplib.HTTPConnection(server, 8080)
    if (prio == 0):
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst,"nw-proto":"%s"%proto,"action":"DENY"})
        print rule
    else:
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/32"%dst,"nw-proto":"%s"%proto,"priority":"%d"%prio,"action":"DENY"})
        print rule
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]