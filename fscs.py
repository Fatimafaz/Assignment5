bursttime =[ 2,3,4,5,6]
arrivaltime=[1,2,3,4,5]
turntime=[0]*5

waitingtime=[0]*5

finishtime=0
startime=0

process= [p1,p3,p2,p4,p5]


for index in range(5)

	print(process[index]), ':'
	finishtime=finishtime+bursttime[index]
	waitingtime[index]=startime-arrivaltime[index]
	turntime[index]=finishtime-arrivaltime[index]
	startime=startime+bursttime[index]

	print "waiting time  : " , waitingtime[index], " turntime : "  , turntime[index]
