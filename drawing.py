import pygame,sys, road
import vehicle as veh
import visualisation as vis
import time
import random
import road as r
import config
class drawing(object):
    def __init__(self):
        # initialization
        clock = pygame.time.Clock()
        FPS = 15
        p = 100
        self.width = 845
        self.height = 1075
        self.mainMap1 = {}
        self.mainMap2 ={}
        self.mainMap3 ={}
        self.cords=[]
        self.mapList=[]
        self.main_road_4=[]
        self.main_road_5=[]
        self.main_road_6=[]
        self.lista=[5,1,1,15,1,1,16,1,1,1]


        self.screen = pygame.display.set_mode((self.width, self.height))
        clear = lambda: print('\n' * 55)
        clear()
        vis.print_roads()
        vehicles = veh.vehicles
        traffic_lights_timer = 20
        main_roads = [r.main_road1, r.main_road2, r.main_road3, r.main_road4, r.main_road5, r.main_road6]
        while True:
            # Handle events
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        sys.exit(0)
                    if(event.key==pygame.K_F12):
                        #fullscreen
                        self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
                    if (event.key == pygame.K_F11):
                        self.screen = pygame.display.set_mode((self.width, self.height))
                    if (event.key == pygame.K_F10):
                        print(self.cords)
                    if (event.key == pygame.K_SPACE):
                        self.cords.pop()
                    if (event.key == pygame.K_F9):
                        self.makeList(self.lista)
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    # print event.button
                    w=pygame.mouse.get_pos()
                    print(w)
                    self.cords.append(w)
                    pygame.display.update()

            vehicles_down = []
            for i in range(len(vehicles)):
                ### initial settings ###
                flag_update = False  # flaga do przeskoczenia do koeljengo obiegu petli w przypadku juz zaktualizowanego miejsca pojazdu
                flag_action = False  # one action for one vehicle

                if (vehicles[i].road.lane[
                    vehicles[i].position].vehicle == 1):  # jesli sa swiatla wlaczone tam to nie usuwaj
                    vehicles[i].update_cell(0)  # remove vehicle from previous position
                # --------------------------

                ### acceleration ###
                if (vehicles[i].velocity < vehicles[i].get_speed_limit()):
                    vehicles[i].velocity += 1
                # --------------------------

                ### changing road or overtaking or breaking ###
                destination_close = vehicles[i].destination[len(vehicles[i].destination) // 2]
                if (destination_close == True):  # zbliza sie moj cel i pasuje zmienic pas na wlasciwy
                    if (vehicles[i].destination[
                        len(vehicles[i].destination) - 1] == 'L'):  # zmieniaj na lewy pas jesli to mozliwe
                        if (vehicles[i].road.l_road != None):
                            change_velocity = veh.changing_road(vehicles[i], vehicles[i].road.l_road)
                            if (change_velocity != False):  # jest lewy pas i miejsce na nim
                                vehicles[i].road = vehicles[i].road.l_road
                                vehicles[i].velocity = change_velocity
                                flag_action = True
                    else:  # zmieniaj na prawy jesli to mozliwe
                        if (vehicles[i].road.r_road != None):
                            change_velocity = veh.changing_road(vehicles[i], vehicles[i].road.r_road)
                            if (change_velocity != False):  # jest prawy pas i miejsce  luka na nim
                                vehicles[i].road = vehicles[i].road.r_road
                                vehicles[i].velocity = change_velocity
                                flag_action = True

                if (not flag_action):
                    for k in range(1, vehicles[i].velocity + 1):  # braking

                        if (len(vehicles[i].road.lane) > (vehicles[i].position + k + 1) and vehicles[i].road.lane[
                            vehicles[
                                i].position + k + 1].vehicle == 3):  # mozna to lepiej zrobic, potrzebne do konczenia sie drogi i wstawionych tam trojek
                            destination_close = False

                        if (vehicles[i].check_collision(k) or (
                                len(vehicles[i].road.lane) > (vehicles[i].position + k + 1) and vehicles[i].road.lane[
                            vehicles[
                                i].position + k + 1].vehicle == 3)):  # jest jakis pojazd przed nami, mozemy zwolnic lub probowac wyprzedzic go
                            if (destination_close == False and vehicles[i].road.l_road != None and veh.check_overtaking(
                                    vehicles[i], vehicles[i].road.l_road)):  # jest lewy pas i odpowiednia luka na nim
                                vehicles[i].road = vehicles[i].road.l_road
                            elif (destination_close == False and vehicles[
                                i].road.r_road != None and veh.check_overtaking(
                                vehicles[i], vehicles[i].road.r_road)):  # jest prawy pas i odpowiednia luka na nim
                                vehicles[i].road = vehicles[i].road.r_road
                            else:
                                vehicles[i].velocity = k - 1  # zwalniamy bo nie mozna wyprzedzic
                            break
                # --------------------------

                ### random braking ###
                if (random.randint(0, 9) < config.p and vehicles[
                    i].velocity > 1):  # (p*10)% chance to slow down if velocity>1
                    vehicles[i].velocity -= 1
                # --------------------------

                ### crossings ###
                for k in range(1,
                               vehicles[i].velocity + 1):  # sprawdzenie czy nie ma jakiegos skrzyzowania przed pojazdem
                    road_info = vehicles[i].check_crossing(k)
                    if (road_info != None):  # jest jakies skrzyzowanie
                        if (road_info[0].lane[road_info[1]].vehicle > 0):  # sprawdzam czy jest tam pojazd
                            vehicles[
                                i].velocity = k - 1  # jesli jest to zmieniejszam predkosc tak zeby w niego nie wjechac
                            break
                        else:  # jesli nie ma to sprawdzam czy ta droga jest moim celem
                            if ((vehicles[i].destination[0] == vehicles[i].road.lane[vehicles[
                                                                                         i].position + k].crossing_id)):  # or vehicles[i].road.lane[vehicles[i].position+k+1].vehicle==3 ) and road_info[0].lane[road_info[1]+1].vehicle !=3): # and upewnij sie ze skrzyzowanie to nie jest wjazdem tylko
                                vehicles[i].destination.pop(0)
                                vehicles[i].destination.pop()
                                vehicles[i].destination[len(vehicles[i].destination) // 2] = False

                                # TODO: usprawnic to
                                odl = abs(vehicles[i].destination[0] - vehicles[i].road.lane[
                                    vehicles[i].position + k].crossing_id)
                                if (odl >= 0 and odl < 7):
                                    # if(vehicles[i].destination[0]<=vehicles[i].road.lane[vehicles[i].position+k].crossing_id+6): #jest to do 6 skrzyzowac przed skrzyzowaniem celem
                                    vehicles[i].destination[len(vehicles[i].destination) // 2] = True

                                vehicles[i].road = road_info[0]
                                vehicles[i].position = road_info[1]
                                vehicles[i].velocity = 1  # przy skrecie zmniejszenie predkosci do 1
                                if (vehicles[i].road.lane[vehicles[i].position].vehicle == 0):
                                    vehicles[i].update_cell(1)  # na jednej warstwie widac tylko ta jedynke(ten pojazd)
                                flag_update = True

                                break  # potrzebne to break zeby nastapila tylko jedna aktualizacja
                            odl = vehicles[i].destination[0] - vehicles[i].road.lane[
                                vehicles[i].position + k].crossing_id
                            if (odl >= 0 and odl < 7):
                                # if(vehicles[i].destination[0]<=vehicles[i].road.lane[vehicles[i].position+k].crossing_id+4): #jest to do 4 skrzyzowac przed skrzyzowaniem celem
                                vehicles[i].destination[len(vehicles[i].destination) // 2] = True
                # --------------------------

                ### update car position ###
                if (flag_update):
                    continue;

                ### out of road OR loop ###
                if ((vehicles[i].position + vehicles[i].velocity) >= len(
                        vehicles[i].road.lane)):  # wyjechanie poza droge
                    if (vehicles[i].road in main_roads):
                        vehicles[i].position = (vehicles[i].position + vehicles[i].velocity) - len(
                            vehicles[i].road.lane)
                        if (vehicles[i].road.lane[vehicles[i].position].vehicle == 0):
                            vehicles[i].update_cell(1)
                        continue
                    else:
                        vehicles_down.append(i)  # indeksy pojazdow ktore trzeba usunac
                        continue
                # --------------------------

                vehicles[i].position += vehicles[i].velocity
                if (vehicles[i].road.lane[vehicles[i].position].vehicle == 0):
                    vehicles[i].update_cell(1)
                # --------------------------

            ### traffic lights ###
            if (traffic_lights_timer == 60):
                traffic_lights_timer = 0
            r.traffic_lights_management(traffic_lights_timer)
            traffic_lights_timer += 1
            # --------------------------

            ### vehicles management ###
            for w in range(len(vehicles_down) - 1, -1,
                           -1):  # usuwanie pojazdow ktore wyjechaly poza droge (usuwanie od tylu zeby nie bylo bledow z odwolaniem do nieistniejacego pojazdu)
                vehicles.pop(vehicles_down[w])

            veh.add_vehicle()
            # --------------------------

            ### simulation speed and visualisation ###
            time.sleep(2 / config.simulation_speed)
            #clear()
            #vis.print_roads()
            # --------------------------
            p=p+1
            bypassImage=pygame.image.load("roadsonmap1.jpg")
            #bypassImage=pygame.transform.scale(bypassImage,(825,1049))
            #bypassImage=pygame.transform.scale(bypassImage,(7423,9439))
            self.screen.blit(bypassImage,(0,0))
            #pygame.display.flip()
            #pygame.display.update()

            for i in range(len(self.cords)):
                (x,y)=self.cords[i]
                pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(x, y, 2, 2))

            self.draw_main_road_1()
            self.draw_main_road_2()
            self.draw_main_road_3()
            self.main_road_3()
            lista=[10,20,15]
            #self.draw_main_road_4()

            pygame.display.update()

            clock.tick(FPS)
    def makeList(self,listofnumbers):
        self.mapList.clear()
        self.mapList.append(self.cords[0])
        dx=0
        dy=0
        for i in range(0,len(self.cords)):
            if(i>0):
                (x1,y1)=self.cords[i]
                (x2,y2)=self.cords[i-1]
                x=x1-x2
                y=y1-y2
                dx=x/listofnumbers[i-1]
                dy=y/listofnumbers[i-1]
                print(listofnumbers[i-1])
                for k in range(listofnumbers[i-1]):
                    x2 = x2 + dx
                    y2 = y2 + dy
                    w = (x2, y2)
                    self.mapList.append(w)
        print(self.mapList)
        print(len(self.mapList))
        if(i>0):
            for i in range(len(self.mapList)):
                (x,y)=self.mapList[i]
                pygame.draw.rect(self.screen, (133, 230, 90), pygame.Rect(x, y, 2, 2))
        pygame.display.update()

    def makeMainMap1(self):
        w = 0
        h = 0
        # wszystkie punkty
        for d in range(len(road.main_road3.lane)):
            w = w + 5
            h = h + 4
            self.mainMap1[d]=(473 + w, 458 - h)

    def makeMainMap3(self):
        w = 0
        h = 0
        w1 = 0
        h1 = 0
        w2 = 0
        h2 = 0
        for d in range(32):
            w = w + 5
            h = h + 4
            self.mainMap3[d]=(479 + w, 466 - h)
        for d in range(32, 35):
            w = w + 6
            h = h + 3
            self.mainMap3[d]=(479 + w, 465 - h)
        for d in range(35, 38):
            w = w + 6
            h = h + 3
            self.mainMap3[d]=(479 + w, 464 - h)
        for d in range(38, 42):
            w = w + 6
            h = h + 3
            self.mainMap3[d]=(479 + w, 463 - h)
        for d in range(42, 44):
            w = w + 5
            h = h + 2
            self.mainMap3[d]=(479 + w, 461 - h)
        for d in range(44, 48):
            w = w + 5
            h = h + 2
            self.mainMap3[d]=(479 + w, 462 - h)
        for d in range(48, 52):
            w = w + 4
            h = h + 2
            self.mainMap3[d]=(479 + w, 462 - h)
        for d in range(52, 56):
            w = w + 6
            h = h + 2
            self.mainMap3[d] =(479 + w, 463 - h)
        for d in range(56, 59):
            w = w + 7
            h = h + 1
            self.mainMap3[d] = (476 + w, 461 - h)
        for d in range(59, 61):
            w = w + 6
            h = h + 1
            self.mainMap3[d] = (475 + w, 460 - h)
            # kolejny obrazek
        for d in range(61, 67):
            w = w + 6
            h = h + 1
            self.mainMap3[d] = (479 + w, 460 - h)
        for d in range(67, 1628):
            w = w + 6
            h = h + 1
            self.mainMap3[d] = (0, 0)

        for d in range(1628, 1638):
            self.mainMap3[d]= (172 + w1, 1027 - h1)
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1638, 1645):
            self.mainMap3[d] = (171 + w1, 1027 - h1)
            w1 = w1 + 2
            h1 = h1 + 7

        for d in range(1645, 1650):
            self.mainMap3[d]=(170 + w1, 1027 - h1)
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1650, 1655):
            self.mainMap3[d] =(170 + w1, 1027 - h1)
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1655, 1660):
            self.mainMap3[d]=(170 + w1, 1027 - h1)
            w1 = w1 + 3
            h1 = h1 + 7
        for d in range(1660, 1665):
            self.mainMap3[d]=(170 + w1, 1027 - h1)
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1665, 1670):
            self.mainMap3[d]=(169 + w1, 1027 - h1)
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1670, 1675):
            self.mainMap3[d]= (168 + w1, 1027 - h1)
            w1 = w1 + 2
            h1 = h1 + 6

        self.mainMap3[1675]=(281, 722)
        self.mainMap3[1676]=(296, 692)

        for d in range(1677, 1687):
            self.mainMap3[d]=(298 + w2, 685 - h2)
            w2 = w2 + 2
            h2 = h2 + 5
        for d in range(1687, 1696):
            self.mainMap3[d]=(298 + w2, 685 - h2)
            w2 = w2 + 3
            h2 = h2 + 6
        for d in range(1696, 1706):
            self.mainMap3[d]=(298 + w2, 685 - h2)
            w2 = w2 + 4
            h2 = h2 + 4
        for d in range(1706, 1716):
            self.mainMap3[d]=(299 + w2, 685 - h2)
            w2 = w2 + 5
            h2 = h2 + 4

        for d in range(1716, 1720):
            self.mainMap3[d] = (303 + w2, 681 - h2)
            w2 = w2 + 9
            h2 = h2 + 6

        for d in range(1720, 1725):
            self.mainMap3[d]=(296 + w2, 684 - h2)
            w2 = w2 + 3
            h2 = h2 + 3

    def main_road_3(self):
        self.makeMainMap3()
        for d in range(len(road.main_road3.lane)):
            if (road.main_road3.lane[d].vehicle == 1):
                (x, y) = self.mainMap3[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()

    def draw_main_road_1(self):
        w = 0
        h = 0
        w1 = 0
        h1 = 0
        w2 = 0
        h2 = 0
        # wszystkie punkty
        for d in range(32):
            w = w + 5
            h = h + 4
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 458 - h, 1, 1))
        for d in range(32, 35):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 457 - h, 1, 1))
        for d in range(35, 38):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 457 - h, 1, 1))
        for d in range(38, 42):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 456 - h, 1, 1))
        for d in range(42, 44):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 453 - h, 1, 1))
        for d in range(44, 48):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 453 - h, 1, 1))
        for d in range(48, 52):
            w = w + 4
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 454 - h, 1, 1))
        for d in range(52, 56):
            w = w + 6
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 455 - h, 1, 1))
        for d in range(56, 59):
            w = w + 7
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(470 + w, 453 - h, 1, 1))
        for d in range(59, 61):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(469 + w, 452 - h, 1, 1))
            # kolejny obrazek
        for d in range(61, 67):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 452 - h, 1, 1))

        for d in range(1628, 1638):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(166 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1638, 1645):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(165 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7

        for d in range(1646, 1650):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(164 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1650, 1655):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(163 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1655, 1660):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(164 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 7
        for d in range(1660, 1665):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(164 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1665, 1670):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(163 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1670, 1675):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(162 + w1, 1019 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 6

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(275, 714, 1, 1))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(290, 684, 1, 1))

        for d in range(1677, 1687):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(292 + w2, 677 - h2, 1, 1))
            w2 = w2 + 2
            h2 = h2 + 5
        for d in range(1687, 1696):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(292 + w2, 677 - h2, 1, 1))
            w2 = w2 + 3
            h2 = h2 + 6
        for d in range(1696, 1706):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(292 + w2, 677 - h2, 1, 1))
            w2 = w2 + 4
            h2 = h2 + 4
        for d in range(1706, 1716):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(292 + w2, 677 - h2, 1, 1))
            w2 = w2 + 5
            h2 = h2 + 4

        for d in range(1716, 1720):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(297 + w2, 672 - h2, 1, 1))
            w2 = w2 + 9
            h2 = h2 + 6

        for d in range(1720, 1725):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(290 + w2, 676 - h2, 1, 1))
            w2 = w2 + 3
            h2 = h2 + 3

    def draw_main_road_2(self):
        w = 0
        h = 0
        w1 = 0
        h1 = 0
        w2 = 0
        h2 = 0
        # wszystkie punkty
        for d in range(32):
            w = w + 5
            h = h + 4
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 462 - h, 1, 1))
        for d in range(32, 35):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 461 - h, 1, 1))
        for d in range(35, 38):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 460 - h, 1, 1))
        for d in range(38, 42):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 459 - h, 1, 1))
        for d in range(42, 44):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 457 - h, 1, 1))
        for d in range(44, 48):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 457 - h, 1, 1))
        for d in range(48, 52):
            w = w + 4
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 458 - h, 1, 1))
        for d in range(52, 56):
            w = w + 6
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 459 - h, 1, 1))
        for d in range(56, 59):
            w = w + 7
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(473 + w, 457 - h, 1, 1))
        for d in range(59, 61):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(472 + w, 456 - h, 1, 1))
            # kolejny obrazek
        for d in range(61, 67):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 456 - h, 1, 1))

        for d in range(1628, 1638):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(169 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1638, 1645):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(168 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7

        for d in range(1646, 1650):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(167 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1650, 1655):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(167 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1655, 1660):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(167 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 7
        for d in range(1660, 1665):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(167 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1665, 1670):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(166 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1670, 1675):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(165 + w1, 1023 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 6

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(278, 718, 1, 1))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(293, 688, 1, 1))

        for d in range(1677, 1687):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(295 + w2, 681 - h2, 1, 1))
            w2 = w2 + 2
            h2 = h2 + 5
        for d in range(1687, 1696):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(295 + w2, 681 - h2, 1, 1))
            w2 = w2 + 3
            h2 = h2 + 6
        for d in range(1696, 1706):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(295 + w2, 681 - h2, 1, 1))
            w2 = w2 + 4
            h2 = h2 + 4
        for d in range(1706, 1716):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(295 + w2, 681 - h2, 1, 1))
            w2 = w2 + 5
            h2 = h2 + 4

        for d in range(1716, 1720):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(300 + w2, 676 - h2, 1, 1))
            w2 = w2 + 9
            h2 = h2 + 6

        for d in range(1720, 1725):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(293 + w2, 680 - h2, 1, 1))
            w2 = w2 + 3
            h2 = h2 + 3

    def draw_main_road_3(self):
        w=0
        h=0
        w1 = 0
        h1 = 0
        w2=0
        h2=0
        # wszystkie punkty
        for d in range(32):
            w=w+5
            h=h+4
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479+w, 466-h, 1, 1))
        for d in range(32, 35):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479+w, 465-h, 1, 1))
        for d in range(35, 38):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 464 - h, 1, 1))
        for d in range(38, 42):
            w = w + 6
            h = h + 3
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 463 - h, 1, 1))
        for d in range(42, 44):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 461 - h, 1, 1))
        for d in range(44, 48):
            w = w + 5
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 462 - h, 1, 1))
        for d in range(48, 52):
            w = w + 4
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 462 - h, 1, 1))
        for d in range(52, 56):
            w = w + 6
            h = h + 2
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 463 - h, 1, 1))
        for d in range(56, 59):
            w = w + 7
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(476 + w, 461 - h, 1, 1))
        for d in range(59, 61):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(475 + w, 460 - h, 1, 1))
            #kolejny obrazek
        for d in range(61, 67):
            w = w + 6
            h = h + 1
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 460 - h, 1, 1))

        for d in range(1628, 1638):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(172 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1638, 1645):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(171 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7

        for d in range(1646, 1650):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(170 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 7
        for d in range(1650, 1655):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(170 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1655, 1660):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(170 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 7
        for d in range(1660, 1665):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(170 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1665, 1670):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(169 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 3
            h1 = h1 + 6
        for d in range(1670, 1675):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(168 + w1, 1027 - h1, 1, 1))
            w1 = w1 + 2
            h1 = h1 + 6

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(281, 722 , 1, 1))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(296, 692, 1, 1))

        for d in range(1677, 1687):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(298 + w2, 685 - h2, 1, 1))
             w2 = w2 + 2
             h2 = h2 + 5
        for d in range(1687, 1696):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(298 + w2, 685 - h2, 1, 1))
             w2 = w2 + 3
             h2 = h2 + 6
        for d in range(1696, 1706):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(298 + w2, 685 - h2, 2, 1))
             w2 = w2 + 4
             h2 = h2 + 4
        for d in range(1706, 1716):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(299 + w2, 685 - h2, 1, 1))
             w2 = w2 + 5
             h2 = h2 + 4

        for d in range(1716, 1720):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(303+ w2, 681 - h2, 1, 1))
             w2 = w2 + 9
             h2 = h2 + 6

        for d in range(1720, 1725):
             pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(296+ w2, 684 - h2, 1, 1))
             w2 = w2 + 3
             h2 = h2 + 3


    def draw_main_road_4(self):
        self.main_road_4=road.main_road4.lane[::-1]

    def draw_main_road_5(self):
        self.makeMap1()
        w = 0
        h = 0
        # wszystkie punkty
        for d in range(24):
            w = w + 5
            h = h + 4
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 466 - h, 1, 1))

    def draw_main_road_6(self):
        self.makeMap1()
        w = 0
        h = 0
        # wszystkie punkty
        for d in range(24):
            w = w + 5
            h = h + 4
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(479 + w, 466 - h, 1, 1))

    """""
                for d in range(len(road.main_road3.lane)):
                    if(road.main_road3.lane[d].vehicle==0):
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.roadMap[d], 1, 1))
                        pygame.display.update()

                pygame.display.update()

                clock.tick(FPS)
    """""

