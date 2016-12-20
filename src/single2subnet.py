import httplib
import json


def allow_single2subnet(server,src,dst,d_mask,prio=0):
    path = '/wm/firewall/rules/json'
    conn =  httplib.HTTPConnection(server, 8080)
    if (prio == 0):
        rule =json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/%d"%(dst,d_mask)})
        print rule
    else:
        rule =json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/%d"%(dst,d_mask),"priority":"%d"%prio})
        print rule
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]


def deny_single2subnet(server,src,dst,d_mask,prio=0):
    path = '/wm/firewall/rules/json'
    conn = httplib.HTTPConnection(server, 8080)
    print d_mask
    if (prio == 0):
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/%d"%(dst,d_mask),"action":"DENY"})
        print rule
    else:
        rule = json.dumps({"src-ip":"%s/32"%src,"dst-ip":"%s/%d"%(dst,d_mask),"priority":"%d"%prio,"action":"DENY"})
        print rule
    conn.request('POST', path, rule)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]




