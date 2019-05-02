#if car checks a Cell and turn_left or turn_right is True then can move one Cell forward and change its direction
#right_lane and left_lane means that on this side is another lane
class Cell(object): #false if doesn't exist (status => 0-empty 1-occupied) 
    def __init__(self,status=0,left_lane=False,right_lane=False,turn_left=False,turn_right=False):
        self.status=status
        self.left_lane=left_lane
        self.right_lane=right_lane
        self.turn_left=turn_left
        self.turn_right=turn_right


#get 2-dimensional array that represents the second Krakow bypass
def getRoad():
    row = 22
    col = 55
    road = [['x'] * col for i in range(row)]
    
    for r in range(22):
        if((r>5 and r<9) or(r>12 and r<16)):
            for c in range(54):
                if(r==7 or r==14):
                    road[r][c]=Cell(left_lane=True,right_lane=True)
                elif(r==6 or r==15):
                    road[r][c]=Cell(left_lane=True)
                else:
                    road[r][c]=Cell(right_lane=True)
            
    # --- crossing no.1 --- 
    for r in range(22):
        for c in range(24,26):
            road[r][c]=Cell()
            
    road[5][24]=Cell(turn_right=True)
    road[6][26]=Cell(turn_right=True)
    road[8][25]=Cell(turn_left=True)     
    road[9][25]=Cell(turn_left=True)
    
    road[16][25]=Cell(turn_right=True)
    road[15][23]=Cell(turn_right=True)
    road[13][24]=Cell(turn_left=True)     
    road[12][24]=Cell(turn_left=True)
    
    return road


#print crossing no.1
def showRoad(road):
    for r in range(22):
        for c in range(54):
            if(isinstance(road[r][c], Cell)):
                if(road[r][c].turn_left):
                    print('L',end=' ')            
                elif(road[r][c].turn_right):
                    print('R',end=' ')
                else:
                    print(road[r][c].status,end=' ')
            else:
                print(road[r][c],end=' ')
        print("")
            

