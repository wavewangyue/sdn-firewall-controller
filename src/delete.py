import httplib
import json


path = '/wm/firewall/rules/json'


def delete_all_rules(server):
    conn = httplib.HTTPConnection(server, 8080)
    conn.request('GET', path)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    rules = json.loads(ret[2])

    print (len(rules))
    for i in range(len(rules)):
        rule_id = "{\"ruleid\":\"%s\"}" %rules[i]['ruleid']
        headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
                }
        conn = httplib.HTTPConnection(server, 8080)
        conn.request('DELETE',path,rule_id,headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        return ret[2]


def delete_rule(server, ruleid):
    rule_id = '{\"ruleid\":\"%s\"}'%ruleid
    headers = {
            'content-type': 'application/json',
            'Accept': 'application/json'
            }
    conn = httplib.HTTPConnection(server, 8080)
    conn.request('DELETE',path, rule_id, headers)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    return ret[2]

