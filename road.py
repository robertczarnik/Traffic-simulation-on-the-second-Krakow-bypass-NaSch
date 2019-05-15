import time
import random

clear = lambda: print('\n' * 55)

class Road(object):
    def __init__(self,lane,l_road=None,p_road=None,other_roads=None):
        self.lane=lane
        self.l_road=l_road
        self.p_road=p_road
        self.other_roads=other_roads #roads that cross this road
               
    def print_road(self):
        for i in range(len(self.lane)):
            print(self.lane[i].vehicle,end=' ')
        print('')


class Cell(object):
    def __init__(self,vehicle,crossroads=False,crossing_id=None,index=None):
        self.vehicle=vehicle
        self.crossroads=crossroads
        self.crossing_id=crossing_id
        self.index=index
        self.speed_limit=4 
       
        
class Vehicle(object):
    def __init__(self,velocity,road,position):
        self.velocity=velocity
        self.road=road
        self.position=position
        self.road.lane[self.position].vehicle=1
        
    def updateCell(self,x):
        self.road.lane[self.position].vehicle=x
    
    def get_speed_limit(self):
        return self.road.lane[self.position].speed_limit
    
    def check_collision(self,distance):
        if(self.position+distance >= len(self.road.lane)): #out of road
            return False
        
        return self.road.lane[self.position+distance].vehicle==1
        

#representing roads
road1_len=55
road2_len=22
road1 = [0] * road1_len
road2 = [0] * road2_len

for i in range(road1_len):
    road1[i]=Cell(0,False);
    
for i in range(road2_len):
    road2[i]=Cell(0,False);

road1[24]=Cell(0,True,1,6);
road2[6]=Cell(0,True,1,24);

road1 = Road(road1,False,False)
road2 = Road(road2,False,False)

road1.other_roads=[road2]
road2.other_roads=[road1]
#--



vehicles=[] #list of vehicles that are on road
vehicles.append(Vehicle(0,road1,0)) #dodanie pojazdu do road1 na miejscu 0 z predkoscia poczatkowa 0

clear()
road1.print_road()

for j in range(30): #mainloop
    vehicles_down=[]
    for i in range(len(vehicles)):
        if(vehicles[i].velocity < vehicles[i].get_speed_limit()): #acceleration
            vehicles[i].velocity+=1
            
        for k in range(1,vehicles[i].velocity+1): #braking
            if(vehicles[i].check_collision(k)):
                vehicles[i].velocity=k-1
                break
            
        if(random.randint(0, 9)<4): #Randomisation 40% chance to slow down
            vehicles[i].velocity-=1
            
        
        vehicles[i].updateCell(0)
        if( (vehicles[i].position+vehicles[i].velocity) >= len(vehicles[i].road.lane)):  #wyjechanie poza droge
            vehicles_down.append(i) #indeksy pojazdow ktore trzeba usunac
        else: #Driving
            vehicles[i].position+=vehicles[i].velocity
            vehicles[i].updateCell(1)
            
     
    for w in range(len(vehicles_down)): #usuwanie pojazdow ktore wyjechaly poza droge
        vehicles.pop(vehicles_down[w])
    
    if(road1.lane[0].vehicle==0): #dodaj samochod do drogi
        vehicles.append(Vehicle(0,road1,0))        
        
    time.sleep(1)

    clear()
    road1.print_road()
    


















    