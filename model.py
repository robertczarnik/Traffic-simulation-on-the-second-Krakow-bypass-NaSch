import vehicle as veh
import visualisation as vis
import time
import random
import road as r
import config

def simulation():
    clear = lambda: print('\n' * 55)     
    
    clear()
    vis.print_roads()
    
    vehicles=veh.vehicles
    traffic_lights_timer=20
    main_roads=[r.main_road1,r.main_road2,r.main_road3,r.main_road4,r.main_road5,r.main_road6]

    while(True): #mainloop
        vehicles_down=[]
        for i in range(len(vehicles)):
            ### initial settings ###
            flag_update=False #flaga do przeskoczenia do koeljengo obiegu petli w przypadku juz zaktualizowanego miejsca pojazdu
            flag_action=False #one action for one vehicle
            
            if(vehicles[i].road.lane[vehicles[i].position].vehicle==1): #jesli sa swiatla wlaczone tam to nie usuwaj
                vehicles[i].update_cell(0) #remove vehicle from previous position
            #--------------------------
            
            ### acceleration ###
            if(vehicles[i].velocity < vehicles[i].get_speed_limit()): 
                vehicles[i].velocity+=1
            #--------------------------
            
            ### changing road or overtaking or breaking ###
            destination_close=vehicles[i].destination[len(vehicles[i].destination)//2]
            if(destination_close==True): #zbliza sie moj cel i pasuje zmienic pas na wlasciwy
                if(vehicles[i].destination[len(vehicles[i].destination)-1]=='L'): #zmieniaj na lewy pas jesli to mozliwe
                    if(vehicles[i].road.l_road != None):
                        change_velocity=veh.changing_road(vehicles[i],vehicles[i].road.l_road)
                        if(change_velocity!=False): #jest lewy pas i miejsce na nim
                            vehicles[i].road=vehicles[i].road.l_road
                            vehicles[i].velocity=change_velocity
                            flag_action=True                    
                else: #zmieniaj na prawy jesli to mozliwe
                    if(vehicles[i].road.r_road != None):
                        change_velocity=veh.changing_road(vehicles[i],vehicles[i].road.r_road)
                        if(change_velocity!=False):#jest prawy pas i miejsce  luka na nim
                            vehicles[i].road=vehicles[i].road.r_road
                            vehicles[i].velocity=change_velocity
                            flag_action=True
                        
            if(not flag_action): 
                for k in range(1,vehicles[i].velocity+1): #braking
                    
                    if(len(vehicles[i].road.lane)>(vehicles[i].position+k+1) and vehicles[i].road.lane[vehicles[i].position+k+1].vehicle==3): #mozna to lepiej zrobic, potrzebne do konczenia sie drogi i wstawionych tam trojek
                        destination_close=False
                    
                    if(vehicles[i].check_collision(k) or (len(vehicles[i].road.lane)>(vehicles[i].position+k+1) and vehicles[i].road.lane[vehicles[i].position+k+1].vehicle==3)): #jest jakis pojazd przed nami, mozemy zwolnic lub probowac wyprzedzic go
                        if(destination_close==False and vehicles[i].road.l_road != None and veh.check_overtaking(vehicles[i],vehicles[i].road.l_road)): #jest lewy pas i odpowiednia luka na nim
                            vehicles[i].road=vehicles[i].road.l_road
                        elif(destination_close==False and vehicles[i].road.r_road != None and veh.check_overtaking(vehicles[i],vehicles[i].road.r_road)):#jest prawy pas i odpowiednia luka na nim
                            vehicles[i].road=vehicles[i].road.r_road
                        else:
                            vehicles[i].velocity=k-1 #zwalniamy bo nie mozna wyprzedzic   
                        break
            #--------------------------
            
            ### random braking ###
            if(random.randint(0, 9)<config.p and vehicles[i].velocity>1): #(p*10)% chance to slow down if velocity>1
                vehicles[i].velocity-=1
            #--------------------------   
                  
                
            ### crossings ###
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
                            
                            odl=vehicles[i].destination[0]-vehicles[i].road.lane[vehicles[i].position+k].crossing_id
                            if(odl>=0 and odl < 7):
                            #if(vehicles[i].destination[0]<=vehicles[i].road.lane[vehicles[i].position+k].crossing_id+6): #jest to do 6 skrzyzowac przed skrzyzowaniem celem
                                vehicles[i].destination[len(vehicles[i].destination)//2]=True
                            
                            
                            vehicles[i].road=road_info[0]
                            vehicles[i].position=road_info[1]
                            vehicles[i].velocity=1 #przy skrecie zmniejszenie predkosci do 1
                            if(vehicles[i].road.lane[vehicles[i].position].vehicle==0):
                                vehicles[i].update_cell(1) #na jednej warstwie widac tylko ta jedynke(ten pojazd)
                            flag_update=True
                            
                            
                            
                            break #potrzebne to break zeby nastapila tylko jedna aktualizacja
                        odl=vehicles[i].destination[0]-vehicles[i].road.lane[vehicles[i].position+k].crossing_id
                        if(odl>=0 and odl < 7):
                        #if(vehicles[i].destination[0]<=vehicles[i].road.lane[vehicles[i].position+k].crossing_id+4): #jest to do 4 skrzyzowac przed skrzyzowaniem celem
                            vehicles[i].destination[len(vehicles[i].destination)//2]=True
            #--------------------------
                         
            ### update car position ###
            if(flag_update):
                continue;
                
            ### out of road OR loop ###
            if( (vehicles[i].position+vehicles[i].velocity) >= len(vehicles[i].road.lane)):  #wyjechanie poza droge
                if(vehicles[i].road in main_roads):
                    vehicles[i].position=(vehicles[i].position+vehicles[i].velocity) - len(vehicles[i].road.lane) 
                    if(vehicles[i].road.lane[vehicles[i].position].vehicle==0):
                        vehicles[i].update_cell(1)
                    continue
                else:
                    vehicles_down.append(i) #indeksy pojazdow ktore trzeba usunac
                    continue
            #--------------------------   
            
            vehicles[i].position+=vehicles[i].velocity
            if(vehicles[i].road.lane[vehicles[i].position].vehicle==0):
                vehicles[i].update_cell(1)
            #--------------------------
            
        ### traffic lights ###
        if(traffic_lights_timer==60):
            traffic_lights_timer=0
        r.traffic_lights_management(traffic_lights_timer)
        traffic_lights_timer+=1
        #--------------------------
                
        ### vehicles management ### 
        for w in range(len(vehicles_down)-1,-1,-1): #usuwanie pojazdow ktore wyjechaly poza droge (usuwanie od tylu zeby nie bylo bledow z odwolaniem do nieistniejacego pojazdu)
            vehicles.pop(vehicles_down[w])
                            
        veh.add_vehicle()
        #--------------------------      
        
        ### simulation speed and visualisation ###    
        time.sleep(2/config.simulation_speed)
        clear()
        vis.print_roads()
        #--------------------------  