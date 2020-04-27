#!/bin/bash

yum install ntpdate -y
ntpdate time.windows.com
GATEWAY=`ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"`
cd /home/shadowsocksr
bash stop.sh
cd /home
rm -rf shadowsocksr
wget http://76.cserver.org/shadowsocksr-tc.tar
tar xvf  shadowsocksr-tc.tar
cd /home/shadowsocksr
sed -i 's/45.207.25.1/'$GATEWAY'/' /home/shadowsocksr/user-config.json
bash run.sh
