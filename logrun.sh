#!/bin/bash
cd `dirname $0`
iptables -t mangle -F
tc qdisc del dev eth0 root > /dev/null 2>&1
tc qdisc add dev eth0 root handle 1: htb r2q 1;
python_ver=$(ls /usr/bin|grep -e "^python[2]\.[1-9]\+$"|tail -1)
eval $(ps -ef | grep "[0-9] ${python_ver} server\\.py m" | awk '{print "kill "$2}')
ulimit -n 512000
nohup ${python_ver} server.py m>> ssserver.log 2>&1 &



