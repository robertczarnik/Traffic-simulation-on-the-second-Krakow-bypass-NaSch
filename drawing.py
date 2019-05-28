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
        self.width = 674
        self.height = 783
        self.mainMap1 = {}
        self.mainMap2 ={}
        self.mainMap3 ={}
        self.cords=[]
        self.mapList=[]
        self.main_road_4=[]
        self.main_road_5=[]
        self.main_road_6=[]
        self.lista=[7,1,17]


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
            bypassImage=pygame.image.load("road/x2.jpg")
            self.screen.blit(bypassImage,(0,0))
            for i in range(len(self.cords)):
                (x,y)=self.cords[i]
                pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(x, y, 2, 2))
            #self.draw_main_road1_pic1()
            #self.draw_main_road2_pic1()
            #self.draw_main_road3_pic1()
            #self.draw_main_road4_pic1()
            #self.draw_main_road5_pic1()
            #self.draw_main_road6_pic1()
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

    def draw_main_road1_pic1(self):
        main_road_1=[(473, 69), (478.25, 64.75), (483.5, 60.5), (488.75, 56.25), (494.0, 52.0), (499.25, 47.75), (504.5, 43.5), (509.75, 39.25), (515.0, 35.0), (520.25, 30.75), (525.5, 26.5), (530.75, 22.25), (536.0, 18.0), (541.25, 13.75), (546.5, 9.5), (551.75, 5.25), (557.0, 1.0)]
        for d in range(17): #len(road.main_road4.lane)
            if (road.main_road1.lane[d].vehicle == 1):
                (x, y) = main_road_1[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()
    def draw_main_road2_pic1(self):
        main_road_2=[(478, 72), (483.3125, 67.6875), (488.625, 63.375), (493.9375, 59.0625), (499.25, 54.75), (504.5625, 50.4375), (509.875, 46.125), (515.1875, 41.8125), (520.5, 37.5), (525.8125, 33.1875), (531.125, 28.875), (536.4375, 24.5625), (541.75, 20.25), (547.0625, 15.9375), (552.375, 11.625), (557.6875, 7.3125), (563.0, 3.0)]
        for d in range(17): #len(road.main_road4.lane)
            if (road.main_road2.lane[d].vehicle == 1):
                (x, y) = main_road_2[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()
    def draw_main_road3_pic1(self):
        main_road_3=[(483, 78), (488.4375, 73.375), (493.875, 68.75), (499.3125, 64.125), (504.75, 59.5), (510.1875, 54.875), (515.625, 50.25), (521.0625, 45.625), (526.5, 41.0), (531.9375, 36.375), (537.375, 31.75), (542.8125, 27.125), (548.25, 22.5), (553.6875, 17.875), (559.125, 13.25), (564.5625, 8.625), (570.0, 4.0)]
        for d in range(17): #len(road.main_road4.lane)
            if (road.main_road3.lane[d].vehicle == 1):
                (x, y) = main_road_3[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()
    def draw_main_road4_pic1(self):
        main_road_4=[(450, 50), (443.3333333333333, 55.0), (436.66666666666663, 60.0), (429.99999999999994, 65.0), (423.33333333333326, 70.0), (416.6666666666666, 75.0), (409.9999999999999, 80.0), (400.0, 88.0), (396.0, 93.0), (391.375, 97.375), (386.75, 101.75), (382.125, 106.125), (377.5, 110.5), (372.875, 114.875), (368.25, 119.25), (363.625, 123.625), (359.0, 128.0), (354.375, 132.375), (349.75, 136.75), (345.125, 141.125), (340.5, 145.5), (335.875, 149.875), (331.25, 154.25), (326.625, 158.625), (322.0, 163.0), (319.0, 167.0), (315.0, 173.0), (311.94117647058823, 179.47058823529412), (308.88235294117646, 185.94117647058823), (305.8235294117647, 192.41176470588235), (302.7647058823529, 198.88235294117646), (299.70588235294116, 205.35294117647058), (296.6470588235294, 211.8235294117647), (293.5882352941176, 218.2941176470588), (290.52941176470586, 224.76470588235293), (287.4705882352941, 231.23529411764704), (284.4117647058823, 237.70588235294116), (281.35294117647055, 244.17647058823528), (278.2941176470588, 250.6470588235294), (275.235294117647, 257.11764705882354), (272.17647058823525, 263.5882352941177), (269.1176470588235, 270.0588235294118), (266.0588235294117, 276.52941176470597), (262.99999999999994, 283.0000000000001), (260.0, 290.0), (255.0, 302.0), (252.5625, 307.4375), (250.125, 312.875), (247.6875, 318.3125), (245.25, 323.75), (242.8125, 329.1875), (240.375, 334.625), (237.9375, 340.0625), (235.5, 345.5), (233.0625, 350.9375), (230.625, 356.375), (228.1875, 361.8125), (225.75, 367.25), (223.3125, 372.6875), (220.875, 378.125), (218.4375, 383.5625), (216.0, 389.0), (213.9375, 393.6875), (211.875, 398.375), (209.8125, 403.0625), (207.75, 407.75), (205.6875, 412.4375), (203.625, 417.125), (201.5625, 421.8125), (199.5, 426.5), (197.4375, 431.1875), (195.375, 435.875), (193.3125, 440.5625), (191.25, 445.25), (189.1875, 449.9375), (187.125, 454.625), (185.0625, 459.3125), (183.0, 464.0), (180.23529411764707, 472.47058823529414), (177.47058823529414, 480.9411764705883), (174.70588235294122, 489.41176470588243), (171.9411764705883, 497.8823529411766), (169.17647058823536, 506.3529411764707), (166.41176470588243, 514.8235294117649), (163.6470588235295, 523.294117647059), (160.88235294117658, 531.7647058823532), (158.11764705882365, 540.2352941176473), (155.35294117647072, 548.7058823529414), (152.5882352941178, 557.1764705882356), (149.82352941176487, 565.6470588235297), (147.05882352941194, 574.1176470588239), (144.294117647059, 582.588235294118), (141.52941176470608, 591.0588235294122), (138.76470588235316, 599.5294117647063), (136.00000000000023, 608.0000000000005), (134.0, 614.0), (130.0, 621.0), (126.0, 632.0), (126.0, 641.0), (126.0, 646.0), (124.14285714285714, 655.5), (122.28571428571428, 665.0), (120.42857142857142, 674.5), (118.57142857142856, 684.0), (116.7142857142857, 693.5), (114.85714285714283, 703.0), (112.99999999999997, 712.5), (111.14285714285711, 722.0), (109.28571428571425, 731.5), (107.42857142857139, 741.0), (105.57142857142853, 750.5), (103.71428571428567, 760.0), (101.8571428571428, 769.5), (99.99999999999994, 779.0)]
        for d in range(114): #len(road.main_road4.lane)
            if (road.main_road4.lane[d].vehicle == 1):
                (x, y) = main_road_4[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()

    def draw_main_road5_pic1(self):
        main_road_5=[(453, 51), (446.5, 56.333333333333336), (440.0, 61.66666666666667), (433.5, 67.0), (427.0, 72.33333333333333), (420.5, 77.66666666666666), (414.0, 82.99999999999999), (405.0, 90.0), (401.0, 96.0), (396.25, 100.3125), (391.5, 104.625), (386.75, 108.9375), (382.0, 113.25), (377.25, 117.5625), (372.5, 121.875), (367.75, 126.1875), (363.0, 130.5), (358.25, 134.8125), (353.5, 139.125), (348.75, 143.4375), (344.0, 147.75), (339.25, 152.0625), (334.5, 156.375), (329.75, 160.6875), (325.0, 165.0), (322.0, 169.0), (319.0, 174.0), (315.94117647058823, 180.7058823529412), (312.88235294117646, 187.41176470588238), (309.8235294117647, 194.11764705882356), (306.7647058823529, 200.82352941176475), (303.70588235294116, 207.52941176470594), (300.6470588235294, 214.23529411764713), (297.5882352941176, 220.94117647058832), (294.52941176470586, 227.6470588235295), (291.4705882352941, 234.3529411764707), (288.4117647058823, 241.05882352941188), (285.35294117647055, 247.76470588235307), (282.2941176470588, 254.47058823529426), (279.235294117647, 261.1764705882354), (276.17647058823525, 267.8823529411766), (273.1176470588235, 274.58823529411774), (270.0588235294117, 281.2941176470589), (266.99999999999994, 288.00000000000006), (263.0, 295.0), (259.0, 305.0), (256.625, 310.3125), (254.25, 315.625), (251.875, 320.9375), (249.5, 326.25), (247.125, 331.5625), (244.75, 336.875), (242.375, 342.1875), (240.0, 347.5), (237.625, 352.8125), (235.25, 358.125), (232.875, 363.4375), (230.5, 368.75), (228.125, 374.0625), (225.75, 379.375), (223.375, 384.6875), (221.0, 390.0), (218.75, 395.0625), (216.5, 400.125), (214.25, 405.1875), (212.0, 410.25), (209.75, 415.3125), (207.5, 420.375), (205.25, 425.4375), (203.0, 430.5), (200.75, 435.5625), (198.5, 440.625), (196.25, 445.6875), (194.0, 450.75), (191.75, 455.8125), (189.5, 460.875), (187.25, 465.9375), (185.0, 471.0), (182.35294117647058, 479.1764705882353), (179.70588235294116, 487.3529411764706), (177.05882352941174, 495.5294117647059), (174.41176470588232, 503.7058823529412), (171.7647058823529, 511.8823529411765), (169.11764705882348, 520.0588235294118), (166.47058823529406, 528.2352941176471), (163.82352941176464, 536.4117647058823), (161.17647058823522, 544.5882352941176), (158.5294117647058, 552.7647058823528), (155.88235294117638, 560.9411764705881), (153.23529411764696, 569.1176470588233), (150.58823529411754, 577.2941176470586), (147.94117647058812, 585.4705882352938), (145.2941176470587, 593.647058823529), (142.64705882352928, 601.8235294117643), (139.99999999999986, 609.9999999999995), (137.0, 616.0), (136.0, 624.0), (132.0, 632.0), (131.0, 640.0), (131.0, 649.0), (129.21428571428572, 658.2857142857143), (127.42857142857143, 667.5714285714287), (125.64285714285714, 676.857142857143), (123.85714285714285, 686.1428571428573), (122.07142857142856, 695.4285714285717), (120.28571428571426, 704.714285714286), (118.49999999999997, 714.0000000000003), (116.71428571428568, 723.2857142857147), (114.92857142857139, 732.571428571429), (113.1428571428571, 741.8571428571433), (111.3571428571428, 751.1428571428577), (109.57142857142851, 760.428571428572), (107.78571428571422, 769.7142857142863), (105.99999999999993, 779.0000000000007)]
        for d in range(114): #len(road.main_road4.lane)
            if (road.main_road5.lane[d].vehicle == 1):
                (x, y) = main_road_5[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()

    def draw_main_road6_pic1(self):
        main_road_6=[(458, 55), (451.6666666666667, 60.0), (445.33333333333337, 65.0), (439.00000000000006, 70.0), (432.66666666666674, 75.0), (426.3333333333334, 80.0), (420.0000000000001, 85.0), (414.0, 92.0), (409.0, 96.0), (404.0625, 100.625), (399.125, 105.25), (394.1875, 109.875), (389.25, 114.5), (384.3125, 119.125), (379.375, 123.75), (374.4375, 128.375), (369.5, 133.0), (364.5625, 137.625), (359.625, 142.25), (354.6875, 146.875), (349.75, 151.5), (344.8125, 156.125), (339.875, 160.75), (334.9375, 165.375), (330.0, 170.0), (327.0, 175.0), (325.0, 179.0), (321.94117647058823, 185.64705882352942), (318.88235294117646, 192.29411764705884), (315.8235294117647, 198.94117647058826), (312.7647058823529, 205.58823529411768), (309.70588235294116, 212.2352941176471), (306.6470588235294, 218.88235294117652), (303.5882352941176, 225.52941176470594), (300.52941176470586, 232.17647058823536), (297.4705882352941, 238.82352941176478), (294.4117647058823, 245.4705882352942), (291.35294117647055, 252.11764705882362), (288.2941176470588, 258.76470588235304), (285.235294117647, 265.41176470588243), (282.17647058823525, 272.0588235294118), (279.1176470588235, 278.7058823529412), (276.0588235294117, 285.3529411764706), (272.99999999999994, 292.0), (267.0, 300.0), (263.0, 308.0), (260.9375, 312.6875), (258.875, 317.375), (256.8125, 322.0625), (254.75, 326.75), (252.6875, 331.4375), (250.625, 336.125), (248.5625, 340.8125), (246.5, 345.5), (244.4375, 350.1875), (242.375, 354.875), (240.3125, 359.5625), (238.25, 364.25), (236.1875, 368.9375), (234.125, 373.625), (232.0625, 378.3125), (230.0, 383.0), (227.6875, 388.1875), (225.375, 393.375), (223.0625, 398.5625), (220.75, 403.75), (218.4375, 408.9375), (216.125, 414.125), (213.8125, 419.3125), (211.5, 424.5), (209.1875, 429.6875), (206.875, 434.875), (204.5625, 440.0625), (202.25, 445.25), (199.9375, 450.4375), (197.625, 455.625), (195.3125, 460.8125), (193.0, 466.0), (190.47058823529412, 474.2352941176471), (187.94117647058823, 482.47058823529414), (185.41176470588235, 490.7058823529412), (182.88235294117646, 498.9411764705883), (180.35294117647058, 507.17647058823536), (177.8235294117647, 515.4117647058824), (175.2941176470588, 523.6470588235295), (172.76470588235293, 531.8823529411766), (170.23529411764704, 540.1176470588236), (167.70588235294116, 548.3529411764707), (165.17647058823528, 556.5882352941178), (162.6470588235294, 564.8235294117649), (160.1176470588235, 573.0588235294119), (157.58823529411762, 581.294117647059), (155.05882352941174, 589.5294117647061), (152.52941176470586, 597.7647058823532), (149.99999999999997, 606.0000000000002), (143.0, 613.0), (140.0, 625.0), (136.0, 640.0), (137.0, 648.0), (135.0, 659.0), (133.35714285714286, 667.5714285714286), (131.71428571428572, 676.1428571428571), (130.07142857142858, 684.7142857142857), (128.42857142857144, 693.2857142857142), (126.7857142857143, 701.8571428571428), (125.14285714285717, 710.4285714285713), (123.50000000000003, 718.9999999999999), (121.85714285714289, 727.5714285714284), (120.21428571428575, 736.142857142857), (118.57142857142861, 744.7142857142856), (116.92857142857147, 753.2857142857141), (115.28571428571433, 761.8571428571427), (113.6428571428572, 770.4285714285712), (112.00000000000006, 778.9999999999998)]
        for d in range(114): #len(road.main_road4.lane)
            if (road.main_road5.lane[d].vehicle == 1):
                (x, y) = main_road_6[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()
    def draw_main_road1_pic2(self):
        main_road_6=[(458, 55), (451.6666666666667, 60.0), (445.33333333333337, 65.0), (439.00000000000006, 70.0), (432.66666666666674, 75.0), (426.3333333333334, 80.0), (420.0000000000001, 85.0), (414.0, 92.0), (409.0, 96.0), (404.0625, 100.625), (399.125, 105.25), (394.1875, 109.875), (389.25, 114.5), (384.3125, 119.125), (379.375, 123.75), (374.4375, 128.375), (369.5, 133.0), (364.5625, 137.625), (359.625, 142.25), (354.6875, 146.875), (349.75, 151.5), (344.8125, 156.125), (339.875, 160.75), (334.9375, 165.375), (330.0, 170.0), (327.0, 175.0), (325.0, 179.0), (321.94117647058823, 185.64705882352942), (318.88235294117646, 192.29411764705884), (315.8235294117647, 198.94117647058826), (312.7647058823529, 205.58823529411768), (309.70588235294116, 212.2352941176471), (306.6470588235294, 218.88235294117652), (303.5882352941176, 225.52941176470594), (300.52941176470586, 232.17647058823536), (297.4705882352941, 238.82352941176478), (294.4117647058823, 245.4705882352942), (291.35294117647055, 252.11764705882362), (288.2941176470588, 258.76470588235304), (285.235294117647, 265.41176470588243), (282.17647058823525, 272.0588235294118), (279.1176470588235, 278.7058823529412), (276.0588235294117, 285.3529411764706), (272.99999999999994, 292.0), (267.0, 300.0), (263.0, 308.0), (260.9375, 312.6875), (258.875, 317.375), (256.8125, 322.0625), (254.75, 326.75), (252.6875, 331.4375), (250.625, 336.125), (248.5625, 340.8125), (246.5, 345.5), (244.4375, 350.1875), (242.375, 354.875), (240.3125, 359.5625), (238.25, 364.25), (236.1875, 368.9375), (234.125, 373.625), (232.0625, 378.3125), (230.0, 383.0), (227.6875, 388.1875), (225.375, 393.375), (223.0625, 398.5625), (220.75, 403.75), (218.4375, 408.9375), (216.125, 414.125), (213.8125, 419.3125), (211.5, 424.5), (209.1875, 429.6875), (206.875, 434.875), (204.5625, 440.0625), (202.25, 445.25), (199.9375, 450.4375), (197.625, 455.625), (195.3125, 460.8125), (193.0, 466.0), (190.47058823529412, 474.2352941176471), (187.94117647058823, 482.47058823529414), (185.41176470588235, 490.7058823529412), (182.88235294117646, 498.9411764705883), (180.35294117647058, 507.17647058823536), (177.8235294117647, 515.4117647058824), (175.2941176470588, 523.6470588235295), (172.76470588235293, 531.8823529411766), (170.23529411764704, 540.1176470588236), (167.70588235294116, 548.3529411764707), (165.17647058823528, 556.5882352941178), (162.6470588235294, 564.8235294117649), (160.1176470588235, 573.0588235294119), (157.58823529411762, 581.294117647059), (155.05882352941174, 589.5294117647061), (152.52941176470586, 597.7647058823532), (149.99999999999997, 606.0000000000002), (143.0, 613.0), (140.0, 625.0), (136.0, 640.0), (137.0, 648.0), (135.0, 659.0), (133.35714285714286, 667.5714285714286), (131.71428571428572, 676.1428571428571), (130.07142857142858, 684.7142857142857), (128.42857142857144, 693.2857142857142), (126.7857142857143, 701.8571428571428), (125.14285714285717, 710.4285714285713), (123.50000000000003, 718.9999999999999), (121.85714285714289, 727.5714285714284), (120.21428571428575, 736.142857142857), (118.57142857142861, 744.7142857142856), (116.92857142857147, 753.2857142857141), (115.28571428571433, 761.8571428571427), (113.6428571428572, 770.4285714285712), (112.00000000000006, 778.9999999999998)]
        for d in range(114): #len(road.main_road4.lane)
            if (road.main_road5.lane[d].vehicle == 1):
                (x, y) = main_road_6[d]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 2, 2))
                pygame.display.update()