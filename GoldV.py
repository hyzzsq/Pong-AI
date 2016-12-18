prev_pos=None
dire = [0,0]  
def get_dest(paddle_frect, other_paddle_frect, ball_frect, table_size):
    ''' return x and y destination of ball in flight''' 
    global dire,prev_pos
    dire[0]=ball_frect.pos[0]-prev_pos[0]
    dire[1]=ball_frect.pos[1]-prev_pos[1]
    prev_pos[0]=ball_frect.pos[0]
    prev_pos[1]=ball_frect.pos[1]
    table_size=(table_size[0],table_size[1]-ball_frect.size[1])

    if dire[0]>0:
        x_dest = "right" 
        y_travel = (max(paddle_frect.pos[0],other_paddle_frect.pos[0])-ball_frect.size[0]-ball_frect.pos[0])/dire[0]*dire[1]

    elif dire[0]<0:
        x_dest = "left"
        y_travel = (ball_frect.pos[0]-min(paddle_frect.pos[0],other_paddle_frect.pos[0])-paddle_frect.size[0])/(-dire[0])*dire[1]
    else:
        y_dest = ball_frect.pos[1] 
        x_dest = None
        y_travel = 0
    y_dest = ball_frect.pos[1] +y_travel
    square_num =y_dest//table_size[1]
    if square_num==0:
        pass
    elif(square_num%2)==0:
        y_dest += (-square_num*table_size[1])
    elif(square_num%2)==1:
        y_dest += (-square_num*table_size[1])
        y_dest = table_size[1]-y_dest  
    
    y_dest +=ball_frect.size[1]/2 
    return x_dest, y_dest 

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global prev_pos
    if prev_pos == None:
        prev_pos=(ball_frect.pos[0],ball_frect.pos[1])
        prev_pos=[ball_frect.pos[0],ball_frect.pos[1]] 
        if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
            return "down"
        else:
            return "up"
    if paddle_frect.pos[0] > other_paddle_frect.pos[0]:
        side = "right"
    else:
        side = "left" 
    a, b = get_dest(paddle_frect, other_paddle_frect, ball_frect, table_size)
     
    if a == side:
        if b > (paddle_frect.pos[1]+paddle_frect.size[1]/2):
            return "down"
        else:
            return "up" 
    else:
        if (paddle_frect.pos[1]+paddle_frect.size[1]/2)>table_size[1]/2:
            return "up"
        else:
            return "down"