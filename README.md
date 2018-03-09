# PubgPing

Python 2.7 脚本

测试当前主机与绝地求生服务器的网络连接状态，原理来自于http://pubg.disquse.ru

# CentOS下用法：
1. 下载py文件

wget https://raw.githubusercontent.com/itpansic/PubgPing/master/pubg.py

2. 如果提示-bash: wget: command not found， 则代表wget命令没有安装，执行下列代码安装wget再执行第1步

yum install -y wget

3. 启动脚本

python -u pubg.py