import dxf_reader

def layer_name():
    for i in dxf_reader.LayerTable.__iter__():
        if(i.name=="front_view"):
            print i.name
            

def entities_name():
    for i in dxf_reader.EntitySection.__iter__():
        if(i.layer=="front_view"):
            print i.dxftype
            
            

    
    