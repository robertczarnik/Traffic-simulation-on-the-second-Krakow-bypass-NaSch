#0-wolna komorka 1-zajeta komorka 2-czerwone swiatlo 3-koniec drogi(koniecznosc zmiany pasa)

class Road(object):
    def __init__(self,lane,l_road=None,r_road=None):
        self.lane=lane
        self.l_road=l_road
        self.r_road=r_road
        self.other_roads=[] #roads that cross this road
               
    def print_road(self,reverse=False):
        if(not reverse):
            for i in range(70):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')
        else: #droga z prawej do lewej
            for i in range(len(self.lane)-1,-1,-1):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle , self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')


class Cell(object):
    def __init__(self,vehicle,crossroads=False,crossing_id=None,index=None,speed_limit=4):
        self.vehicle=vehicle
        self.crossroads=crossroads
        self.crossing_id=crossing_id
        self.index=index
        self.speed_limit=speed_limit 
    
    
def traffic_lights_management(traffic_lights_timer):
    if(traffic_lights_timer==60):
        traffic_lights_timer=0
    
    if(traffic_lights_timer==0):
        traffic_ligths1(1)
     
    if(traffic_lights_timer==17):
        traffic_ligths1(2)    
        
    elif(traffic_lights_timer==20):
        traffic_ligths1(3)
        
    elif(traffic_lights_timer==35):
        traffic_ligths1(4)
        
    elif(traffic_lights_timer==45):
        traffic_ligths1(5)
        
    traffic_lights_timer+=1
        
        
def traffic_ligths1(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[23].vehicle=0
        main_road2.lane[23].vehicle=0
        main_road3.lane[23].vehicle=0
        main_road4.lane[28].vehicle=0
        main_road5.lane[28].vehicle=0
        main_road6.lane[28].vehicle=0
        r1.lane[18].vehicle=2
        r2.lane[18].vehicle=2
        r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
    elif(x==2):
        main_road1.lane[23].vehicle=2
        main_road2.lane[23].vehicle=2
        main_road3.lane[23].vehicle=2
        main_road4.lane[28].vehicle=2
        main_road5.lane[28].vehicle=2
        main_road6.lane[28].vehicle=2
    elif(x==3):
        r1.lane[18].vehicle=0
        r2.lane[18].vehicle=0
    elif(x==4):
        r1.lane[11].vehicle=0
        r2.lane[11].vehicle=0
    elif(x==5):
        r1.lane[11].vehicle=2
        r2.lane[11].vehicle=2
        
    
def add_none_to_other_roads(roads_list):
    if(main_road1 not in roads_list):
        main_road1.other_roads.append(None)
    if(main_road2 not in roads_list):
        main_road2.other_roads.append(None)
    if(main_road3 not in roads_list):
        main_road3.other_roads.append(None)
    if(main_road4 not in roads_list):
        main_road4.other_roads.append(None)
    if(main_road5 not in roads_list):
        main_road5.other_roads.append(None)
    if(main_road6 not in roads_list):
        main_road6.other_roads.append(None)
            
def road_creator(roads_list ,roads_param , crossing_list , template , space_between_roads=0 , one_lane_closed=0):
    road = []
    len_roads=12
    
    if(template == 1): #wjazd
        param = [len_roads + one_lane_closed]
        road = [Cell(0) for i in range(len_roads+1+one_lane_closed)] #+1 bo wjazd
        road=Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
    
    elif(template == 2): #wyjazd
        param = [0]
        road = [Cell(0) for i in range(len_roads+1)] #+1 bo wyjazd
        road=Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0]] 
        
    elif(template == 3): #pelna droga
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1,len_roads+2+space_between_roads+2,len_roads+2+space_between_roads+3]
        road = [Cell(0) for i in range(len_roads*2+space_between_roads+6)] #pelna droga
        road = Road(road)
        
        if(roads_list[0]!=None): 
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[0])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[0])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[1])
            roads_list[3].other_roads.append(road)
            
        if(roads_list[4]!=None):
            (roads_list[4]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[4])
            road.lane[param[4]]=Cell(0,True,5,roads_param[1])
            roads_list[4].other_roads.append(road)
            
        if(roads_list[5]!=None):
            (roads_list[5]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[5])
            road.lane[param[5]]=Cell(0,True,6,roads_param[1])
            roads_list[5].other_roads.append(road)
        
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3],roads_list[4],roads_list[5]]
    
    elif(template == 4): #niepelna droga wjazdowa
        param = [len_roads,len_roads+1,len_roads+2,len_roads+2+space_between_roads+1]
        road = [Cell(0) for i in range(len_roads+space_between_roads+4)] #niepelna droga
        road = Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[0])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[0])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[1])
            roads_list[3].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3]]

    elif(template == 5): #niepelna droga wyjazdowa
        param = [0,1+space_between_roads,2+space_between_roads,3+space_between_roads]
        road = [Cell(0) for i in range(len_roads+space_between_roads+4)] #niepelna droga
        road = Road(road)
        
        if(roads_list[0]!=None):
            (roads_list[0]).lane[roads_param[0]]=Cell(0,True,crossing_list[0],param[0])
            road.lane[param[0]]=Cell(0,True,1,roads_param[0])
            roads_list[0].other_roads.append(road)
            
        if(roads_list[1]!=None):
            (roads_list[1]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[1])
            road.lane[param[1]]=Cell(0,True,2,roads_param[1])
            roads_list[1].other_roads.append(road)
            
        if(roads_list[2]!=None):
            (roads_list[2]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[2])
            road.lane[param[2]]=Cell(0,True,3,roads_param[1])
            roads_list[2].other_roads.append(road)
            
        if(roads_list[3]!=None):
            (roads_list[3]).lane[roads_param[1]]=Cell(0,True,crossing_list[1],param[3])
            road.lane[param[3]]=Cell(0,True,4,roads_param[1])
            roads_list[3].other_roads.append(road)
            
        add_none_to_other_roads(roads_list)
        road.other_roads=[roads_list[0],roads_list[1],roads_list[2],roads_list[3]]
        
    return road #zwracam powstałą droge
    

###representing roads###
#main roads
main_road4 = [Cell(0) for i in range(1725)]
main_road5 = [Cell(0) for i in range(1725)]
main_road6 = [Cell(0) for i in range(1725)]
main_road1 = [Cell(0) for i in range(1725)]
main_road2 = [Cell(0) for i in range(1725)]
main_road3 = [Cell(0) for i in range(1725)]
#for i in range(455):
    #main_road3.append(Cell(3))
main_road1 = Road(main_road1)
main_road2 = Road(main_road2)
main_road3 = Road(main_road3)
main_road4 = Road(main_road4)
main_road5 = Road(main_road5)
main_road6 = Road(main_road6)

main_road1.r_road=main_road2
main_road2.l_road=main_road1
main_road2.r_road=main_road3
main_road3.l_road=main_road2
main_road4.l_road=main_road5
main_road5.r_road=main_road4
main_road5.l_road=main_road6
main_road6.r_road=main_road5  
#--

z_gory         = [None,None,None,main_road1,main_road2,main_road3]
z_dolu         = [main_road3,main_road2,main_road1,None,None,None]
wjazd_z_gory   = [None,None,None,main_road1]
wjazd_z_dolu   = [main_road3,main_road2,main_road1,None]
zjazd_do_gory  = [main_road1,None,None,None] 
zjazd_do_dolu  = [None,main_road1,main_road2,main_road3]

#other roads

# 3 lanes
r1   = road_creator(z_gory       ,[None,24],[None,1],3,4)
r2   = road_creator(z_dolu       ,[25,None],[2,None],3,4)
r3   = road_creator([main_road3] ,[42],[3],1)
r4   = road_creator(z_gory       ,[None,59],[None,4],3,4)
r5   = road_creator(zjazd_do_gory,[60,None],[5,None],5,4)
r6   = road_creator(z_gory       ,[None,73],[None,6],3,4)
r7   = road_creator(wjazd_z_gory ,[None,74],[None,7],4,4)
r8   = road_creator(z_dolu       ,[75,None],[8,None],3,4)
r9   = road_creator([main_road3] ,[76],[9],1)
r10  = road_creator([None]       ,[None],[10],2)
r11  = road_creator([None]       ,[None],[11],2)
r12  = road_creator([None]       ,[None],[12],1)
r13  = road_creator(wjazd_z_gory ,[None,102],[None,13],4,1)
r14  = road_creator(zjazd_do_gory,[104,None],[14,None],5,1)
r15  = road_creator([None]       ,[None],[15],2,1)
r16  = road_creator([None]       ,[None],[16],1)
r17  = road_creator([None]       ,[None],[17],1)
r18  = road_creator([main_road3] ,[142],[18],2)

# 2 lanes
r19  = road_creator([None]       ,[None],[19],2)
r20  = road_creator([main_road2] ,[168],[20],1)
r21  = road_creator([None]       ,[None],[21],1)
r22  = road_creator([None]       ,[None],[22],2)
r23  = road_creator([main_road2] ,[168],[23],2)
r24  = road_creator([main_road2] ,[168],[24],2)
r25  = road_creator([None]       ,[None],[25],1)
r26  = road_creator([None]       ,[None],[26],1)
r27  = road_creator([main_road1] ,[218],[27],1)
r28  = road_creator([main_road2] ,[219],[28],1)
r29  = road_creator([None]       ,[None],[29],2)
r30  = road_creator([None]       ,[None],[30],1)
r31  = road_creator([main_road2] ,[187],[31],2)
r32  = road_creator([main_road2] ,[371],[32],1)
r33  = road_creator([None]       ,[None],[33],2)
r34  = road_creator([main_road2] ,[372],[34],2)
r35  = road_creator(wjazd_z_gory ,[None,375],[None,35],4)
r36  = road_creator(z_dolu       ,[376,None],[36,None],3)  
r37  = road_creator([None]       ,[None],[37],2)
r38  = road_creator([main_road2] ,[388],[38],2)
r39  = road_creator([None]       ,[None],[39],1)
r40  = road_creator([None]       ,[None],[40],2)
r41  = road_creator([main_road2] ,[425],[41],1)

# 3 lanes
r42  = road_creator(wjazd_z_gory ,[None,436],[None,42],4,4)
r43  = road_creator(wjazd_z_gory ,[None,437],[None,43],4,4)
r44  = road_creator([None]       ,[None],[44],2)
r45  = road_creator([None]       ,[None],[45],2)
r46  = road_creator([None]       ,[None],[46],1)
r47  = road_creator([None]       ,[None],[47],1)
r48  = road_creator([None]       ,[None],[48],2)
r49  = road_creator([None]       ,[None],[49],2)
r50  = road_creator([main_road3] ,[448],[50],2)
r51  = road_creator(wjazd_z_dolu ,[455,None],[51,None],4,4)
r52  = road_creator(wjazd_z_dolu ,[456,None],[52,None],4,4)
r53  = road_creator([None]       ,[None],[53],1)
r54  = road_creator([None]       ,[None],[54],2)
r55  = road_creator([main_road3] ,[530],[55],1)
r56  = road_creator([None]       ,[None],[56],1)
r57  = road_creator(z_gory       ,[None,565],[None,57],3)
r58  = road_creator(z_gory       ,[None,566],[None,58],3)
r59  = road_creator(z_dolu       ,[573,None],[59,None],3)
r60  = road_creator(z_dolu       ,[574,None],[60,None],3)
r61  = road_creator([main_road3] ,[575],[61],1)

# 2 lanes
r62  = road_creator([None]       ,[None],[62],2)
r63  = road_creator([None]       ,[None],[63],1)
r64  = road_creator([main_road2] ,[618],[64],2)
r65  = road_creator([main_road2] ,[677],[65],2)
r66  = road_creator([main_road2] ,[688],[66],1)
r67  = road_creator([None]       ,[None],[67],2)
r68  = road_creator([None]       ,[None],[68],1)
r69  = road_creator(z_gory       ,[None,744],[None,69],3)
r70  = road_creator(wjazd_z_gory ,[None,745],[None,70],4)
r71  = road_creator(wjazd_z_dolu ,[745,None],[71,None],4)
r72  = road_creator(z_dolu       ,[746,None],[72],3)
r73  = road_creator(zjazd_do_gory,[811,None],[73,None],5)
r74  = road_creator(zjazd_do_gory,[812,None],[74,None],5)
r75  = road_creator(wjazd_z_gory ,[None,815],[None,75],4)
r76  = road_creator(wjazd_z_gory ,[None,816],[None,76],4)
r77  = road_creator([None]       ,[None],[77],2)
r78  = road_creator([None]       ,[None],[78],1)
r79  = road_creator([main_road2] ,[832],[79],2)
r80  = road_creator([main_road2] ,[833],[80],1)
r81  = road_creator([None]       ,[None],[81],2)
r82  = road_creator([None]       ,[None],[82],1)
r83  = road_creator([main_road2] ,[840],[83],2)
r84  = road_creator([main_road2] ,[851],[84],2)
r85  = road_creator([main_road2] ,[852],[85],1)

# 3 lanes
r86  = road_creator([main_road2] ,[861],[86],2)
r87  = road_creator([main_road2] ,[871],[87],1)
r88  = road_creator([main_road1] ,[904],[88],1)
r89  = road_creator([main_road1] ,[905],[89],1)
r90  = road_creator([None]       ,[None],[90],2)
r91  = road_creator([main_road1] ,[919],[91],2)
r92  = road_creator(z_gory       ,[None,933],[None,92],3)
r93  = road_creator(z_dolu       ,[934,None],[93,None],3)

# 2 lanes
r94  = road_creator([main_road1] ,[1084],[94],2)
r95  = road_creator([main_road1] ,[1085],[95],2)
r96  = road_creator([main_road2] ,[1091],[96],1)
r97  = road_creator([main_road2] ,[1092],[97],2)
r98  = road_creator([main_road2] ,[1100],[98],1)
r99  = road_creator([main_road2] ,[1101],[99],2)
r100 = road_creator([None]       ,[None],[100],1)
r101 = road_creator([None]       ,[None],[101],1)
r102 = road_creator([None]       ,[None],[102],1)
r103 = road_creator([None]       ,[None],[103],2)
r104 = road_creator([None]       ,[None],[104],2)
r105 = road_creator([None]       ,[None],[105],2)
r106 = road_creator([None]       ,[None],[106],1)
r107 = road_creator([None]       ,[None],[107],1)
r108 = road_creator(z_gory       ,[None,1164],[None,108],3)
r109 = road_creator(z_gory       ,[None,1165],[None,109],3)
r110 = road_creator(z_dolu       ,[1170,None],[110,None],3)
r111 = road_creator(z_dolu       ,[1171,None],[111,None],3)
r112 = road_creator([main_road2] ,[1171],[112],1)
r113 = road_creator([main_road2] ,[1224],[113],2)
r114 = road_creator([main_road2] ,[1234],[114],2)
r115 = road_creator([main_road2] ,[1235],[115],1)
r116 = road_creator([main_road2] ,[1268],[116],2)
r117 = road_creator([main_road2] ,[1273],[117],1)

# 3 lanes
r118 = road_creator([main_road3] ,[1309],[118],2)
r119 = road_creator([main_road3] ,[1313],[119],1)
r120 = road_creator([None]       ,[None],[120],1)
r121 = road_creator([None]       ,[None],[121],2)
r122 = road_creator([main_road3] ,[1333],[122],2)
r123 = road_creator([main_road3] ,[1334],[123],2)
r124 = road_creator([None]       ,[None],[124],2)
r125 = road_creator([None]       ,[None],[125],2)
r126 = road_creator([main_road3] ,[1386],[126],1)
r127 = road_creator([main_road3] ,[1387],[127],1)
r128 = road_creator([None]       ,[None],[128],1)
r129 = road_creator([None]       ,[None],[129],1)
r130 = road_creator([main_road3] ,[1408],[130],2)
r131 = road_creator([main_road3] ,[1409],[131],1)
r132 = road_creator([None]       ,[None],[132],2)
r133 = road_creator([None]       ,[None],[133],1)
r134 = road_creator(z_gory       ,[None,1463],[None,134],3)
r135 = road_creator(z_dolu       ,[1464,None],[135,None],3)
r136 = road_creator([main_road3] ,[1465],[136],1)
r137 = road_creator([None]       ,[None],[137],1)
r138 = road_creator([None]       ,[None],[138],2)
r139 = road_creator([None]       ,[None],[139],1)
r140 = road_creator([main_road3] ,[1529],[140],1)
r141 = road_creator([main_road3] ,[1575],[141],2)
r142 = road_creator([main_road3] ,[1574],[142],1)
r143 = road_creator([None]       ,[None],[143],1)
r144 = road_creator([None]       ,[None],[144],2)
r145 = road_creator([None]       ,[None],[145],1)
r146 = road_creator(wjazd_z_gory ,[None,1597],[None,146],4)
r147 = road_creator(zjazd_do_gory,[1598,None],[147,None],5)
r148 = road_creator([None]       ,[None],[148],1)
r149 = road_creator([None]       ,[None],[149],1)
r150 = road_creator(z_gory       ,[None,1627],[None,150],3)
r151 = road_creator(z_dolu       ,[1628,None],[151,None],3)
r152 = road_creator(z_dolu       ,[1629,None],[152,None],3)
r153 = road_creator([None]       ,[None],[153],2)
r154 = road_creator([main_road3] ,[1646],[154],1)
r155 = road_creator([None]       ,[None],[155],1)
r156 = road_creator(z_gory       ,[None,1676],[None,156],3)
r157 = road_creator(z_dolu       ,[1677,None],[157,None],3)
r158 = road_creator(zjazd_do_gory,[1697,None],[158,None],5)
r159 = road_creator([None]       ,[None],[159],1)
r160 = road_creator([main_road4] ,[24],[160],2)
r161 = road_creator(z_gory       ,[None,1717],[None,161],3)
r162 = road_creator(wjazd_z_gory ,[None,1718],[None,162],4)
r163 = road_creator(z_dolu       ,[1719,None],[163,None],3)
r164 = road_creator([main_road3] ,[1720],[164],1)


for i in range(len(main_road4.lane)):
    if(main_road4.lane[i].crossing_id!=None):
        print(main_road4.lane[i].crossing_id)

   
