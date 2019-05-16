import vehicle as veh
import visualisation as vis
import time
import random
import road as r

clear = lambda: print('\n' * 55) 

def check_overtaking(vehicle,road):
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.velocity+1): #zeby nie wyleciec poza droge
        return False
    
    for i in range(pos-road.lane[pos].speed_limit,pos+vehicle.velocity+1): # (gap_lookback,gap_ahead)
            if(road.lane[i].vehicle>0): #sprawdzenie czy jest wolne miejsce zeby mozna bylo wyprzedzac
                return False
    return True

clear()
vis.print_roads()
vehicles=veh.vehicles
lights_change=1
lights_timer=9

for j in range(30): #mainloop
    vehicles_down=[]
    lights_timer+=1
    for i in range(len(vehicles)):
        flag_update=False; #flaga do przeskoczenia do koeljengo obiegu petli w przypadku juz zaktualizowanego miejsca pojazdu
        
        if(vehicles[i].road.lane[vehicles[i].position].vehicle==1): #jesli sa swiatla wlaczone tam to nie usuwaj
            vehicles[i].update_cell(0) #remove vehicle from previous position
        
        if(vehicles[i].velocity < vehicles[i].get_speed_limit()): #acceleration
            vehicles[i].velocity+=1
            
        for k in range(1,vehicles[i].velocity+1): #braking
            if(vehicles[i].check_collision(k)): #jest jakis pojazd przed nami, mozemy zwolnic lub probowac wyprzedzic go
                if(vehicles[i].road.l_road != None and check_overtaking(vehicles[i],vehicles[i].road.l_road)): #jest lewy pas i odpowiednia luka na nim
                    vehicles[i].road=vehicles[i].road.l_road
                elif(vehicles[i].road.r_road != None and check_overtaking(vehicles[i],vehicles[i].road.r_road)):#jest prawy pas i odpowiednia luka na nim
                    vehicles[i].road=vehicles[i].road.r_road
                else:
                    vehicles[i].velocity=k-1 #zwalniamy bo nie mozna wyprzedzic
                
                break
            
        if(random.randint(0, 9)<4 and vehicles[i].velocity>0): #Randomisation 40% chance to slow down
            vehicles[i].velocity-=1
            
              
        
        if( (vehicles[i].position+vehicles[i].velocity) >= len(vehicles[i].road.lane)):  #wyjechanie poza droge
            vehicles_down.append(i) #indeksy pojazdow ktore trzeba usunac
            continue
        
        
        for k in range(1,vehicles[i].velocity+1): #sprawdzenie czy nie ma jakiegos skrzyzowania przed pojazdem
            road_info=vehicles[i].check_crossing(k)
            if(road_info!=None): #jest jakies skrzyzowanie
                if(road_info[0].lane[road_info[1]].vehicle > 0): #sprawdzam czy jest tam pojazd
                    vehicles[i].velocity=k-1 #jesli jest to zmieniejszam predkosc tak zeby w niego nie wjechac
                else: #jesli nie ma to musze podjac decyzje czy skrecic - poki co szansa 40%
                    if(random.randint(0, 9)<4 or vehicles[i].road.lane[vehicles[i].position+k+1].vehicle==3):
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
        
        #---swiatla---
    
        if(lights_timer==10):
            lights_change*=-1
            r.traffic_ligths1(lights_change)
            lights_timer=0
            
        #-------------
            
     
    for w in range(len(vehicles_down)-1,-1): #usuwanie pojazdow ktore wyjechaly poza droge (usuwanie od tylu zeby nie bylo bledow z odwolaniem do nieistniejacego pojazdu)
        vehicles.pop(vehicles_down[w])
        
    #dodawanie pojazdow    
    veh.add_vehicle()
    veh.add_vehicle()      
        
    time.sleep(0.6)

    clear()
    vis.print_roads()