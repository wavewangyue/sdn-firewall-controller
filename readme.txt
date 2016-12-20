项目部署步骤：
1 启动mininet，指定拓扑文件及控制器ip
    sudo mn --custom mytopo.py --topo mytopo --controller=remote,ip=~~,port=6633
    其中~~为floodlight所在服务器ip
2 启动floodlight
3 安装flask
    sudo pip install flask
4 启动项目
    修改run.py中的ip_floodlight为控制器所在ip
    然后运行python run.py
5 浏览器访问localhost:5000