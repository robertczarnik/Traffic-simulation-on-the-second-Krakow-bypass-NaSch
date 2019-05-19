#0-wolna komorka 1-zajeta komorka 2-czerwone swiatlo 3-koniec drogi(koniecznosc zmiany pasa)

class Road(object):
    def __init__(self,lane,l_road=None,r_road=None,other_roads=None):
        self.lane=lane
        self.l_road=l_road
        self.r_road=r_road
        self.other_roads=other_roads #roads that cross this road
               
    def print_road(self,reverse=False):
        if(not reverse):
            for i in range(len(self.lane)):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')
        else: #droga z prawej do lewej
            for i in range(len(self.lane)-1,-1,-1):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')


class Cell(object):
    def __init__(self,vehicle,crossroads=False,crossing_id=None,index=None,speed_limit=4):
        self.vehicle=vehicle
        self.crossroads=crossroads
        self.crossing_id=crossing_id
        self.index=index
        self.speed_limit=speed_limit 
    
    
def traffic_lights_management(traffic_lights_timer):
    if(traffic_lights_timer==60):
        traffic_lights_timer=0
    
    if(traffic_lights_timer==0):
        traffic_ligths1(1)
     
    if(traffic_lights_timer==17):
        traffic_ligths1(2)    
        
    elif(traffic_lights_timer==20):
        traffic_ligths1(3)
        
    elif(traffic_lights_timer==35):
        traffic_ligths1(4)
        
    elif(traffic_lights_timer==45):
        traffic_ligths1(5)
        
    traffic_lights_timer+=1
        
        
def traffic_ligths1(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[23].vehicle=0
        main_road2.lane[23].vehicle=0
        main_road3.lane[23].vehicle=0
        main_road4.lane[28].vehicle=0
        main_road5.lane[28].vehicle=0
        main_road6.lane[28].vehicle=0
        r1.lane[18].vehicle=2
        r2.lane[18].vehicle=2
        r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[23].vehicle=2
        main_road2.lane[23].vehicle=2
        main_road3.lane[23].vehicle=2
        main_road4.lane[28].vehicle=2
        main_road5.lane[28].vehicle=2
        main_road6.lane[28].vehicle=2
    elif(x==3):
        r1.lane[18].vehicle=0
        r2.lane[18].vehicle=0
    elif(x==4):
        r1.lane[11].vehicle=0
        r2.lane[11].vehicle=0
    elif(x==5):
        r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
        
    
###representing roads###
########################## roads init with empty cells ################################       
main_road4 = [Cell(0) for i in range(55)]
main_road5 = [Cell(0) for i in range(55)]
main_road6 = [Cell(0) for i in range(55)]
main_road1 = [Cell(0) for i in range(115)]
main_road2 = [Cell(0) for i in range(115)]
main_road3 = [Cell(0) for i in range(115)]
r1 = [Cell(0) for i in range(34)]
r2 = [Cell(0) for i in range(34)]
r3 = [Cell(0) for i in range(14)]
r4 = [Cell(0) for i in range(34)]
r5 = [Cell(0) for i in range(22)]
r6 = [Cell(0) for i in range(34)]
r7 = [Cell(0) for i in range(21)]
r8 = [Cell(0) for i in range(34)]
r9 = [Cell(0) for i in range(14)]
r10 = []
r11 = []
r12 = []
r13 = [Cell(0) for i in range(17)] 
r14 = [Cell(0) for i in range(18)]    
r15 = []

########################## special cells and init roads obj ###########################
#main_road1
main_road1[24]=Cell(0,True,1,19) #r1
main_road1[25]=Cell(0,True,2,14) #r2
main_road1[59]=Cell(0,True,4,19) #r4
main_road1[60]=Cell(0,True,5,2)  #r5
main_road1[73]=Cell(0,True,6,19) #r6
main_road1[74]=Cell(0,True,7,19) #r7
main_road1[75]=Cell(0,True,8,14) #r8
main_road1[102]=Cell(0,True,13,15)#r13 #nie ma pasa zieleni pomiedzy drogami
main_road1[104]=Cell(0,True,14,2) #r14 
main_road1 = Road(main_road1)
#---

#main_road2
main_road2[24]=Cell(0,True,1,20) #r1
main_road2[25]=Cell(0,True,2,13) #r2
main_road2[59]=Cell(0,True,4,20) #r4
main_road2[60]=Cell(0,True,5,1)  #r5
main_road2[73]=Cell(0,True,6,20) #r6
main_road2[75]=Cell(0,True,8,13) #r8
main_road2[104]=Cell(0,True,14,1) #r14 
main_road2 = Road(main_road2)
#---

#main_road3
main_road3[24]=Cell(0,True,1,21) #r1
main_road3[25]=Cell(0,True,2,12) #r2
main_road3[42]=Cell(0,True,3,12) #r3
main_road3[59]=Cell(0,True,4,21) #r4
main_road3[60]=Cell(0,True,5,0)  #r5
main_road3[73]=Cell(0,True,6,21) #r6
main_road3[75]=Cell(0,True,8,12) #r8
main_road3[76]=Cell(0,True,9,12) #r9
main_road3[104]=Cell(0,True,14,0) #r14 
main_road3 = Road(main_road3)
#---

#main_road4
main_road4[29]=Cell(0,True,1,12) #r2
main_road4[30]=Cell(0,True,2,12) #r1
main_road4 = Road(main_road4)
#---

#main_road5
main_road5[29]=Cell(0,True,1,13) #r2
main_road5[30]=Cell(0,True,2,13) #r1
main_road5 = Road(main_road5)
#---

#main_road6
main_road6[29]=Cell(0,True,1,14) #r2
main_road6[30]=Cell(0,True,2,14) #r1
main_road6 = Road(main_road6)
#---

#r1 \/
r1[12]=Cell(0,True,1,30)  #mr4
r1[13]=Cell(0,True,2,30)  #mr5
r1[14]=Cell(0,True,3,30) #mr6
r1[19]=Cell(0,True,4,24) #mr1
r1[20]=Cell(0,True,5,24) #mr2
r1[21]=Cell(0,True,6,24) #mr3
r1 = Road(r1)
#---

#r2 /\
r2[12]=Cell(0,True,1,25)  #mr3
r2[13]=Cell(0,True,2,25)  #mr2
r2[14]=Cell(0,True,3,25) #mr1
r2[19]=Cell(0,True,4,29) #mr6
r2[20]=Cell(0,True,5,29) #mr5
r2[21]=Cell(0,True,6,29) #mr4
r2 = Road(r2)
#---

#r3 /\
r3[12]=Cell(0,True,1,42)  #mr3
r3[13]=Cell(3) #end of road
r3 = Road(r3)
#---

#r4 \/
#r4[8]=Cell(0,True,1,30)  #mr4
#r4[9]=Cell(0,True,2,30)  #mr5
#r4[10]=Cell(0,True,3,30) #mr6
r4[19]=Cell(0,True,4,59) #mr1
r4[20]=Cell(0,True,5,59) #mr2
r4[21]=Cell(0,True,6,59) #mr3
r4 = Road(r4)
#---

#r5 /\
r5[0]=Cell(0,True,1,60)  #mr3
r5[1]=Cell(0,True,2,60)  #mr2
r5[2]=Cell(0,True,3,60)  #mr1
#r5[15]=Cell(0,True,4,29) #mr6
#r5[16]=Cell(0,True,5,29) #mr5
#r5[17]=Cell(0,True,6,29) #mr4
r5 = Road(r5)
#---

#r6 \/
#r6[12]=Cell(0,True,1,30)  #mr4
#r6[13]=Cell(0,True,2,30)  #mr5
#r6[14]=Cell(0,True,3,30) #mr6
r6[19]=Cell(0,True,4,73) #mr1
r6[20]=Cell(0,True,5,73) #mr2
r6[21]=Cell(0,True,6,73) #mr3
r6 = Road(r6)
#---

#r7 \/
r7[19]=Cell(0,True,4,74)   #mr1
r7[20]=Cell(3) #end of road
r7 = Road(r7)
#---

#r8 /\
r8[12]=Cell(0,True,1,75)  #mr3
r8[13]=Cell(0,True,2,75)  #mr2
r8[14]=Cell(0,True,3,75)  #mr1
#r8[19]=Cell(0,True,4,29) #mr6
#r8[20]=Cell(0,True,5,29) #mr5
#r8[21]=Cell(0,True,6,29) #mr4
r8 = Road(r8)
#---

#r9 /\
r9[12]=Cell(0,True,1,76)  #mr3
r9[13]=Cell(3) #end of road
r9 = Road(r9)
#---

#r13 \/
r13[15]=Cell(0,True,4,102)  #mr1
r13[16]=Cell(3) #end of road
r13 = Road(r13)
#---

#r14 /\
r14[0]=Cell(0,True,1,104)  #mr3
r14[1]=Cell(0,True,2,104)  #mr2
r14[2]=Cell(0,True,3,104)  #mr1
#r14[3]=Cell(0,True,4,75)  #mr6
#r14[4]=Cell(0,True,5,75)  #mr5
#r14[5]=Cell(0,True,6,75)  #mr4
r14 = Road(r14)
#---


########################## setting neighbors and other roads ##########################
#main_road1
main_road1.r_road=main_road2
main_road1.other_roads=[r1,r2,None,r4,r5,r6,r7,r8,None,None,None,None,r13,r14]
#---

#main_road2
main_road2.l_road=main_road1
main_road2.r_road=main_road3
main_road2.other_roads=[r1,r2,None,r4,r5,r6,None,r8,None,None,None,None,None,r14]
#---

#main_road3
main_road3.l_road=main_road2
main_road3.other_roads=[r1,r2,r3,r4,r5,r6,None,r8,r9,None,None,None,None,r14]
#---

#main_road4
main_road4.l_road=main_road5
main_road4.other_roads=[r2,r1]
#---

#main_road5
main_road5.r_road=main_road4
main_road5.l_road=main_road6
main_road5.other_roads=[r2,r1]
#---

#main_road6
main_road6.r_road=main_road5
main_road6.other_roads=[r2,r1]
#---

#r1
r1.other_roads=[main_road4,main_road5,main_road6,main_road1,main_road2,main_road3] 
#---

#r2
r2.other_roads=[main_road3,main_road2,main_road1,main_road6,main_road5,main_road4]
#---

#r3
r3.other_roads=[main_road3]
#---

#r4
r4.other_roads=[None,None,None,main_road1,main_road2,main_road3]
#---

#r5
r5.other_roads=[main_road3,main_road2,main_road1,None,None,None]
#---

#r6
r6.other_roads=[None,None,None,main_road1,main_road2,main_road3]
#---

#r7
r7.other_roads=[None,None,None,main_road1]
#---

#r8
r8.other_roads=[main_road3,main_road2,main_road1,None,None,None]
#---

#r9
r9.other_roads=[main_road3]
#---

#r13
r13.other_roads=[None,None,None,main_road1]
#---

#r14
r14.other_roads=[main_road3,main_road2,main_road1]
#---