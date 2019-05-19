import road as r

def print_roads():
    for i in range(12):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 67 ,end='')
        print(r.r4.lane[i].vehicle,end=' ')
        print(r.r5.lane[len(r.r5.lane)-i-1].vehicle)
        
    r.main_road4.print_road(True)
    r.main_road5.print_road(True)
    r.main_road6.print_road(True)        
        
    for i in range(15,19):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 67 ,end='')
        print(r.r4.lane[i].vehicle,end=' ')
        print(r.r5.lane[len(r.r5.lane)-i-1].vehicle)
        
    r.main_road1.print_road()
    r.main_road2.print_road()
    r.main_road3.print_road()
    
    for i in range(22,30):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 33,end='')
        print(r.r3.lane[len(r.r3.lane)-1-(i-20)].vehicle,end='')
        print(' ' * 33 ,end='')
        print(r.r4.lane[i].vehicle)

        
print_roads()