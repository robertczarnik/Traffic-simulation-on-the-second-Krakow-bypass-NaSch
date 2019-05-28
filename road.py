#0-wolna komorka 1-zajeta komorka 2-czerwone swiatlo 3-koniec drogi(koniecznosc zmiany pasa)

class Road(object):
    def __init__(self,lane,l_road=None,r_road=None):
        self.lane=lane
        self.l_road=l_road
        self.r_road=r_road
        self.other_roads=[] #roads that cross this road
               
    def print_road(self,poczatek,koniec,reverse=False):
        if(not reverse):
            for i in range(poczatek,koniec):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')
        else: #droga z prawej do lewej
            for i in range(koniec-1,poczatek-1,-1):
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
        traffic_ligths2(1)
     
    if(traffic_lights_timer==17):
        traffic_ligths1(2)
        traffic_ligths2(2)
        
    elif(traffic_lights_timer==20):
        traffic_ligths1(3)
        traffic_ligths2(3)
        
    elif(traffic_lights_timer==35):
        traffic_ligths1(4)
        traffic_ligths2(4)
        
    elif(traffic_lights_timer==45):
        traffic_ligths1(5)
        traffic_ligths2(5)
        
    traffic_lights_timer+=1
        
        
def traffic_ligths1(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[23].vehicle=0
        main_road2.lane[23].vehicle=0
        main_road3.lane[23].vehicle=0
        main_road4.lane[1721].vehicle=0
        main_road5.lane[1721].vehicle=0
        main_road6.lane[1721].vehicle=0
        r1.lane[18].vehicle=2
        r2.lane[18].vehicle=2
        #r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[23].vehicle=2
        main_road2.lane[23].vehicle=2
        main_road3.lane[23].vehicle=2
        main_road4.lane[1721].vehicle=2
        main_road5.lane[1721].vehicle=2
        main_road6.lane[1721].vehicle=2
    elif(x==3):
        r1.lane[18].vehicle=0
        r2.lane[18].vehicle=0
    elif(x==4):
        r1.lane[11].vehicle=0
        r2.lane[11].vehicle=0
    elif(x==5):
        #r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
        
def traffic_ligths2(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[58].vehicle=0
        main_road2.lane[58].vehicle=0
        main_road3.lane[58].vehicle=0
        main_road4.lane[1686].vehicle=0
        main_road5.lane[1686].vehicle=0
        main_road6.lane[1686].vehicle=0
        r4.lane[18].vehicle=2
        r5.lane[18].vehicle=2
        r4.lane[11].vehicle=2
        r5.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[58].vehicle=2
        main_road2.lane[58].vehicle=2
        main_road3.lane[58].vehicle=2
        main_road4.lane[1686].vehicle=2
        main_road5.lane[1686].vehicle=2
        main_road6.lane[1686].vehicle=2
    elif(x==3):
        r4.lane[18].vehicle=0
        r5.lane[18].vehicle=0
    elif(x==4):
        r4.lane[11].vehicle=0
        r5.lane[11].vehicle=0
    elif(x==5):
        r4.lane[11].vehicle=2
        r5.lane[11].vehicle=2
        
def traffic_ligths3(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[74].vehicle=0
        main_road2.lane[74].vehicle=0
        main_road3.lane[74].vehicle=0
        main_road4.lane[1671].vehicle=0
        main_road5.lane[1671].vehicle=0
        main_road6.lane[1671].vehicle=0
        r6.lane[18].vehicle=2
        r7.lane[18].vehicle=2
        r8.lane[11].vehicle=2
        r9.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[74].vehicle=2
        main_road2.lane[74].vehicle=2
        main_road3.lane[74].vehicle=2
        main_road4.lane[1671].vehicle=2
        main_road5.lane[1671].vehicle=2
        main_road6.lane[1671].vehicle=2
    elif(x==3):
        r6.lane[18].vehicle=0
        r7.lane[18].vehicle=0
    elif(x==4):
        r8.lane[11].vehicle=0
        r9.lane[11].vehicle=0
    elif(x==5):
        r6.lane[11].vehicle=2
        r7.lane[11].vehicle=2
        
def traffic_ligths4(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[100].vehicle=0
        main_road2.lane[100].vehicle=0
        main_road3.lane[100].vehicle=0
        main_road4.lane[1652].vehicle=0
        main_road5.lane[1652].vehicle=0
        main_road6.lane[1652].vehicle=0
        r12.lane[11].vehicle=2
        r13.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[100].vehicle=2
        main_road2.lane[100].vehicle=2
        main_road3.lane[100].vehicle=2
        main_road4.lane[1652].vehicle=2
        main_road5.lane[1652].vehicle=2
        main_road6.lane[1652].vehicle=2
    elif(x==3):
        r12.lane[11].vehicle=0
        r13.lane[11].vehicle=0
    elif(x==4):
        r12.lane[11].vehicle=0
        r13.lane[11].vehicle=0
    elif(x==5):
        r12.lane[11].vehicle=2
        r13.lane[11].vehicle=2
        
def traffic_ligths5(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[100].vehicle=0
        main_road2.lane[100].vehicle=0
        main_road3.lane[100].vehicle=0
        main_road4.lane[1652].vehicle=0
        main_road5.lane[1652].vehicle=0
        main_road6.lane[1652].vehicle=0
        r12.lane[11].vehicle=2
        r13.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[100].vehicle=2
        main_road2.lane[100].vehicle=2
        main_road3.lane[100].vehicle=2
        main_road4.lane[1652].vehicle=2
        main_road5.lane[1652].vehicle=2
        main_road6.lane[1652].vehicle=2
    elif(x==3):
        r12.lane[11].vehicle=0
        r13.lane[11].vehicle=0
    elif(x==4):
        r12.lane[11].vehicle=0
        r13.lane[11].vehicle=0
    elif(x==5):
        r12.lane[11].vehicle=2
        r13.lane[11].vehicle=2
        
def traffic_ligths6(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[372].vehicle=0
        main_road2.lane[372].vehicle=0
        main_road3.lane[372].vehicle=0
        main_road4.lane[1397].vehicle=0
        main_road5.lane[1397].vehicle=0
        main_road6.lane[1397].vehicle=0
        r35.lane[11].vehicle=2
        r36.lane[18].vehicle=2
    elif(x==2):
        main_road1.lane[372].vehicle=2
        main_road2.lane[372].vehicle=2
        main_road3.lane[372].vehicle=2
        main_road4.lane[1397].vehicle=2
        main_road5.lane[1397].vehicle=2
        main_road6.lane[1397].vehicle=2
    elif(x==3):
        r35.lane[11].vehicle=0
        r36.lane[18].vehicle=0
    elif(x==4):
        r35.lane[11].vehicle=0
        r36.lane[18].vehicle=0
    elif(x==5):
        r35.lane[11].vehicle=2
        r36.lane[18].vehicle=2
    
def traffic_ligths7(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[450].vehicle=0
        main_road2.lane[450].vehicle=0
        main_road3.lane[450].vehicle=0
        main_road4.lane[1310].vehicle=0
        main_road5.lane[1310].vehicle=0
        main_road6.lane[1310].vehicle=0
        r46.lane[11].vehicle=2
        r47.lane[11].vehicle=2
        r42.lane[11].vehicle=2
        r43.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[450].vehicle=2
        main_road2.lane[450].vehicle=2
        main_road3.lane[450].vehicle=2
        main_road4.lane[1310].vehicle=2
        main_road5.lane[1310].vehicle=2
        main_road6.lane[1310].vehicle=2
    elif(x==3):
        r46.lane[11].vehicle=0
        r47.lane[11].vehicle=0
    elif(x==4):
        r42.lane[11].vehicle=2
        r43.lane[11].vehicle=2
    elif(x==5):
        r46.lane[11].vehicle=2
        r47.lane[11].vehicle=2
        
def traffic_ligths8(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[562].vehicle=0
        main_road2.lane[562].vehicle=0
        main_road3.lane[562].vehicle=0
        main_road4.lane[1180].vehicle=0
        main_road5.lane[1180].vehicle=0
        main_road6.lane[1180].vehicle=0
        
        r56.lane[11].vehicle=2
        r57.lane[11].vehicle=2
        r58.lane[11].vehicle=2
        
        r59.lane[11].vehicle=2
        r60.lane[11].vehicle=2
        r61.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[562].vehicle=2
        main_road2.lane[562].vehicle=2
        main_road3.lane[562].vehicle=2
        main_road4.lane[1180].vehicle=2
        main_road5.lane[1180].vehicle=2
        main_road6.lane[1180].vehicle=2
    elif(x==3):
        r56.lane[11].vehicle=0
        r57.lane[11].vehicle=0
        r58.lane[11].vehicle=0
    elif(x==4):
        r59.lane[11].vehicle=0
        r60.lane[11].vehicle=0
        r61.lane[11].vehicle=0
    elif(x==5):
        #r46.lane[11].vehicle=2
        #r47.lane[11].vehicle=2
        r61.lane[11].vehicle=0

def traffic_ligths9(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[744].vehicle=0
        main_road2.lane[744].vehicle=0
        main_road3.lane[744].vehicle=0
        main_road4.lane[1036].vehicle=0
        main_road5.lane[1036].vehicle=0
        main_road6.lane[1036].vehicle=0
        r71.lane[11].vehicle=2
        r72.lane[11].vehicle=2
        r69.lane[11].vehicle=2
        r70.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[744].vehicle=2
        main_road2.lane[744].vehicle=2
        main_road3.lane[744].vehicle=2
        main_road4.lane[1036].vehicle=2
        main_road5.lane[1036].vehicle=2
        main_road6.lane[1036].vehicle=2
    elif(x==3):
        r71.lane[11].vehicle=0
        r72.lane[11].vehicle=0
    elif(x==4):
        r69.lane[11].vehicle=0
        r70.lane[11].vehicle=0
    elif(x==5):
        r71.lane[11].vehicle=2
        r72.lane[11].vehicle=2
        
def traffic_ligths10(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[871].vehicle=2
        main_road2.lane[871].vehicle=2
        main_road3.lane[871].vehicle=2
        r73.lane[11].vehicle = 0
        r74.lane[11].vehicle = 0
        main_road4.lane[950].vehicle=0
        main_road5.lane[950].vehicle=0
        main_road6.lane[950].vehicle=0
        r78.lane[11].vehicle=2
        r75.lane[11].vehicle=2
        r76.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[871].vehicle=0
        main_road2.lane[871].vehicle=0
        main_road3.lane[871].vehicle=0
        main_road4.lane[950].vehicle=2
        main_road5.lane[950].vehicle=2
        main_road6.lane[950].vehicle=2
    elif(x==3):
        r78.lane[11].vehicle=0
    elif(x==4):
        r75.lane[11].vehicle=0
        r76.lane[11].vehicle=0
    elif(x==5):
        r71.lane[11].vehicle=2
        r72.lane[11].vehicle=2
        
def traffic_ligths11(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[932].vehicle=0
        main_road2.lane[932].vehicle=0
        main_road3.lane[932].vehicle=0
        r92.lane[11].vehicle=2
        r93.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[871].vehicle=0
        main_road2.lane[871].vehicle=0
        main_road3.lane[871].vehicle=0
    elif(x==3):
        main_road1.lane[871].vehicle=2
        main_road2.lane[871].vehicle=2
        main_road3.lane[871].vehicle=2
        r92.lane[11].vehicle=0
        r93.lane[11].vehicle=0
    elif(x==4):
        main_road1.lane[871].vehicle=0
        main_road2.lane[871].vehicle=0
        main_road3.lane[871].vehicle=0
        r92.lane[11].vehicle=2
        r93.lane[11].vehicle=2
    elif(x==5):
        r92.lane[11].vehicle=2
        r93.lane[11].vehicle=2
        
def traffic_ligths12(x): #sekwencja swiatel
    if(x==1):
        main_road4.lane[622].vehicle=0
        main_road5.lane[622].vehicle=0
        main_road6.lane[622].vehicle=0
    elif(x==2):
        main_road4.lane[622].vehicle=0
        main_road5.lane[622].vehicle=0
        main_road6.lane[622].vehicle=0
    elif(x==3):
        main_road4.lane[622].vehicle=2
        main_road5.lane[622].vehicle=2
        main_road6.lane[622].vehicle=2
    elif(x==4):
        main_road4.lane[622].vehicle=0
        main_road5.lane[622].vehicle=0
        main_road6.lane[622].vehicle=0
    elif(x==5):
        main_road4.lane[622].vehicle=0
        main_road5.lane[622].vehicle=0
        main_road6.lane[622].vehicle=0

def traffic_ligths13(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1162].vehicle=0
        main_road2.lane[1162].vehicle=0
        main_road3.lane[1162].vehicle=0
        main_road4.lane[551].vehicle=0
        main_road5.lane[551].vehicle=0
        main_road6.lane[551].vehicle=0
        r107.lane[11].vehicle=2
        r108.lane[11].vehicle=2
        r109.lane[11].vehicle=2
        r110.lane[11].vehicle=2
        r111.lane[11].vehicle=2
        r112.lane[11].vehicle=2    
    elif(x==3):
        main_road1.lane[1162].vehicle=2
        main_road2.lane[1162].vehicle=2
        main_road3.lane[1162].vehicle=2
        main_road4.lane[551].vehicle=2
        main_road5.lane[551].vehicle=2
        main_road6.lane[551].vehicle=2
        r107.lane[11].vehicle=0
        r108.lane[11].vehicle=0
        r109.lane[11].vehicle=0
        r110.lane[11].vehicle=0
        r111.lane[11].vehicle=0
        r112.lane[11].vehicle=0    
    elif(x==5):
        main_road1.lane[1162].vehicle=0
        main_road2.lane[1162].vehicle=0
        main_road3.lane[1162].vehicle=0
        main_road4.lane[551].vehicle=0
        main_road5.lane[551].vehicle=0
        main_road6.lane[551].vehicle=0
        r107.lane[11].vehicle=2
        r108.lane[11].vehicle=2
        r109.lane[11].vehicle=2
        r110.lane[11].vehicle=2
        r111.lane[11].vehicle=2
        r112.lane[11].vehicle=2

def traffic_ligths14(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1461].vehicle=0
        main_road2.lane[1461].vehicle=0
        main_road3.lane[1461].vehicle=0
        main_road4.lane[245].vehicle=0
        main_road5.lane[245].vehicle=0
        main_road6.lane[245].vehicle=0
        r136.lane[11].vehicle=2
        r138.lane[11].vehicle=2
        r134.lane[11].vehicle=2
        r133.lane[11].vehicle=2
    elif(x==3):
        main_road1.lane[1461].vehicle=2
        main_road2.lane[1461].vehicle=2
        main_road3.lane[1461].vehicle=2
        main_road4.lane[245].vehicle=2
        main_road5.lane[245].vehicle=2
        main_road6.lane[245].vehicle=2
        r136.lane[11].vehicle=0
        r138.lane[11].vehicle=0
        r134.lane[11].vehicle=0
        r133.lane[11].vehicle=0    
    elif(x==5):
        main_road1.lane[1461].vehicle=0
        main_road2.lane[1461].vehicle=0
        main_road3.lane[1461].vehicle=0
        main_road4.lane[245].vehicle=0
        main_road5.lane[245].vehicle=0
        main_road6.lane[245].vehicle=0
        r136.lane[11].vehicle=2
        r138.lane[11].vehicle=2
        r134.lane[11].vehicle=2
        r133.lane[11].vehicle=2

def traffic_ligths15(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1523].vehicle=0
        main_road2.lane[1523].vehicle=0
        main_road3.lane[1523].vehicle=0
        main_road4.lane[181].vehicle=0
        main_road5.lane[181].vehicle=0
        main_road6.lane[181].vehicle=0
        r139.lane[11].vehicle=2
        r140.lane[11].vehicle=2
    elif(x==3):
        main_road1.lane[1523].vehicle=2
        main_road2.lane[1523].vehicle=2
        main_road3.lane[1523].vehicle=2
        main_road4.lane[181].vehicle=2
        main_road5.lane[181].vehicle=2
        main_road6.lane[181].vehicle=2
        r139.lane[11].vehicle=0
        r140.lane[11].vehicle=0  
    elif(x==5):
        main_road1.lane[1523].vehicle=0
        main_road2.lane[1523].vehicle=0
        main_road3.lane[1523].vehicle=0
        main_road4.lane[181].vehicle=0
        main_road5.lane[181].vehicle=0
        main_road6.lane[181].vehicle=0
        r139.lane[11].vehicle=2
        r140.lane[11].vehicle=2

def traffic_ligths16(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1599].vehicle=0
        main_road2.lane[1599].vehicle=0
        main_road3.lane[1599].vehicle=0
        main_road4.lane[119].vehicle=0
        main_road5.lane[119].vehicle=0
        main_road6.lane[119].vehicle=0
        r145.lane[11].vehicle=2
        r146.lane[11].vehicle=2
    elif(x==3):
        main_road1.lane[1599].vehicle=2
        main_road2.lane[1599].vehicle=2
        main_road3.lane[1599].vehicle=2
        main_road4.lane[119].vehicle=2
        main_road5.lane[119].vehicle=2
        main_road6.lane[119].vehicle=2
        r145.lane[11].vehicle=0
        r146.lane[11].vehicle=0  
    elif(x==5):
        main_road1.lane[1599].vehicle=0
        main_road2.lane[1599].vehicle=0
        main_road3.lane[1599].vehicle=0
        main_road4.lane[119].vehicle=0
        main_road5.lane[119].vehicle=0
        main_road6.lane[119].vehicle=0
        r145.lane[11].vehicle=2
        r146.lane[11].vehicle=2

def traffic_ligths17(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1635].vehicle=0
        main_road2.lane[1635].vehicle=0
        main_road3.lane[1635].vehicle=0
        main_road4.lane[94].vehicle=0
        main_road5.lane[94].vehicle=0
        main_road6.lane[94].vehicle=0
        r151.lane[11].vehicle=2
        r152.lane[11].vehicle=2
        r150.lane[11].vehicle=2
        r148.lane[11].vehicle=2
        r149.lane[11].vehicle=2
    elif(x==3):
        main_road1.lane[1635].vehicle=2
        main_road2.lane[1635].vehicle=2
        main_road3.lane[1635].vehicle=2
        main_road4.lane[94].vehicle=2
        main_road5.lane[94].vehicle=2
        main_road6.lane[94].vehicle=2
        r151.lane[11].vehicle=0
        r152.lane[11].vehicle=0
        r150.lane[11].vehicle=0
        r148.lane[11].vehicle=0
        r149.lane[11].vehicle=0  
    elif(x==5):
        main_road1.lane[1635].vehicle=0
        main_road2.lane[1635].vehicle=0
        main_road3.lane[1635].vehicle=0
        main_road4.lane[94].vehicle=0
        main_road5.lane[94].vehicle=0
        main_road6.lane[94].vehicle=0
        r151.lane[11].vehicle=2
        r152.lane[11].vehicle=2
        r150.lane[11].vehicle=2
        r148.lane[11].vehicle=2
        r149.lane[11].vehicle=2

def traffic_ligths18(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[1716].vehicle=0
        main_road2.lane[1716].vehicle=0
        main_road3.lane[1716].vehicle=0
        main_road4.lane[4].vehicle=0
        main_road5.lane[4].vehicle=0
        main_road6.lane[4].vehicle=0
        r163.lane[11].vehicle=2
        r164.lane[11].vehicle=2
        r162.lane[11].vehicle=2
        r161.lane[11].vehicle=2
    elif(x==3):
        main_road1.lane[1716].vehicle=2
        main_road2.lane[1716].vehicle=2
        main_road3.lane[1716].vehicle=2
        main_road4.lane[4].vehicle=2
        main_road5.lane[4].vehicle=2
        main_road6.lane[4].vehicle=2
        r163.lane[11].vehicle=0
        r164.lane[11].vehicle=0
        r162.lane[11].vehicle=0
        r161.lane[11].vehicle=0  
    elif(x==5):
        main_road1.lane[1716].vehicle=0
        main_road2.lane[1716].vehicle=0
        main_road3.lane[1716].vehicle=0
        main_road4.lane[4].vehicle=0
        main_road5.lane[4].vehicle=0
        main_road6.lane[4].vehicle=0
        r163.lane[11].vehicle=2
        r164.lane[11].vehicle=2
        r162.lane[11].vehicle=2
        r161.lane[11].vehicle=2

def add_none_to_other_roads(roads_list):
    if(main_road1 not in roads_list):
        main_road1.other_roads.append(None)
    if(main_road2 not in roads_list):
        main_road2.other_roads.append(None)
    if(main_road3 not in roads_list):
        main_road3.other_roads.append(None)
    if(main_road4 not in roads_list):
        main_road4.other_roads.append(None)
    if(main_road5 not in roads_list):
        main_road5.other_roads.append(None)
    if(main_road6 not in roads_list):
        main_road6.other_roads.append(None)
 
       
def road_creator(roads_list ,roads_param , crossing_list , template , space_between_roads=0):
    road = []
    len_roads=12
    
    if(template == 1): #wjazd
        param = [len_roads]
        road = [Cell(0) for i in range(len_roads+1)] #+1 bo wjazd
        road=Road(road)
        
        (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
        road.lane[param[0]]=Cell(0,True,1,roads_param[0])
        roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
    
    elif(template == 2): #wyjazd
        param = [0]
        road = [Cell(0) for i in range(len_roads+1)] #+1 bo wyjazd
        road=Road(road)
        
        (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
        road.lane[param[0]]=Cell(0,True,1,roads_param[0])
        roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
        
        #destination
        if(roads_list[0] in [main_road2,main_road3]):
            bottom_destinations_ins.append(crossing_list[0])
        
        elif(roads_list[0] in [main_road4,main_road5]):
            bottom_destinations_out.append(crossing_list[0])
            
    elif(template == 3): #pelna droga
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1,len_roads+2+space_between_roads+2,len_roads+2+space_between_roads+3]
        road = [Cell(0) for i in range(len_roads*2+space_between_roads+6)] #pelna droga
        road = Road(road)
        
        (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
        road.lane[param[0]]=Cell(0,True,1,roads_param[0])
        roads_list[0].other_roads.append(road)
            
        (roads_list[1]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[1])
        road.lane[param[1]]=Cell(0,True,2,roads_param[0])
        roads_list[1].other_roads.append(road)
            
        (roads_list[2]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[2])
        road.lane[param[2]]=Cell(0,True,3,roads_param[0])
        roads_list[2].other_roads.append(road)

        (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[3])
        road.lane[param[3]]=Cell(0,True,4,roads_param[1])
        roads_list[3].other_roads.append(road)
            
        (roads_list[4]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[4])
        road.lane[param[4]]=Cell(0,True,5,roads_param[1])
        roads_list[4].other_roads.append(road)
            
        (roads_list[5]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[5])
        road.lane[param[5]]=Cell(0,True,6,roads_param[1])
        roads_list[5].other_roads.append(road)
        
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3],roads_list[4],roads_list[5]]
        
        #destination
        if(roads_list == [main_road4,main_road5,main_road6,main_road1,main_road2,main_road3]):
            bottom_destinations_ins.append(crossing_list[0])
            upper_destinations_out.append(crossing_list[0])
        
        elif(roads_list == [main_road3,main_road2,main_road1,main_road6,main_road5,main_road4]):
            upper_destinations_ins.append(crossing_list[0])
            bottom_destinations_out.append(crossing_list[0])
    
    elif(template == 4): #niepelna droga wjazdowa
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1]
        road = [Cell(0) for i in range(len_roads+space_between_roads+4)] #niepelna droga
        road = Road(road)
        
        (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
        road.lane[param[0]]=Cell(0,True,1,roads_param[0])
        roads_list[0].other_roads.append(road)
            
        (roads_list[1]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[1])
        road.lane[param[1]]=Cell(0,True,2,roads_param[0])
        roads_list[1].other_roads.append(road)
            
        (roads_list[2]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[2])
        road.lane[param[2]]=Cell(0,True,3,roads_param[0])
        roads_list[2].other_roads.append(road)
            
        (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[3])
        road.lane[param[3]]=Cell(0,True,4,roads_param[1])
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
            (roads_list[1]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[1])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[1])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[0],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[1])
            roads_list[3].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3]]
        
        #destination
        if(roads_list == [main_road1,main_road6,main_road5,main_road4] ):
            upper_destinations_ins.append(crossing_list[0])
            bottom_destinations_out.append(crossing_list[0])
        
        elif(roads_list == [main_road6,main_road1,main_road2,main_road3]):
            bottom_destinations_ins.append(crossing_list[0])
            upper_destinations_out.append(crossing_list[0])
                    
    return road
    

###representing roads###
#mainroads 1-3 destinations 

bottom_destinations_ins = [] 
upper_destinations_ins  = []
  
#mainroads 4-6 destinations
bottom_destinations_out = []
upper_destinations_out  = []    

#mainroads
main_road4 = []
main_road5 = [Cell(0) for i in range(1750)]
main_road6 = [Cell(0) for i in range(1750)]

for i in range(440):
    main_road4.append(Cell(0))

for i in range(230):
    main_road4.append(Cell(3))
    
for i in range(248):
    main_road4.append(Cell(0))

for i in range(262):
    main_road4.append(Cell(3)) 
    
for i in range(174):
    main_road4.append(Cell(0))

for i in range(254):
    main_road4.append(Cell(3)) 
  
for i in range(142):
    main_road4.append(Cell(0))

main_road1 = [Cell(0) for i in range(1725)]
main_road2 = [Cell(0) for i in range(1725)]
main_road3 = []

for i in range(145):
    main_road3.append(Cell(0))

for i in range(282):
    main_road3.append(Cell(3))
    
for i in range(156):
    main_road3.append(Cell(0))

for i in range(272):
    main_road3.append(Cell(3)) 
    
for i in range(232):
    main_road3.append(Cell(0))

for i in range(186):
    main_road3.append(Cell(3)) 
  
for i in range(452):
    main_road3.append(Cell(0))
    
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
#--

z_gory         = [main_road4,main_road5,main_road6,main_road1,main_road2,main_road3]
z_dolu         = [main_road3,main_road2,main_road1,main_road6,main_road5,main_road4]
wjazd_z_gory   = [main_road4,main_road5,main_road6,main_road1]
wjazd_z_dolu   = [main_road3,main_road2,main_road1,main_road6]
zjazd_do_gory  = [main_road1,main_road6,main_road5,main_road4] 
zjazd_do_dolu  = [main_road6,main_road1,main_road2,main_road3]

#other roads
# 3 lanes  
r1   = road_creator(z_gory       ,[1723,24]  ,[1],3,4)
r2   = road_creator(z_dolu       ,[25,1722]  ,[2],3,4)
r3   = road_creator([main_road3] ,[42]       ,[3],1)
r4   = road_creator(z_gory       ,[1688,59]  ,[4],3,4)
r5   = road_creator(zjazd_do_gory,[60,1687]  ,[5],5,4)
r6   = road_creator(z_gory       ,[1674,73]  ,[6],3,4)
r7   = road_creator(wjazd_z_gory ,[1673,74]  ,[7],4,4)
r8   = road_creator(z_dolu       ,[75,1672]  ,[8],3,4)
r9   = road_creator([main_road3] ,[76]       ,[9],1)
r10  = road_creator([main_road4] ,[1667]     ,[10],2)
r11  = road_creator([main_road4] ,[1660]     ,[11],2)
r12  = road_creator([main_road4] ,[1656]     ,[12],1)
r13  = road_creator(wjazd_z_gory ,[1655,102] ,[13],4)
r14  = road_creator(zjazd_do_gory,[104,1654] ,[14],5)
r15  = road_creator([main_road4] ,[1653]     ,[15],2,1)
r16  = road_creator([main_road4] ,[1616]     ,[16],1)
r17  = road_creator([main_road4] ,[1615]     ,[17],1)
r18  = road_creator([main_road3] ,[142]      ,[18],2)

# 2 lanes
r19  = road_creator([main_road5] ,[1601]     ,[19],2)
r20  = road_creator([main_road2] ,[168]      ,[20],1)
r21  = road_creator([main_road5] ,[1564]     ,[21],1)
r22  = road_creator([main_road5] ,[1562]     ,[22],2)
r23  = road_creator([main_road2] ,[168]      ,[23],2)
r24  = road_creator([main_road2] ,[168]      ,[24],2)
r25  = road_creator([main_road5] ,[1551]     ,[25],1)
r26  = road_creator([main_road5] ,[1550]     ,[26],1)
r27  = road_creator([main_road1] ,[218]      ,[27],1)
r28  = road_creator([main_road2] ,[219]      ,[28],1)
r29  = road_creator([main_road5] ,[1496]     ,[29],2)
r30  = road_creator([main_road5] ,[1482]     ,[30],1)
r31  = road_creator([main_road2] ,[187]      ,[31],2)
r32  = road_creator([main_road2] ,[371]      ,[32],1)
r33  = road_creator([main_road5] ,[1402]     ,[33],2)
r34  = road_creator([main_road2] ,[372]      ,[34],2)
r35  = road_creator(wjazd_z_gory ,[1399,375] ,[35],4)
r36  = road_creator(z_dolu       ,[376,1398] ,[36],3)  
r37  = road_creator([main_road5] ,[1397]     ,[37],2)
r38  = road_creator([main_road2] ,[388]      ,[38],2)
r39  = road_creator([main_road5] ,[1378]     ,[39],1)
r40  = road_creator([main_road5] ,[1377]     ,[40],2)
r41  = road_creator([main_road2] ,[425]      ,[41],1)

# 3 lanes
r42  = road_creator(wjazd_z_gory ,[1344,436] ,[42],4,4)
r43  = road_creator(wjazd_z_gory ,[1343,437] ,[43],4,4)
r44  = road_creator([main_road4] ,[1341]     ,[44],2)
r45  = road_creator([main_road4] ,[1340]     ,[45],2)
r46  = road_creator([main_road4] ,[1331]     ,[46],1)
r47  = road_creator([main_road4] ,[1330]     ,[47],1)
r48  = road_creator([main_road4] ,[1325]     ,[48],2)
r49  = road_creator([main_road4] ,[1324]     ,[49],2)
r50  = road_creator([main_road3] ,[448]      ,[50],2)
r51  = road_creator(wjazd_z_dolu ,[455,1312] ,[51],4,4)
r52  = road_creator(wjazd_z_dolu ,[456,1311] ,[52],4,4)
r53  = road_creator([main_road4] ,[1267]     ,[53],1)
r54  = road_creator([main_road4] ,[1266]     ,[54],2)
r55  = road_creator([main_road3] ,[530]      ,[55],1)
r56  = road_creator([main_road4] ,[1205]     ,[56],1)
r57  = road_creator(z_gory       ,[1204,565] ,[57],3,4)
r58  = road_creator(z_gory       ,[1203,566] ,[58],3,4)
r59  = road_creator(z_dolu       ,[573,1196] ,[59],3,4)
r60  = road_creator(z_dolu       ,[574,1195] ,[60],3,4)
r61  = road_creator([main_road3] ,[575]      ,[61],1)

# 2 lanes
r62  = road_creator([main_road5] ,[1177]     ,[62],2)
r63  = road_creator([main_road5] ,[1157]     ,[63],1)
r64  = road_creator([main_road2] ,[618]      ,[64],2)
r65  = road_creator([main_road2] ,[677]      ,[65],2)
r66  = road_creator([main_road2] ,[688]      ,[66],1)
r67  = road_creator([main_road5] ,[1097]     ,[67],2)
r68  = road_creator([main_road5] ,[1086]     ,[68],1)
r69  = road_creator(z_gory       ,[1036,744] ,[69],3)
r70  = road_creator(wjazd_z_gory ,[1035,745] ,[70],4)
r71  = road_creator(wjazd_z_dolu ,[745,1034] ,[71],4)
r72  = road_creator(z_dolu       ,[746,1033] ,[72],3)
r73  = road_creator(zjazd_do_gory,[811,955]  ,[73],5,4)
r74  = road_creator(zjazd_do_gory,[812,956]  ,[74],5,4)
r75  = road_creator(wjazd_z_gory ,[966,815]  ,[75],4,4)
r76  = road_creator(wjazd_z_gory ,[965,816]  ,[76],4,4)
r77  = road_creator([main_road5] ,[961]      ,[77],2)
r78  = road_creator([main_road5] ,[960]      ,[78],1)
r79  = road_creator([main_road2] ,[832]      ,[79],2)
r80  = road_creator([main_road2] ,[833]      ,[80],1)
r81  = road_creator([main_road5] ,[939]      ,[81],2)
r82  = road_creator([main_road5] ,[938]      ,[82],1)
r83  = road_creator([main_road2] ,[840]      ,[83],2)
r84  = road_creator([main_road2] ,[851]      ,[84],2)
r85  = road_creator([main_road2] ,[852]      ,[85],1)

# 3 lanes
r86  = road_creator([main_road3] ,[861]      ,[86],2)
r87  = road_creator([main_road3] ,[871]      ,[87],1)
r88  = road_creator([main_road3] ,[904]      ,[88],1)
r89  = road_creator([main_road3] ,[905]      ,[89],1)
r90  = road_creator([main_road4] ,[871]      ,[90],2)
r91  = road_creator([main_road3] ,[919]      ,[91],2)
r92  = road_creator(z_gory       ,[841,933]  ,[92],3)
r93  = road_creator(z_dolu       ,[934,840]  ,[93],3)

# 2 lanes
r94  = road_creator([main_road2] ,[1084]     ,[94],2)
r95  = road_creator([main_road2] ,[1085]     ,[95],2)
r96  = road_creator([main_road2] ,[1091]     ,[96],1)
r97  = road_creator([main_road2] ,[1092]     ,[97],2)
r98  = road_creator([main_road2] ,[1100]     ,[98],1)
r99  = road_creator([main_road2] ,[1101]     ,[99],2)
r100 = road_creator([main_road5] ,[666]      ,[100],1)
r101 = road_creator([main_road5] ,[622]      ,[101],1)
r102 = road_creator([main_road5] ,[623]      ,[102],1)
r103 = road_creator([main_road5] ,[594]      ,[103],2)
r104 = road_creator([main_road5] ,[595]      ,[104],2)
r105 = road_creator([main_road2] ,[1148]     ,[105],2)
r106 = road_creator([main_road2] ,[1149]     ,[106],1)
r107 = road_creator([main_road5] ,[552]      ,[107],1)
r108 = road_creator(z_gory       ,[551,1164] ,[108],3,4)
r109 = road_creator(z_gory       ,[550,1165] ,[109],3,4)
r110 = road_creator(z_dolu       ,[1170,549] ,[110],3,4)
r111 = road_creator(z_dolu       ,[1171,548] ,[111],3,4)
r112 = road_creator([main_road2] ,[1171]     ,[112],1)
r113 = road_creator([main_road2] ,[1224]     ,[113],2)
r114 = road_creator([main_road2] ,[1234]     ,[114],2)
r115 = road_creator([main_road2] ,[1235]     ,[115],1)
r116 = road_creator([main_road2] ,[1268]     ,[116],2)
r117 = road_creator([main_road2] ,[1273]     ,[117],1)

# 3 lanes
r118 = road_creator([main_road3] ,[1309]     ,[118],2)
r119 = road_creator([main_road3] ,[1313]     ,[119],1)
r120 = road_creator([main_road4] ,[404]      ,[120],1)
r121 = road_creator([main_road4] ,[400]      ,[121],2)
r122 = road_creator([main_road3] ,[1333]     ,[122],2)
r123 = road_creator([main_road3] ,[1334]     ,[123],2)
r124 = road_creator([main_road4] ,[377]      ,[124],1)
r125 = road_creator([main_road4] ,[378]      ,[125],1)
r126 = road_creator([main_road3] ,[1386]     ,[126],1)
r127 = road_creator([main_road3] ,[1387]     ,[127],1)
r128 = road_creator([main_road4] ,[321]      ,[128],2)
r129 = road_creator([main_road4] ,[322]      ,[129],2)
r130 = road_creator([main_road3] ,[1408]     ,[130],1)
r131 = road_creator([main_road3] ,[1409]     ,[131],2)
r132 = road_creator([main_road4] ,[280]      ,[132],2)
r133 = road_creator([main_road4] ,[249]      ,[133],1)
r134 = road_creator(z_gory       ,[248,1463] ,[134],3)
r135 = road_creator(z_dolu       ,[1464,247] ,[135],3)
r136 = road_creator([main_road3] ,[1465]     ,[136],1)
r137 = road_creator([main_road4] ,[201]      ,[137],1)
r138 = road_creator([main_road4] ,[200]      ,[138],2)
r139 = road_creator(z_gory       ,[183,1528] ,[139],3,4)
r140 = road_creator(z_dolu       ,[1529,182] ,[140],3,4)
r141 = road_creator([main_road3] ,[1575]     ,[141],2)
r142 = road_creator([main_road3] ,[1574]     ,[142],1)
r143 = road_creator([main_road4] ,[142]      ,[143],1)
r144 = road_creator([main_road4] ,[141]      ,[144],2)
r145 = road_creator([main_road4] ,[118]      ,[145],1)
r146 = road_creator(wjazd_z_gory ,[117,1597] ,[146],4,4)
r147 = road_creator(zjazd_do_gory,[1598,116] ,[147],5,4)
r148 = road_creator([main_road4] ,[99]       ,[148],1)
r149 = road_creator([main_road4] ,[98]       ,[149],1)
r150 = road_creator(z_gory       ,[97,1627]  ,[150],3,4)
r151 = road_creator(z_dolu       ,[1628,96]  ,[151],3,4)
r152 = road_creator(z_dolu       ,[1629,95]  ,[152],3,4)
r153 = road_creator([main_road4] ,[94]       ,[153],2)
r154 = road_creator([main_road3] ,[1646]     ,[154],1)
r155 = road_creator([main_road4] ,[45]       ,[155],1)
r156 = road_creator(z_gory       ,[44,1676]  ,[156],3,4)
r157 = road_creator(z_dolu       ,[1677,43]  ,[157],3,4)
r158 = road_creator(zjazd_do_gory,[1697,25]  ,[158],5,4)
r159 = road_creator([main_road4] ,[26]       ,[159],1)
r160 = road_creator([main_road4] ,[24]       ,[160],2)
r161 = road_creator(z_gory       ,[8,1717]   ,[161],3,4)
r162 = road_creator(wjazd_z_gory ,[7,1718]   ,[162],4,4)
r163 = road_creator(z_dolu       ,[1719,6]   ,[163],3,4)
r164 = road_creator([main_road3] ,[1720]     ,[164],1)