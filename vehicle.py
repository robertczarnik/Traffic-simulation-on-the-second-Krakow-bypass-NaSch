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

bottom_destinations=[1,4,6,18,23,24,31,34,35,38,50,57,64,65,
                     69,79,83,84,86,92,96,98,105,108,109,
                     113,114,116,118,122,123,130,134,141,
                     150,156,158,163]
upper_destinations=[2,5,8,10,11,14,15,
                    19,22,29,36,37,40,44,45,48,49,
                    54,61,62,68,72,73,74,81,91,93,94,95,110,
                    111,135,147,151,152,157,161]


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
aleja29listopada4=low #21
aleja29listopada5=low #25
aleja29listopada6=low #26
aleja29listopada7=low #27
aleja29listopada8=low #28
stwosza=low           #30
stwosza2=low          #32
rakowicka1=low        #35
rakowicka2=low        #36
lubomirskiego1=low    #39
lubomirskiego2=low    #41
r42=low               #42
r43=low               #43
r46=low               #46
r47=low               #47
r51=low               #51
r52=low               #52
r53=low               #53
r55=low               #55
r56=low               #56
r57=low               #57
r58=low               #58
r59=low               #59
r60=low               #60
r61=low               #61
r63=low               #63
r66=low               #66
r67=low               #67

r69=low               #69
r70=low               #70
r71=low               #71
r72=low               #72

r75=low               #75
r76=low               #76
r78=low               #78

r80=low               #80
r82=low               #82
r85=low               #85
r87=low               #87

r88=low               #88
r89=low               #89
r92=low               #92
r93=low               #93
r97=low               #97
r99=low               #99

r101=low               #101
r102=low               #102
r106=low               #106

r107=low               #107
r108=low               #108
r109=low               #109
r110=low               #110
r111=low               #111
r112=low               #112

r115=low               #115
r117=low               #117
r119=low               #119
r120=low               #120


r126=low               #126
r127=low               #127
r128=low               #128
r129=low               #129
r131=low               #131

r133=low               #133
r134=low               #134
r135=low               #135
r136=low               #136
r137=low               #137
r139=low               #139
r140=low               #140
r142=low               #142
r143=low               #143

r145=low               #145
r146=low               #146

r148=low               #148
r149=low               #149
r150=low               #150
r151=low               #151
r152=low               #152

r154=low               #154

r155=low               #155
r156=low               #156
r157=low               #157

r159=low               #159
r161=low               #161
r162=low               #162
r163=low               #163
r164=low               #164



def add_vehicle():
#(road , freq , nr , reverse , only_enter , only_entry_other_side , forward , less)
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
    vehicle_creator(r.r21,aleja29listopada4,21,True,only_entry=True)
    vehicle_creator(r.r25,aleja29listopada5,25,True,only_entry=True)
    vehicle_creator(r.r26,aleja29listopada6,26,True,only_entry=True)
    vehicle_creator(r.r27,aleja29listopada7,27,only_entry=True)
    vehicle_creator(r.r28,aleja29listopada8,28,only_entry=True)
    vehicle_creator(r.r30,stwosza,30,True,only_entry=True)
    vehicle_creator(r.r32,stwosza2,32,only_entry=True)
    vehicle_creator(r.r35,rakowicka1,35,True,less=1)
    vehicle_creator(r.r36,rakowicka2,36,less=1)
    vehicle_creator(r.r39,lubomirskiego1,39,True,only_entry=True)
    vehicle_creator(r.r41,lubomirskiego2,41,only_entry=True)
    vehicle_creator(r.r42,r42,42,True)
    vehicle_creator(r.r43,r43,43,True,only_entry_other_side=True)
    vehicle_creator(r.r46,r46,46,True,only_entry=True)
    vehicle_creator(r.r47,r47,47,True,only_entry=True)
    vehicle_creator(r.r51,r51,51,only_entry_other_side=True)
    vehicle_creator(r.r52,r52,52)
    vehicle_creator(r.r53,r53,53,True,only_entry=True)
    vehicle_creator(r.r55,r55,55,only_entry=True)
    vehicle_creator(r.r56,r56,56,True,only_entry=True)
    vehicle_creator(r.r57,r57,57,True,only_entry_other_side=True)
    vehicle_creator(r.r58,r58,58,True,forward=True)
    vehicle_creator(r.r59,r59,59,only_entry_other_side=True)
    vehicle_creator(r.r60,r60,60,forward=True)
    vehicle_creator(r.r61,r61,61,only_entry=True)
    vehicle_creator(r.r63,r63,63,True,only_entry=True)
    vehicle_creator(r.r66,r66,66,only_entry=True)
    vehicle_creator(r.r67,r67,67,True,only_entry=True)
    vehicle_creator(r.r69,r69,69,True)
    vehicle_creator(r.r70,r70,70,True,only_entry_other_side=True)
    vehicle_creator(r.r71,r71,71,only_entry_other_side=True)
    vehicle_creator(r.r72,r72,72)
    vehicle_creator(r.r75,r75,75,True)
    vehicle_creator(r.r76,r76,76,True)
    vehicle_creator(r.r78,r78,78,True,only_entry=True)
    vehicle_creator(r.r80,r80,80,only_entry=True)
    vehicle_creator(r.r82,r82,82,True,only_entry=True)
    vehicle_creator(r.r85,r85,85,only_entry=True)
    vehicle_creator(r.r87,r87,87,only_entry=True)
    vehicle_creator(r.r88,r88,88,only_entry=True)
    vehicle_creator(r.r89,r89,89,only_entry=True)
    vehicle_creator(r.r92,r92,92,True)
    vehicle_creator(r.r93,r93,93)
    vehicle_creator(r.r97,r97,97,only_entry=True)
    vehicle_creator(r.r99,r99,99,only_entry=True)
    vehicle_creator(r.r101,r101,101,True,only_entry=True)
    vehicle_creator(r.r102,r102,102,True,only_entry=True)
    vehicle_creator(r.r106,r106,106,only_entry=True)
    vehicle_creator(r.r107,r107,107,True,only_entry=True)
    vehicle_creator(r.r108,r108,108,True,only_entry_other_side=True)
    vehicle_creator(r.r109,r109,109,True,forward=True)
    vehicle_creator(r.r110,r110,110,only_entry_other_side=True)
    vehicle_creator(r.r111,r111,111,forward=True)
    vehicle_creator(r.r112,r112,112,only_entry=True)
    vehicle_creator(r.r115,r115,115,only_entry=True)
    vehicle_creator(r.r117,r117,117,only_entry=True)
    vehicle_creator(r.r119,r119,119,only_entry=True)
    vehicle_creator(r.r120,r120,120,True,only_entry=True)
    
    vehicle_creator(r.r126,r126,126,only_entry=True)
    vehicle_creator(r.r127,r127,127,only_entry=True)
    vehicle_creator(r.r128,r128,128,True,only_entry=True)
    vehicle_creator(r.r129,r129,129,True,only_entry=True)
    vehicle_creator(r.r131,r131,131,only_entry=True)
    
    vehicle_creator(r.r133,r133,133,True,only_entry=True)
    vehicle_creator(r.r134,r134,134,True,only_entry_other_side=True)
    vehicle_creator(r.r135,r135,135,only_entry_other_side=True)
    vehicle_creator(r.r136,r136,136,only_entry=True)

    vehicle_creator(r.r137,r137,137,True,only_entry=True)
    vehicle_creator(r.r139,r139,139,True,only_entry=True)
    vehicle_creator(r.r140,r140,140,only_entry=True)
    
    vehicle_creator(r.r142,r142,142,only_entry=True)
    vehicle_creator(r.r143,r143,143,True,only_entry=True)

    vehicle_creator(r.r145,r145,145,True,only_entry=True)
    vehicle_creator(r.r146,r146,146,True,only_entry_other_side=True)
    
    
    vehicle_creator(r.r148,r148,148,True,only_entry=True)
    vehicle_creator(r.r149,r149,149,True,only_entry=True)
    
    vehicle_creator(r.r150,r150,150,True,only_entry_other_side=True)
    vehicle_creator(r.r151,r151,151,only_entry_other_side=True)
    vehicle_creator(r.r152,r152,152,only_entry=True)
    vehicle_creator(r.r154,r154,154,only_entry=True)

    vehicle_creator(r.r155,r155,155,True,only_entry=True)
    vehicle_creator(r.r156,r156,156,True,only_entry_other_side=True)
    vehicle_creator(r.r157,r157,157)
    
    vehicle_creator(r.r159,r159,159,True,only_entry=True)
    vehicle_creator(r.r161,r161,161,True)
    vehicle_creator(r.r162,r162,162,True,only_entry_other_side=True)
    vehicle_creator(r.r163,r163,163,only_entry_other_side=True)
    vehicle_creator(r.r164,r164,164,only_entry=True)















vehicles=[] #list of vehicles that are on road