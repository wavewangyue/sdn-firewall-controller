import httplib


def get_rules(server):
    path = '/wm/firewall/rules/json'
    conn = httplib.HTTPConnection(server, 8080)
    conn.request('GET', path)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]
