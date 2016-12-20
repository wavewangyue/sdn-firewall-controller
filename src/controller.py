import single2single
from get_status import FireWallInit
import full_network_connection
import get_rules
import delete
import single2subnet
import subnet2subnet
import based_protocol
import based_port


def init(ip_floodlight):
    wall = FireWallInit(ip_floodlight)
    full_network_connection.full_network_connection(ip_floodlight)
    wall.enable_firewall()
    return wall


def switch_status(wall):
    print "Controller: get switch status"
    return wall.get_status()


def switch_on(wall):
    print "Controller: switch on"
    return wall.enable_firewall()


def switch_off(wall):
    print "Controller: switch off"
    return wall.disable_firewall()


def rule_status(ip_floodlight):
    print "Controller: get rules status"
    return get_rules.get_rules(ip_floodlight)


def rule_append(ip_floodlight, myinput):
    print "Controller: append new rule " + ','.join(myinput)
    if myinput[0] == "P2P":
        if myinput[8] == "y":
            return single2single.allow_single2single(ip_floodlight, myinput[1], myinput[4], int(myinput[9]))
        else:
            return single2single.deny_single2single(ip_floodlight, myinput[1], myinput[4], int(myinput[9]))
    elif myinput[0] == "P2S":
        if myinput[8] == "y":
            return single2subnet.allow_single2subnet(ip_floodlight, myinput[1], myinput[4], int(myinput[5]), int(myinput[9]))
        else:
            return single2subnet.deny_single2subnet(ip_floodlight, myinput[1], myinput[4], int(myinput[5]), int(myinput[9]))
    elif myinput[0] == "S2S":
        if myinput[8] == "y":
            return subnet2subnet.allow_subnet2subnet(ip_floodlight, myinput[1], int(myinput[2]), myinput[4], int(myinput[5]), int(myinput[9]))
        else:
            return subnet2subnet.deny_subnet2subnet(ip_floodlight, myinput[1], int(myinput[2]), myinput[4], int(myinput[5]), int(myinput[9]))
    elif myinput[0] == "PRO":
        if myinput[8] == "y":
            return based_protocol.allow_protocol(ip_floodlight, myinput[1], myinput[4], myinput[7], int(myinput[9]))
        else:
            return based_protocol.deny_protocol(ip_floodlight, myinput[1], myinput[4], myinput[7], int(myinput[9]))
    elif myinput[0] == "PORT":
        if myinput[8] == "y":
            return based_port.allow_port(ip_floodlight, myinput[1], int(myinput[3]), myinput[4], int(myinput[6]), myinput[7], int(myinput[9]))
        else:
            return based_port.deny_port(ip_floodlight, myinput[1], int(myinput[3]), myinput[4], int(myinput[6]), myinput[7], int(myinput[9]))


def rule_delete(ip_floodlight, num):
    print "Controller: delete rule "+num
    return delete.delete_rule(ip_floodlight, int(num))

