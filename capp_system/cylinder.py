import top_view
import front_view
seq=["EN8D","NORMALISING","NC. TURNING","STRESS RELIEVING","NC. TURNING","H. MILLING","FITTING","R.DRILLING","FITTING","CYL.GRINDING","CYL.GRINDING","INT.GRINDING"];
   
length=0
breadth=0
height=0
def info():
    global length
    global breadth
    global height
    if(top_view.is_circle()):
        top_view.circle_info()
        length=2*top_view.max_r
    else:
        front_view.circle_info()
        length=2*front_view.max_r
        
    
    if(top_view.is_rectangle()):
        top_view.rectangle_info()
        height_min=min(top_view.height_y)
        height_max=max(top_view.height_y)
        
    else:
        front_view.rectangle_info()
        height_min=min(front_view.height_y)
        height_max=max(front_view.height_y)
     
    breadth=length
    height=height_max-height_min
    
           
    
       
 

