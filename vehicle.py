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
    
    def check_collision(self,distance): #WYLOT
        pos=self.position+distance
        if(pos >= len(self.road.lane)): #zapetlnie drogi
            return False
        
        return self.road.lane[pos].vehicle>0
    
    def check_crossing(self,distance): #WYLOT
        pos=self.position+distance
        
        if(pos >= len(self.road.lane)): #zapetlnie drogi
            return None
            
        if(self.road.lane[pos].crossing_id!=None): #czyli jest jakies skrzyzowanie drog
            return [self.road.other_roads[self.road.lane[pos].crossing_id-1],self.road.lane[pos].index] #zwracam droge ktora sie krzyzuje i pozycje w niej tego miejsca
        
        return None
    
def changing_road(vehicle,road): #WYLOT nie takii koniecznyy
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.road.lane[pos].speed_limit+1): #zeby nie wyleciec poza droge
        return False
        
    if(road.lane[pos].vehicle>0): #jest samochod na sasiednim pasie - nie da sie zmienic pasa
        return False
        
    for i in range(pos+1,pos+vehicle.road.lane[pos].speed_limit+1): # (gap_lookback,gap_ahead)
        if(road.lane[i].vehicle>0):
            return i-1 #predkosc z jaka moze zmienic pas
    
    return vehicle.road.lane[pos].speed_limit

    
def check_overtaking(vehicle,road): #WYLOT
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.velocity+1): #zeby nie wyleciec poza droge
        return False
        
    for i in range(pos- ( road.lane[pos].speed_limit-vehicle.velocity)  ,pos+vehicle.velocity+1): # (gap_lookback,gap_ahead)
        if(road.lane[i].vehicle>0): #sprawdzenie czy jest wolne miejsce zeby mozna bylo wyprzedzac
            return False
    return True
        

#vehicles destinations
    
#down->down [1,nr,False,'P','P']
#down->up   [4,nr,False,'P','L'] #usually 4
#up->up     [1,nr,False,'P','P']
#up->down   [4,nr,False,'L','P'] #usually 4

#each road has its own propability to create a vehicle

low=10
medium=40
high=80    

mazowiecka=medium   #r1
krowoderska=medium  #r2
zulawskiego=low     #r3
slaska=medium       #r4
pradnicka1=medium   #r6
pradnicka2=low      #r7
dluga1=low          #r8
dluga2=low          #r9
kamienna1=low       #r12
kamienna2=low       #r13
aleja29listopada1=low #16
aleja29listopada2=low #17
aleja29listopada3=low #20


def vehicle_creator(road,freq,nr,reverse=False,only_entry=False,only_entry_other_side=False,forward=False,less=0):#chyba dziala XD
    #gdzie chce dojechac
    #i wtedy wybor czy przejechac na druga strone i czy to jest droga w gore czy w dol
    

    if(reverse):
        bottom=upper_destinations
        upper=bottom_destinations
    else:
        bottom=bottom_destinations
        upper=upper_destinations
        
        
    if(random.randint(0,99)<freq and road.lane[0].vehicle==0):
        
        if(forward==True):
            vehicles.append(Vehicle(0,road,0,[False]))
            return
        
        if((random.randint(0,1) or only_entry) and not only_entry_other_side): #przejazd dolem
            if(random.randint(0,1)):
                destination = random.randint(0,len(bottom)-1)
                
                if(bottom[destination]==nr):
                    vehicles.append(Vehicle(0,road,0,[False])) # ||
                    
                else:
                    #print(bottom[destination])
                    vehicles.append(Vehicle(0,road,0,[1+less,bottom[destination],False,'P','P'])) # -> /
            else:
                destination = random.randint(0,len(upper)-1)
                if(upper[destination]==nr):
                    vehicles.append(Vehicle(0,road,0,[False])) # ||
                else:
                    #print(upper[destination])
                    vehicles.append(Vehicle(0,road,0,[1+less,upper[destination],False,'L','P'])) # -> /
        else: #przejazd gora
            if(random.randint(0,1)):
                destination = random.randint(0,len(upper)-1)
                if(upper[destination]==nr):
                    vehicles.append(Vehicle(0,road,0,[False])) # ||
                else:
                    vehicles.append(Vehicle(0,road,0,[4+less,upper[destination],False,'P','L'])) # <- /
            else:
                destination = random.randint(0,len(bottom)-1)
                if(bottom[destination]==nr):
                    vehicles.append(Vehicle(0,road,0,[False])) # ||
                else:
                    vehicles.append(Vehicle(0,road,0,[4+less,bottom[destination],False,'L','L'])) # <- /

bottom_destinations=[1,4,6,18]
upper_destinations=[2,5,8,10,11,14,15,19]


def add_vehicle():
    #(road , freq , nr , reverse , only_enter , only_entry_other_side , forward)
    vehicle_creator(r.r1,mazowiecka,1,True)
    vehicle_creator(r.r2,krowoderska,2)
    vehicle_creator(r.r3,zulawskiego,3,False,True)
    vehicle_creator(r.r4,slaska,4,True)
    vehicle_creator(r.r6,pradnicka1,6,True)
    vehicle_creator(r.r7,pradnicka2,7,True,only_entry_other_side=True)
    vehicle_creator(r.r8,dluga1,8,only_entry_other_side=True)
    vehicle_creator(r.r9,dluga2,9,only_entry=True)
    vehicle_creator(r.r12,kamienna1,12,True,only_entry=True)
    vehicle_creator(r.r13,kamienna2,13,True,only_entry_other_side=True)
    vehicle_creator(r.r16,aleja29listopada1,16,True,only_entry=True)
    vehicle_creator(r.r17,aleja29listopada2,17,True,only_entry=True)
    vehicle_creator(r.r20,aleja29listopada3,20,only_entry=True)

vehicles=[] #list of vehicles that are on road