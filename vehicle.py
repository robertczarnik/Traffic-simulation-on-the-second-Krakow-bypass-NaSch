import road as r
import random

class Vehicle(object):
    def __init__(self,velocity,road,position,destination):
        self.velocity=velocity
        self.road=road
        self.position=position
        self.destination=destination #list
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
    
def changing_road(vehicle,road):
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.velocity+1): #zeby nie wyleciec poza droge
        return False
        
    if(road.lane[pos].vehicle>0): #jest samochod na sasiednim pasie - nie da sie zmienic pasa
        return False
        
    for i in range(pos+1,pos+vehicle.road.lane[pos].speed_limit+1): # (gap_lookback,gap_ahead)
        if(road.lane[i].vehicle>0):
            return i-1 #predkosc z jaka moze zmienic pas
    
    return vehicle.road.lane[pos].speed_limit

    
def check_overtaking(vehicle,road):
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.velocity+1): #zeby nie wyleciec poza droge
        return False
        
    for i in range(pos- ( road.lane[pos].speed_limit-vehicle.velocity)  ,pos+vehicle.velocity+1): # (gap_lookback,gap_ahead)
        if(road.lane[i].vehicle>0): #sprawdzenie czy jest wolne miejsce zeby mozna bylo wyprzedzac
            return False
    return True
        
 
#bottom road
#destinations_bottom=[[1]]
def add_vehicle():
    case=random.randint(0,2)
    if(case == 0 and r.r1.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.r1,0,[4,4,False,'P','L']))  # oznaczenia L i P sa po to zeby samochod wiedzial na ktorym pasie sie ustawic, w odwrotnej kolejnosci niz numery skrzyzowan
    elif(case == 1 and r.r2.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.r2,0,[1,4,False,'P','P']))
    elif(case == 2 and r.r3.lane[0].vehicle==0):
        vehicles.append(Vehicle(0,r.r3,0,[1,4,False,'P','P']) )
    #dodaj samochod do losowej drogi
      
    #if(case == 0 and r.main_road1.lane[0].vehicle==0):
        #vehicles.append(Vehicle(0,r.main_road1,0,[]))  
    #elif(case == 1 and r.main_road2.lane[0].vehicle==0):
        #vehicles.append(Vehicle(0,r.main_road2,0,[])) 
    #elif(case == 2 and r.main_road3.lane[0].vehicle==0):
        #vehicles.append(Vehicle(0,r.main_road3,0,[]))
    #elif(case == 3 and r.r1.lane[0].vehicle==0): 
        #vehicles.append(Vehicle(0,r.r1,0,[]))
    #elif(case == 4 and r.r1.lane[0].vehicle==0):
        #vehicles.append(Vehicle(0,r.r2,0,[]))
    #elif(case == 5 and r.r3.lane[0].vehicle==0):
        #vehicles.append(Vehicle(0,r.r3,0,[]))

      
vehicles=[] #list of vehicles that are on road