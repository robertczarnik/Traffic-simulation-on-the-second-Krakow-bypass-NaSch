import road as r

def print_roads():
    for i in range(12):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 67 ,end='')
        print(r.r4.lane[i].vehicle,end=' ')
        print(r.r5.lane[len(r.r5.lane)-i-1].vehicle,end='')
        print(' ' * 25 ,end='')
        print(r.r6.lane[i].vehicle)

        
        
    r.main_road4.print_road(1676,1748,True)
    r.main_road5.print_road(1676,1748,True)
    r.main_road6.print_road(1676,1748,True)        
        
    for i in range(15,19):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 67 ,end='')
        print(r.r4.lane[i].vehicle,end=' ')
        print(r.r5.lane[len(r.r5.lane)-i-1].vehicle,end='')
        print(' ' * 25 ,end='')
        print(r.r6.lane[i].vehicle)

        
    r.main_road1.print_road(0,70)
    r.main_road2.print_road(0,70)
    r.main_road3.print_road(0,70)
    
    for i in range(22,34):
        print(' ' * 48,end='')
        print(r.r1.lane[i].vehicle,end=' ')
        print(r.r2.lane[len(r.r2.lane)-i-1].vehicle,end='')
        print(' ' * 33,end='')
        print(r.r3.lane[len(r.r3.lane)-1-(i-22)].vehicle,end='')
        print(' ' * 33 ,end='')
        print(r.r4.lane[i].vehicle,end='')
        print(' ' * 27 ,end='')
        print(r.r6.lane[i].vehicle)


      
print_roads()