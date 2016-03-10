import dxf_reader
import math

        
entities=[]

def distance(x1,y1,x2,y2):
    dis=math.sqrt ((x1-x2)**2 + (y1-y2)**2)
    return dis

def layer_name():
    for i in dxf_reader.LayerTable.__iter__():
        if(i.name=="front_view"):
            print i.name
            

def entities_name():
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="front_view"):
            entities.append(i.dxftype)
            print i.dxftype
            
            
def circle_info():
    print "circle info ......"
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="front_view" and i.dxftype=="CIRCLE"):
            
            print i.center
            print i.radius
            
    
def rectangle_info():
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="front_view" and (i.dxftype=="POLYLINE" or i.dxftype=="LWPOLYLINE" or i.dxftype=="LINE" )):
            
            print i.points
            print i.is_closed
            
            k=0
            for j in i.__iter__():
                
                if(k<=2):
                    k=k+1
                else:
                    k=0
                
                m=i[k]
                
                print  distance(j[0],j[1],m[0],m[1])
            
            
    
    

    
    