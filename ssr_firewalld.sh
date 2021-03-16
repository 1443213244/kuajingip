#!/bin/bash

IPT='/sbin/iptables'
IP=('112.73.24.219' '149.129.59.34' '8.210.6.77' '157.119.73.119' '69.172.75.87')



SetFirewalld(){
    #echo "Set Firewalld"
    port=`ss -lnp |grep pid=$pid|grep tcp|sort -g|awk -F" " '{ print $5}'|awk -F":" '{ print $2}'|sort -g|head -1`
    let end=port+252
    $IPT -F

    for((i=0;i<=${#IP[@]}-1;i++))
    do
        $IPT -I INPUT -p tcp -s ${IP[i]} --dport $port:$end -j ACCEPT
        $IPT -I INPUT -p tcp -s ${IP[i]} --dport 22 -j ACCEPT
        $IPT -I INPUT -s ${IP[i]} -p icmp -j ACCEPT
    done

    
    $IPT -A INPUT -p tcp --dport $port:$end -j DROP
    $IPT -A INPUT -p tcp --dport 22 -j DROP
    $IPT -A INPUT -p icmp -j DROP    
    $IPT -nvL

}


CheckSSR(){
        pid=`ps -ef|grep server.py|grep python|awk '{print $2}'`
        if [ -z "$pid" ]; then
            echo "Please start SSR and try again"
            #sleep 30
            #CheckSSR
        else
            SetFirewalld
        fi
}

CheckSSR




