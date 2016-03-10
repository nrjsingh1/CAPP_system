
import dxfgrabber

s=raw_input("Enter dxf file path/name \n")
print "Received file ",s

dxf = dxfgrabber.readfile(s)#dxf drawing object .. contains all information about drawing... class drawing  

print dxf.dxfversion

LayerTable =dxf.layers#object of type layertable

StyleTable=dxf.styles#object of type styletable

LinetypeTable=dxf.linetypes#object of type linetypetable

BlocksSection=dxf.blocks#object of type blocksection dict like

EntitySection=dxf.entities#object of type entitysection

dxfObjects= dxf.objects#object of type entitysection list like

modelSpace= dxf.modelspace

paperSpace=dxf.paperspace

 
 
def read_msg():
    print "reading dxf file ........................ "+s        
       
   