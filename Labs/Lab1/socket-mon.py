import psutil
import operator

print '"pid", "laddr", "raddr", "status" \n'

i=0
store={}

for line in psutil.net_connections(kind='tcp'):

	if(str(line.pid) != "None" and str(line.raddr)!="()"):
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
		store[i] = []

		nu = 1

		if(pid in store.values()):
			nu=nu+store[key][6]
		else:
			nu=1


		store[i].extend([pid, laddr1,laddr2, raddr1,raddr2,status,nu])

		i=i+1

#print  store

#for key,value in sorted(store.iteritems(), key=operator.itemgetter(1)):
#	print '"%d", "%s@%s", "%s@%s", "%s" \n' %(store[key][0], store[key][1],store[key][2],store[key][3],store[key][4], store[key][5])


for key,value in sorted(store.iteritems(), key=lambda x:(x[6],x[1])):
	print '"%d", "%s@%s", "%s@%s", "%s" \n' %(store[key][0], store[key][1],store[key][2],store[key][3],store[key][4], store[key][5])

#[t[0] for t in sorted(d.items(), key=lambda x:(x[1],x[0]))]
#['Bob', 'Alex', 'Bill', 'Charles']
