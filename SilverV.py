prev_pos=None
dire = [0,0]  
def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
    ''' 
    global prev_pos,dire,right
    if prev_pos==None:
        prev_pos=[ball_frect.pos[0],ball_frect.pos[1]] 
        if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
            return "down"
        else:
            return "up"
    dire[0]=ball_frect.pos[0]-prev_pos[0]
    dire[1]=ball_frect.pos[1]-prev_pos[1]
    prev_pos[0]=ball_frect.pos[0]
    prev_pos[1]=ball_frect.pos[1]
    table_size=(paddle_frect.pos[0]-ball_frect.size[0],table_size[1]-ball_frect.size[1])  
    # the position of centre of mass in the new table coord is the same as the position of the top-left corner in the old table coord. 
    if dire[0]>0:
        y_travel = (table_size[0]-ball_frect.pos[0])/dire[0]*dire[1]
        y_dest = ball_frect.pos[1]+ y_travel
        square_num=y_dest//table_size[1]
        if square_num==0:
            pass
        elif(square_num%2)==0:
            y_dest += (-square_num*table_size[1])
        elif(square_num%2)==1:
            y_dest += (-square_num*table_size[1])
            y_dest = table_size[1]-y_dest
    
    elif dire[0]<0:
        y_travel = (ball_frect.pos[0])/(-dire[0])*dire[1]
        y_dest = ball_frect.pos[1] +y_travel
        square_num =y_dest//table_size[1]
        if square_num==0:
            pass
        elif(square_num%2)==0:
            y_dest += (-square_num*table_size[1])
        elif(square_num%2)==1:
            y_dest += (-square_num*table_size[1])
            y_dest = table_size[1]-y_dest  
    else:
        y_dest = ball_frect.pos[1] 
    if y_dest > (paddle_frect.pos[1]+paddle_frect.size[1]/2):
        return "down"
    else:
        return "up"
    
