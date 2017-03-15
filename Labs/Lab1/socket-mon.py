import psutil
import operator




store={}

for line in psutil.net_connections(kind='tcp'):

	if(str(line.pid) != "None" and str(line.raddr)!="()" and str(line.laddr) != "None" and str(line.raddr) != "None"):
		pid=int(line.pid)
		laddr=str(line.laddr)
		raddr=str(line.raddr)
		status=str(line.status)
		laddr1=""
		laddr2=""
		if laddr.startswith('(') and laddr.endswith(')'):
			laddr = laddr[1:-1]
			laddr1,laddr2=laddr.split(',')
			if laddr1.startswith('\'') and laddr1.endswith('\''):
				laddr1 = laddr1[1:-1]
				laddr2 = laddr2[1:]

		laddr="%s@%s" %(laddr1,laddr2)

		raddr1=""
		raddr2=""
		if raddr.startswith('(') and raddr.endswith(')'):
			raddr = raddr[1:-1]
			raddr1,raddr2=raddr.split(',')
			if raddr1.startswith('\'') and raddr1.endswith('\''):
				raddr1 = raddr1[1:-1]
				raddr2 = raddr2[1:]

		raddr="%s@%s" %(raddr1,raddr2)
		#print '"%s", "%s", "%s", "%s" \n' %(pid, laddr, raddr,status)
		

		nu = 1
		
		if pid in store:
		#if store.has_key(pid):
  			#print pid, " FOUND"
  			nu=1+store[pid][0]
  			store[pid][0]=nu
  			store[pid].append([laddr1,laddr2, raddr1,raddr2,status])
		else: 
			#print pid," NOT FOUND"
			store[pid] = []
			store[pid].append(1)
			store[pid].append([laddr1,laddr2, raddr1,raddr2,status])

		#print type(store[pid][0])
		#print "pid=",pid, "nu=",store[pid][0]
#print  store


print '"pid", "laddr", "raddr", "status" \n'

for key,value in sorted(store.iteritems(), key=operator.itemgetter(1),reverse=True):
#for key,value in sorted(store.iteritems(), key=lambda x:(x[0]),reverse=True):
		#print "key",key, "value",value, "\n\n"
	
	#print "pid=",key, "nu=",value[0]

	for i in value:
		#for j in i[1]:
		#	print
		if type(i) is list:
			print '"%d", "%s@%s", "%s@%s", "%s" \n' %(key,i[0], i[1],i[2],i[3],i[4])
#for key,value in sorted(store.iteritems(), key=lambda x:(x[6],x[1])):
#	print '"%d", "%s@%s", "%s@%s", "%s" \n' %(store[key][0], store[key][1],store[key][2],store[key][3],store[key][4], store[key][5])

#[t[0] for t in sorted(d.items(), key=lambda x:(x[1],x[0]))]

