import road as r
import random

class Vehicle(object):
    def __init__(self,velocity,road,position):
        self.velocity=velocity
        self.road=road
        self.position=position
        self.road.lane[self.position].vehicle=1
        
    def update_cell(self,x):
        self.road.lane[self.position].vehicle=x
    
    def get_speed_limit(self):
        return self.road.lane[self.position].speed_limit
    
    def check_collision(self,distance):
        if(self.position+distance >= len(self.road.lane)): #out of road
            return False
        
        return self.road.lane[self.position+distance].vehicle>0
    
    def check_crossing(self,distance):
        if(self.road.lane[self.position+distance].crossing_id!=None): #czyli jest jakies skrzyzowanie drog
            return [self.road.other_roads[self.road.lane[self.position+distance].crossing_id-1],self.road.lane[self.position+distance].index] #zwracam droge ktora sie krzyzuje i pozycje w niej tego miejsca
        return None
        
 
def add_vehicle():
    case=random.randint(0,8)
    
    #dodaj samochod do losowej drogi
    if(case == 0 and r.r1.lane[0].vehicle==0): 
        vehicles.append(Vehicle(0,r.r1,0))  
    elif(case == 1 and r.main_road1.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road1,0))  
    elif(case == 2 and r.main_road2.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road2,0)) 
    elif(case == 3 and r.main_road3.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road3,0))
    elif(case == 4 and r.main_road4.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road4,0))  
    elif(case == 5 and r.main_road5.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road5,0)) 
    elif(case == 6 and r.main_road6.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.main_road6,0))
    elif(case == 7 and r.r1.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.r2,0))
    elif(case == 8 and r.r3.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.r3,0))

            
vehicles=[] #list of vehicles that are on road
vehicles.append(Vehicle(4,r.main_road1,2)) #dodanie pojazdu do road1 na miejscu 0 z predkoscia poczatkowa 0
vehicles.append(Vehicle(0,r.main_road1,7))
vehicles.append(Vehicle(0,r.main_road3,0))

vehicles.append(Vehicle(0,r.r1,0)) # z gory
vehicles.append(Vehicle(0,r.r1,1))