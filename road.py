#0-wolna komorka 1-zajeta komorka 2-czerwone swiatlo 3-koniec drogi(koniecznosc zmiany pasa)

class Road(object):
    def __init__(self,lane,l_road=None,r_road=None):
        self.lane=lane
        self.l_road=l_road
        self.r_road=r_road
        self.other_roads=[] #roads that cross this road
               
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
                    print(max(self.lane[i].vehicle , self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
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
        
    
def add_none_to_other_roads(roads_list):
    if(len(roads_list)==1): #1
        if(roads_list[0]!=main_road1):
            main_road1.other_roads.append(None)
        if(roads_list[0]!=main_road2):
            main_road2.other_roads.append(None)
        if(roads_list[0]!=main_road3):
            main_road3.other_roads.append(None)
        if(roads_list[0]!=main_road4):
            main_road4.other_roads.append(None) #dla 3-6 chyba nie append tylko wstawianie do poczatku jaki insert
        if(roads_list[0]!=main_road5):
            main_road5.other_roads.append(None)
        if(roads_list[0]!=main_road6):
            main_road6.other_roads.append(None)
    elif(len(roads_list)==4): #4
        if(roads_list[0]!=main_road1 and roads_list[1]!=main_road1 and roads_list[2]!=main_road1 and roads_list[3]!=main_road1):
            main_road1.other_roads.append(None)
        if(roads_list[0]!=main_road2 and roads_list[1]!=main_road2 and roads_list[2]!=main_road2 and roads_list[3]!=main_road2):
            main_road2.other_roads.append(None)
        if(roads_list[0]!=main_road3 and roads_list[1]!=main_road3 and roads_list[2]!=main_road3 and roads_list[3]!=main_road3):
            main_road3.other_roads.append(None)
        if(roads_list[0]!=main_road4 and roads_list[1]!=main_road4 and roads_list[2]!=main_road4 and roads_list[3]!=main_road4):
            main_road4.other_roads.append(None)
        if(roads_list[0]!=main_road5 and roads_list[1]!=main_road5 and roads_list[2]!=main_road5 and roads_list[3]!=main_road5):
            main_road5.other_roads.append(None)
        if(roads_list[0]!=main_road6 and roads_list[1]!=main_road6 and roads_list[2]!=main_road6 and roads_list[3]!=main_road6):
            main_road6.other_roads.append(None)
    elif(len(roads_list)==6): #6
        if(roads_list[0]!=main_road1 and roads_list[1]!=main_road1 and roads_list[2]!=main_road1 and roads_list[3]!=main_road1 and roads_list[4]!=main_road1 and roads_list[5]!=main_road1):
            main_road1.other_roads.append(None)
        if(roads_list[0]!=main_road2 and roads_list[1]!=main_road2 and roads_list[2]!=main_road2 and roads_list[3]!=main_road2 and roads_list[4]!=main_road2 and roads_list[5]!=main_road2):
            main_road2.other_roads.append(None)
        if(roads_list[0]!=main_road3 and roads_list[1]!=main_road3 and roads_list[2]!=main_road3 and roads_list[3]!=main_road3 and roads_list[4]!=main_road3 and roads_list[5]!=main_road3):
            main_road3.other_roads.append(None)
        if(roads_list[0]!=main_road4 and roads_list[1]!=main_road4 and roads_list[2]!=main_road4 and roads_list[3]!=main_road4 and roads_list[4]!=main_road4 and roads_list[5]!=main_road4):
            main_road4.other_roads.append(None)
        if(roads_list[0]!=main_road5 and roads_list[1]!=main_road5 and roads_list[2]!=main_road5 and roads_list[3]!=main_road5 and roads_list[4]!=main_road5 and roads_list[5]!=main_road5):
            main_road5.other_roads.append(None)
        if(roads_list[0]!=main_road6 and roads_list[1]!=main_road6 and roads_list[2]!=main_road6 and roads_list[3]!=main_road6 and roads_list[4]!=main_road6 and roads_list[5]!=main_road6):
            main_road6.other_roads.append(None)
            
def road_creator(roads_list ,roads_param , crossing_list , template , space_between_roads=0 , one_lane_closed=0):
    road = []
    len_roads=12
    
    if(template == 1): #wjazd
        param = [len_roads + one_lane_closed]
        road = [Cell(0) for i in range(len_roads+1+one_lane_closed)] #+1 bo wjazd
        road=Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
    
    elif(template == 2): #wyjazd
        param = [0]
        road = [Cell(0) for i in range(len_roads+1)] #+1 bo wyjazd
        road=Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
        
    elif(template == 3): #pelna droga
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1,len_roads+2+space_between_roads+2,len_roads+2+space_between_roads+3]
        road = [Cell(0) for i in range(len_roads*2+space_between_roads+6)] #pelna droga
        road = Road(road)
        
        if(roads_list[0]!=None): 
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[1])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[2]]=Cell(0,True,crossing_list[2],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[2])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[3]]=Cell(0,True,crossing_list[3],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[3])
            roads_list[3].other_roads.append(road)
            
        if(roads_list[4]!=None):
            (roads_list[4]).lane[roads_param[4]]=Cell(0,True,crossing_list[4],param[4])
            road.lane[param[4]]=Cell(0,True,5,roads_param[4])
            roads_list[4].other_roads.append(road)
            
        if(roads_list[5]!=None):
            (roads_list[5]).lane[roads_param[5]]=Cell(0,True,crossing_list[5],param[5])
            road.lane[param[5]]=Cell(0,True,6,roads_param[5])
            roads_list[5].other_roads.append(road)
        
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3],roads_list[4],roads_list[5]]
    
    elif(template == 4): #niepelna droga wjazdowa
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1]
        road = [Cell(0) for i in range(len_roads+space_between_roads+4)] #niepelna droga
        road = Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[1])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[2]]=Cell(0,True,crossing_list[2],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[2])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[3]]=Cell(0,True,crossing_list[3],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[3])
            roads_list[3].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3]]

    elif(template == 5): #niepelna droga wyjazdowa
        param = [0,1+space_between_roads,2+space_between_roads,3+space_between_roads]
        road = [Cell(0) for i in range(len_roads+space_between_roads+4)] #niepelna droga
        road = Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[1])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[2]]=Cell(0,True,crossing_list[2],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[2])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[3]]=Cell(0,True,crossing_list[3],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[3])
            roads_list[3].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3]]
        
    return road #zwracam powstałą droge
    
    
###representing roads###
########################## roads init with empty cells ################################       

###representing roads###
#main roads
main_road4 = [Cell(0) for i in range(55)]
main_road5 = [Cell(0) for i in range(55)]
main_road6 = [Cell(0) for i in range(55)]
main_road1 = [Cell(0) for i in range(78)]
main_road2 = [Cell(0) for i in range(78)]
main_road3 = [Cell(0) for i in range(78)]
#for i in range(55):
#    main_road3.append(Cell(3))
main_road1 = Road(main_road1)
main_road2 = Road(main_road2)
main_road3 = Road(main_road3)
main_road4 = Road(main_road4)
main_road5 = Road(main_road5)
main_road6 = Road(main_road6)

main_road1.r_road=main_road2
main_road2.l_road=main_road1
main_road2.r_road=main_road3
main_road3.l_road=main_road2
main_road4.l_road=main_road5
main_road5.r_road=main_road4
main_road5.l_road=main_road6
main_road6.r_road=main_road5  

#other roads
r1=road_creator([None,None,None,main_road1,main_road2,main_road3],[None,None,None,24,24,24],[None,None,None,1,1,1],3,4)
r2=road_creator([main_road3,main_road2,main_road1,None,None,None],[25,25,25,None,None,None],[2,2,2,None,None,None],3,4)
r3=road_creator([main_road3],[42],[3],1)
r4=road_creator([None,None,None,main_road1,main_road2,main_road3],[None,None,None,59,59,59],[None,None,None,4,4,4],3,4)
r5=road_creator([main_road1,None,None,None],[60,None,None,None],[5,None,None,None],5,4)
r6=road_creator([None,None,None,main_road1,main_road2,main_road3],[None,None,None,73,73,73],[None,None,None,6,6,6],3,4)


#r1=road_creator([None,main_road1], [None,24] , [None,1] , 8 , 4 )
#r2=road_creator([main_road1,None], [25,None] , [2,None] , 8 , 4 )
#r3=road_creator([main_road3], [42] , [3] , 1)
#r4=road_creator([None,main_road1], [None,59] , [None,4] , 8 , 4 )
#r5=road_creator([main_road1,None], [60,None] , [5,None] , 9 , 4 )
#r6=road_creator([main_road3], [63] , [6] , 2 )



   
