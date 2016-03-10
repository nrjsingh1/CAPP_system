import dxf_reader

class Circle:
    def is_concentric(self):
        f
        
        
        
entities=[]


    


def layer_name():
    for i in dxf_reader.LayerTable.__iter__():
        if(i.name=="top_view"):
            print i.name
            

def entities_name():
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="top_view"):
            entities.append(i.dxftype)
            print i.dxftype
            
            
def circle_info():
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="top_view" and i.dxftype=="CIRCLE"):
            
            print i.center
            print i.radius
            
            
    
    

    
    