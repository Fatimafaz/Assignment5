countofproc=input('How many processes you want to make ? ' )
finishtime=0
startime=0
avgturntim=0
avgwaittime=0
quantumtime=2

proclist=[0]*countofproc

for index in range(countofproc)
    
    proclist[index]=dict{}
    
    processID=input('Enter the name of the process')
    dict['processID']=processID
    
    arrivaltime=input('Enter the value of arrival time of the process')
    dict['arrival_Time']=arrivaltime
    
    burstime=input('what is the burst time for your process')
    dict['Burst_time']=burstime


    dict['RemB_Time']=0

    dict['waitingtime']=0

    dict['turnaround_time']=0

for index1 in range(countofproc-1):
    for index2 in range(countofproc-1-index1):

    if proclist[index2]['arrivaltime']>proclist[index2]['arrivaltime']:

    tempdict=proclist[index2]
    proclist[index2]=proclist[index2+1]
    proclist[index2+1]=tempdict

for index in range(countofproc):
    proclist[index]['RemB_time']=proclist[index]['Burst_time']

timecheck=0

for index in range(countofproc):
    if(proclist[index]['RemB_time']>quantumtime):
        timecheck=timecheck+quantumtime
        proclist[index]['RemB_Time']=proclist[index]['RemB_Time']-quantumtime
        print (proclist[index]['processID'] , ':' , timecheck

    elif(proclist[index]['RemB_Time']<=quantumtime and proclist[index]['RemB_Time']>0):
               timecheck=timecheck+proclist[index]['RemB_Time']
               proclist[index]['RemB_Time']=0
               print (proclist[index]['processID'] , ':' , timecheck
               proclist[index]['waitingtime']=timecheck- proclist[index]['Burst_Time']- plist[index]['arrivaltime']
               proclist[index]['turnaround_time']=timecheck-proclist[index]['arrival_time']
for indexOut in range(countofproc):
     print proclist[indexOut]
     avgwaittime=avgwaittime+proclist[indexOut]['waitingime']/countofproc
     avgturntime=avgturntime+proclist[indexOut]['turnaround_time']/countofproc
print 'Average waiting time : '] ,avgwaittime
print 'Average turnaround time :' ],avgturntime
                                            

    
