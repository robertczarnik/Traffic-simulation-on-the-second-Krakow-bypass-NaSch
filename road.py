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
        
    def update_cell(self,x):
        self.road.lane[self.position].vehicle=x
    
    def get_speed_limit(self):
        return self.road.lane[self.position].speed_limit
    
    def check_collision(self,distance):
        if(self.position+distance >= len(self.road.lane)): #out of road
            return False
        
        return self.road.lane[self.position+distance].vehicle==1
    
    def check_crossing(self,distance):
        if(self.road.lane[self.position+distance].crossing_id!=None): #czyli jest jakies skrzyzowanie drog
            return [self.road.other_roads[self.road.lane[self.position+distance].crossing_id-1],self.road.lane[self.position+distance].index] #zwracam droge ktora sie krzyzuje i pozycje w niej tego miejsca
        return None
        

#representing roads
main_road1_len=55
main_road2_len=55
main_road3_len=55

road1_len=30

main_road1 = [0] * main_road1_len
main_road2 = [0] * main_road2_len
main_road3 = [0] * main_road3_len

road1 = [0] * road1_len


for i in range(main_road1_len):
    main_road1[i]=Cell(0,False);
    
for i in range(main_road2_len):
    main_road2[i]=Cell(0,False);
    
for i in range(main_road3_len):
    main_road3[i]=Cell(0,False);
    
    
for i in range(road1_len):
    road1[i]=Cell(0,False);


main_road1[24]=Cell(0,True,1,13); #dla kazdej z tych drog to jest pierwsze skrzyzowanie
main_road2[24]=Cell(0,True,1,14);
main_road3[24]=Cell(0,True,1,15);

road1[13]=Cell(0,True,1,24); #tutaj juz ta droga krzyzuje sie po kolei z trzema innymi
road1[14]=Cell(0,True,2,24);
road1[15]=Cell(0,True,3,24);

main_road1 = Road(main_road1,None,main_road2)
main_road2 = Road(main_road2,main_road1,main_road3)
main_road3 = Road(main_road3,main_road2,None)

road1 = Road(road1)

main_road1.other_roads=[road1]#dodanie drog z ktorymi sie po kolei krzyzuja
main_road2.other_roads=[road1]
main_road3.other_roads=[road1]

road1.other_roads=[main_road1,main_road2,main_road3]
#--


vehicles=[] #list of vehicles that are on road
vehicles.append(Vehicle(0,main_road1,0)) #dodanie pojazdu do road1 na miejscu 0 z predkoscia poczatkowa 0
vehicles.append(Vehicle(0,main_road2,0))
vehicles.append(Vehicle(0,main_road3,0))

def print_roads():
    for i in range(13):
        print(' ' * 48,end='')
        print(road1.lane[i].vehicle)
        
    main_road1.print_road()
    main_road2.print_road()
    main_road3.print_road()
    
    for i in range(16,30):
        print(' ' * 48,end='')
        print(road1.lane[i].vehicle)

clear()
print_roads()

for j in range(30): #mainloop
    vehicles_down=[]
    for i in range(len(vehicles)):
        flag_update=False; #flaga do przeskoczenia do koeljengo obiegu petli w przypadku juz zaktualizowanego miejsca pojazdu
        
        if(vehicles[i].velocity < vehicles[i].get_speed_limit()): #acceleration
            vehicles[i].velocity+=1
            
        for k in range(1,vehicles[i].velocity+1): #braking
            if(vehicles[i].check_collision(k)):
                vehicles[i].velocity=k-1
                break
            
        if(random.randint(0, 9)<4 and vehicles[i].velocity>0): #Randomisation 40% chance to slow down
            vehicles[i].velocity-=1
            
              
        vehicles[i].update_cell(0) #remove vehicle from previous position
        
        if( (vehicles[i].position+vehicles[i].velocity) >= len(vehicles[i].road.lane)):  #wyjechanie poza droge
            vehicles_down.append(i) #indeksy pojazdow ktore trzeba usunac
            continue
        
        for k in range(1,vehicles[i].velocity+1): #sprawdzenie czy nie ma jakiegos skrzyzowania przed pojazdem
            road_info=vehicles[i].check_crossing(k)
            if(road_info!=None): #jest jakies skrzyzowanie
                if(road_info[0].lane[road_info[1]].vehicle == 1): #sprawdzam czy jest tam pojazd
                    vehicles[i].velocity=k-1 #jesli jest to zmieniejszam predkosc tak zeby w niego nie wjechac
                else: #jesli nie ma to musze podjac decyzje czy skrecic - poki co szansa 50%
                    if(random.randint(0, 9)<5):
                        vehicles[i].road=road_info[0]
                        vehicles[i].position=road_info[1]
                        vehicles[i].velocity=1 #przy skrecie zmniejszenie predkosci do 1
                        vehicles[i].update_cell(1) #na jednej warstwie widac tylko ta jedynke(ten pojazd)
                        flag_update=True
                        break #potrzebne to break zeby nastapila tylko jedna aktualizacja
        
        if(flag_update):
            continue;
            
        vehicles[i].position+=vehicles[i].velocity #Driving
        vehicles[i].update_cell(1)
            
     
    for w in range(len(vehicles_down)-1,-1): #usuwanie pojazdow ktore wyjechaly poza droge (usuwanie od tylu zeby nie bylo bledow z odwolaniem do nieistniejacego pojazdu)
        vehicles.pop(vehicles_down[w])
    
    if(road1.lane[0].vehicle==0): #dodaj samochod do drogi
        case=random.randint(0,3)
        if(case==0):
            vehicles.append(Vehicle(0,main_road1,0))  
        elif(case==1):
            vehicles.append(Vehicle(0,main_road2,0))  
        elif(case==2):
            vehicles.append(Vehicle(0,main_road3,0))  
        
        
    time.sleep(0.6)

    clear()
    print_roads()
    


















    