

countofproc=input('How many processes you want to make ? ' )
finishtime=0
startime=0
avgturntim=0

proclist=[0]*countofproc

for index in range(countofproc)
    
    proclist[index]=dict{}
    
    processID=input('Enter the name of the process')
    dict['processID']=processID
    
    arrivaltime=input('Enter the value of arrival time of the process')
    dict['arrival_Time']=arrivaltime
    
    burstime=input('what is the burst time for your process')
    dict['Burst_time']=burstime

    dict['waitingtime']=0

    dict['turnaround_time']=0
timecheck=0
for index in range(countofproc)
    for index2 in range(countofproc-index)

    if proclist[index2]['Burst_time']>proclist[index2+1] and proclist[ndex2]['arrival_time]>timecheck

    tempdict=proclist[index]
    proclist[index]=proclist[index+1]
    proclist[index+1]=tempdict
timecheck=timecheck+proclist[index2]['Burst_time']    
                                                                             



for index in range(countofproc)
    print proclist[index]['processID']
    finishtime=finishtime+proclist[index]['Burst_time']
    proclist[index]['waitingtime']=startime-proclist[index]['arrival_time']
    proclist[index]['turnaround_time']=finishtime-proclist[index]['arrivaltime']
    avgturntime=avgturntim+ proclist[index]['turnaround_time']
    avgwaittime=avgwaitim+ proclist[index]['turnaround_time']
    print 'waitingtime : ' , proclist[index]['waitingtime']
    print 'turnaround time : ' , proclist[index]['waitingtime']
    print 'average turnaround time : ' , avgturntim
    print 'average waiting time : ' , avgwaitim
