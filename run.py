from flask import Flask
from flask import render_template
from flask import request
from src import controller

ip_floodlight = '192.168.3.199'
app = Flask(__name__)
wall = controller.init(ip_floodlight)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/control/switch_status')
def switch_status():
    return controller.switch_status(wall)


@app.route('/control/switch_on')
def switch_on():
    return controller.switch_on(wall)


@app.route('/control/switch_off')
def switch_off():
    return controller.switch_off(wall)


@app.route('/control/rule_status')
def rule_status():
    return controller.rule_status(ip_floodlight)


@app.route('/control/rule_append')
def rule_append():
    myinput = []
    for i in range(10):
        myinput.append(request.args.get("input" + str(i)))
    return controller.rule_append(ip_floodlight, myinput)


@app.route('/control/rule_delete')
def rule_delete():
    num = request.args.get("num")
    return controller.rule_delete(ip_floodlight, num)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0', use_reloader=False)
