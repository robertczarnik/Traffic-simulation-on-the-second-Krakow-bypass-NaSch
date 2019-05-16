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
    def __init__(self,vehicle,crossroads=False,crossing_id=None,index=None):
        self.vehicle=vehicle
        self.crossroads=crossroads
        self.crossing_id=crossing_id
        self.index=index
        self.speed_limit=4 
       
      
        
def traffic_ligths1(x):
    if(x==1):
        main_road1.lane[23].vehicle=2
        main_road2.lane[23].vehicle=2
        main_road3.lane[23].vehicle=2
        main_road4.lane[28].vehicle=2
        main_road5.lane[28].vehicle=2
        main_road6.lane[28].vehicle=2
        r1.lane[7].vehicle=0
        r1.lane[14].vehicle=0
        r2.lane[7].vehicle=0
        r2.lane[14].vehicle=0
    elif(x==-1):
        main_road1.lane[23].vehicle=0
        main_road2.lane[23].vehicle=0
        main_road3.lane[23].vehicle=0
        main_road4.lane[28].vehicle=0
        main_road5.lane[28].vehicle=0
        main_road6.lane[28].vehicle=0
        r1.lane[7].vehicle=2
        r1.lane[14].vehicle=2
        r2.lane[7].vehicle=2
        r2.lane[14].vehicle=2
        
    
#representing roads
main_road4_len=55
main_road5_len=55
main_road6_len=55
main_road1_len=80
main_road2_len=80
main_road3_len=80

r1_len=26
r2_len=26
r3_len=10 #z koncem drogi

main_road4 = [0] * main_road4_len
main_road5 = [0] * main_road5_len
main_road6 = [0] * main_road6_len
main_road1 = [0] * main_road1_len
main_road2 = [0] * main_road2_len
main_road3 = [0] * main_road3_len

r1 = [0] * r1_len
r2 = [0] * r2_len
r3 = [0] * r3_len


for i in range(main_road4_len):
    main_road4[i]=Cell(0,False)
    
for i in range(main_road5_len):
    main_road5[i]=Cell(0,False)
    
for i in range(main_road6_len):
    main_road6[i]=Cell(0,False)

for i in range(main_road1_len):
    main_road1[i]=Cell(0,False)
    
for i in range(main_road2_len):
    main_road2[i]=Cell(0,False)
    
for i in range(main_road3_len):
    main_road3[i]=Cell(0,False)
    
for i in range(r1_len):
    r1[i]=Cell(0,False)
    
for i in range(r2_len):
    r2[i]=Cell(0,False)
    
for i in range(r3_len):
    r3[i]=Cell(0,False)


main_road1[24]=Cell(0,True,1,15)
main_road1[25]=Cell(0,True,2,15)

main_road2[24]=Cell(0,True,1,16)
main_road2[25]=Cell(0,True,2,16)

main_road3[24]=Cell(0,True,1,17)
main_road3[25]=Cell(0,True,2,17)

main_road4[29]=Cell(0,True,1,8)
main_road4[30]=Cell(0,True,2,8)

main_road5[29]=Cell(0,True,1,9)
main_road5[30]=Cell(0,True,2,9)

main_road6[29]=Cell(0,True,1,10)
main_road6[30]=Cell(0,True,2,10)

main_road3[42]=Cell(0,True,1,8) #r3


r1[8]=Cell(0,True,1,30)
r1[9]=Cell(0,True,2,30)
r1[10]=Cell(0,True,3,30)
r1[15]=Cell(0,True,4,24) #tutaj juz ta droga krzyzuje sie po kolei z trzema innymi
r1[16]=Cell(0,True,5,24)
r1[17]=Cell(0,True,6,24)


r2[8]=Cell(0,True,1,25)  #droga do gory
r2[9]=Cell(0,True,2,25)
r2[10]=Cell(0,True,3,25)
r2[15]=Cell(0,True,4,29)  #droga do gory
r2[16]=Cell(0,True,5,29)
r2[17]=Cell(0,True,6,29)

r3[8]=Cell(0,True,1,42) #r3
r3[9]=Cell(3) #r3 #koniec drogi - musisz skrecic


main_road4 = Road(main_road4)
main_road5 = Road(main_road5)
main_road6 = Road(main_road6)
main_road1 = Road(main_road1)
main_road2 = Road(main_road2)
main_road3 = Road(main_road3)

#ustawienie sasiednich pasow
main_road6.r_road=main_road5
main_road5.l_road=main_road6
main_road5.r_road=main_road4
main_road4.l_road=main_road5
main_road1.r_road=main_road2
main_road2.l_road=main_road1
main_road2.r_road=main_road3
main_road3.l_road=main_road2


r1 = Road(r1) #!!
r2 = Road(r2) #!!
r3 = Road(r3)


main_road4.other_roads=[r2,r1] #dodanie drog z ktorymi sie po kolei krzyzuja
main_road5.other_roads=[r2,r1]
main_road6.other_roads=[r2,r1]

main_road1.other_roads=[r1,r2] #dodanie drog z ktorymi sie po kolei krzyzuja
main_road2.other_roads=[r1,r2]
main_road3.other_roads=[r1,r2,r3]

r1.other_roads=[main_road4,main_road5,main_road6,main_road1,main_road2,main_road3] #!!
r2.other_roads=[main_road3,main_road2,main_road1,main_road6,main_road5,main_road4] #!!
r3.other_roads=[main_road3]








    