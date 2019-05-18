import vehicle as veh
import visualisation as vis
import time
import random
import road as r
import config

clear = lambda: print('\n' * 55) 

def check_overtaking(vehicle,road):
    pos=vehicle.position
    if(len(road.lane)<=pos+vehicle.velocity+1): #zeby nie wyleciec poza droge
        return False
    
    for i in range(pos- ( road.lane[pos].speed_limit-vehicle.velocity)  ,pos+vehicle.velocity+1): # (gap_lookback,gap_ahead)
            if(road.lane[i].vehicle>0): #sprawdzenie czy jest wolne miejsce zeby mozna bylo wyprzedzac
                return False
    return True

clear()
vis.print_roads()
vehicles=veh.vehicles
traffic_lights_timer=0

while(True): #mainloop
    vehicles_down=[]
    for i in range(len(vehicles)):
        flag_update=False; #flaga do przeskoczenia do koeljengo obiegu petli w przypadku juz zaktualizowanego miejsca pojazdu
        
        if(vehicles[i].road.lane[vehicles[i].position].vehicle==1): #jesli sa swiatla wlaczone tam to nie usuwaj
            vehicles[i].update_cell(0) #remove vehicle from previous position
        
        if(vehicles[i].velocity < vehicles[i].get_speed_limit()): #acceleration
            vehicles[i].velocity+=1
            
        if(vehicles[i].destination[len(vehicles[i].destination)//2]==True): #zbliza sie moj cel i pasuje zmienic pas na wlasciwy
            if(vehicles[i].destination[len(vehicles[i].destination)-1]=='L'): #zmieniaj na lewy pas jesli to mozliwe
                if(vehicles[i].road.l_road != None and check_overtaking(vehicles[i],vehicles[i].road.l_road)): #jest lewy pas i odpowiednia luka na nim
                    vehicles[i].road=vehicles[i].road.l_road
                else: #hamowanko jesli jest przed nami samochod
                    for k in range(1,vehicles[i].velocity+1):
                        if(vehicles[i].check_collision(k)):
                            vehicles[i].velocity=k-1
                        break
            else: #zmieniaj na prawy jesli to mozliwe
                if(vehicles[i].road.r_road != None and check_overtaking(vehicles[i],vehicles[i].road.r_road)):#jest prawy pas i odpowiednia luka na nim
                    vehicles[i].road=vehicles[i].road.r_road
                else: #hamowanko jesli jest przed nami samochod
                    for k in range(1,vehicles[i].velocity+1):
                        if(vehicles[i].check_collision(k)):
                            vehicles[i].velocity=k-1
                        break
        else:    
            for k in range(1,vehicles[i].velocity+1): #braking
                if(vehicles[i].check_collision(k)): #jest jakis pojazd przed nami, mozemy zwolnic lub probowac wyprzedzic go
                    if(vehicles[i].road.l_road != None and check_overtaking(vehicles[i],vehicles[i].road.l_road)): #jest lewy pas i odpowiednia luka na nim
                        vehicles[i].road=vehicles[i].road.l_road
                    elif(vehicles[i].road.r_road != None and check_overtaking(vehicles[i],vehicles[i].road.r_road)):#jest prawy pas i odpowiednia luka na nim
                        vehicles[i].road=vehicles[i].road.r_road
                    else:
                        vehicles[i].velocity=k-1 #zwalniamy bo nie mozna wyprzedzic   
                    break
            
        if(random.randint(0, 9)<4 and vehicles[i].velocity>1): #Randomisation 40% chance to slow down
            vehicles[i].velocity-=1
            
              
        
        if( (vehicles[i].position+vehicles[i].velocity) >= len(vehicles[i].road.lane)):  #wyjechanie poza droge
            vehicles_down.append(i) #indeksy pojazdow ktore trzeba usunac
            continue
        
        
        if(vehicles[i].road.lane[vehicles[i].position+1].vehicle==3):
            road_info=vehicles[i].check_crossing(0)
            
            
        for k in range(1,vehicles[i].velocity+1): #sprawdzenie czy nie ma jakiegos skrzyzowania przed pojazdem
            road_info=vehicles[i].check_crossing(k)
            if(road_info!=None): #jest jakies skrzyzowanie
                if(road_info[0].lane[road_info[1]].vehicle > 0): #sprawdzam czy jest tam pojazd
                    vehicles[i].velocity=k-1 #jesli jest to zmieniejszam predkosc tak zeby w niego nie wjechac
                    break
                else: #jesli nie ma to sprawdzam czy ta droga jest moim celem
                    if( ( vehicles[i].destination[0]==vehicles[i].road.lane[vehicles[i].position+k].crossing_id )):# or vehicles[i].road.lane[vehicles[i].position+k+1].vehicle==3 ) and road_info[0].lane[road_info[1]+1].vehicle !=3): # and upewnij sie ze skrzyzowanie to nie jest wjazdem tylko
                        vehicles[i].destination.pop(0)
                        vehicles[i].destination.pop()
                        vehicles[i].destination[len(vehicles[i].destination)//2]=False
                        vehicles[i].road=road_info[0]
                        vehicles[i].position=road_info[1]
                        vehicles[i].velocity=1 #przy skrecie zmniejszenie predkosci do 1
                        if(vehicles[i].road.lane[vehicles[i].position].vehicle==0):
                            vehicles[i].update_cell(1) #na jednej warstwie widac tylko ta jedynke(ten pojazd)
                        flag_update=True
                        break #potrzebne to break zeby nastapila tylko jedna aktualizacja
                    elif(vehicles[i].destination[0]<=vehicles[i].road.lane[vehicles[i].position+k].crossing_id+2): #jest to do 2 skrzyzowac przed skrzyzowaniem celem
                        vehicles[i].destination[len(vehicles[i].destination)//2]=True
                     
        
        if(flag_update):
            continue;
            
        vehicles[i].position+=vehicles[i].velocity #Driving
        if(vehicles[i].road.lane[vehicles[i].position].vehicle==0):
            vehicles[i].update_cell(1)
        
    #---swiatla---
    if(traffic_lights_timer==80):
        traffic_lights_timer=0
    r.traffic_lights_management(traffic_lights_timer)
    traffic_lights_timer+=1
    #-------------
            
     
    for w in range(len(vehicles_down)-1,-1): #usuwanie pojazdow ktore wyjechaly poza droge (usuwanie od tylu zeby nie bylo bledow z odwolaniem do nieistniejacego pojazdu)
        vehicles.pop(vehicles_down[w])
        
    #dodawanie pojazdow    
    veh.add_vehicle()
    #veh.add_vehicle()      
    #if(r.main_road3.lane[0].vehicle==0 and vehicles == []):
        #vehicles.append(veh.Vehicle(0,r.main_road3,35))  
        
    time.sleep(2/config.simulation_speed)

    clear()
    vis.print_roads()