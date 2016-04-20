import find_shape
import dxf_reader
import operation_sequence
import parameters_input
if(find_shape.shape()=="cylinder"):
    import cylinder
    

f=open(dxf_reader.filename+".txt",'w')
height=cylinder.height()
length,breadth=cylinder.length()
extra_l=length+4
length_left=length+2*0.3
breadth_left=length_left
length=str(length)
extra_b=breadth+4

breadth=str(breadth)
extra_h=height+4
height_left=height+2*0.3
height=str(height)

extra_l=str(extra_l)
extra_b=str(extra_b)
extra_h=str(extra_h)

length_left=str(length_left)
breadth_left=str(breadth_left)
height_left=str(height_left)

dia,hole_count=cylinder.hole()
left_dia=dia-2*0.3
left_dia=str(left_dia)
hole_count=str(hole_count)
dia=str(dia)
hardness,cf,material_recrystalizing_point=parameters_input.read_param_material()
temperature=parameters_input.read_param_heat_tratment()
hardness=str(hardness)
temp=str(temperature)
def gen():
    f.write ( "Raw Material Specification...... HGT x LNT x BRD     TOTAL PS       No/Comp ....\n")
    f.write ( "................................................................................\n")
    f.write ( "Block ..................  "+extra_h+" x "+extra_l+" x "+extra_b +"      1         1\n" ) 
    f.write("MATERIAL HARDNESS------------"+hardness+"\n")
    f.write ( "................................................................................\n")
   
    seq=operation_sequence.CYLINDER()
    for i in seq:
        
        
    
        if(i=="NORMALISING"):
            f.write ( "Heat Treatment ...................................................  NORMALISING\n")
            
            if(temperature<=material_recrystalizing_point):
                f.write("Heat temperature--- less than recrystalisation point.... "+temp+"...HOT WORKING"+"\n")
            else:
                f.write("Heat temperature--- more than recrystalisation point.... "+temp+"...COLD WORKING"+"\n")
           
            f.write ( "................................................................................\n")
        elif(i=="NC.TURNING"):
            f.write ( "TURNING .............."+extra_h+" x "+length_left+" x "+breadth_left+".........   NC.TURNING\n")
            f.write ( "................................................................................\n")
        elif(i=="STRESS RELIEVING"):
            f.write ( "STRESS RELIEVING.........................................................  \n")
            
        elif(i=="H.MILLING"):
            f.write ( "MILLING    .........4  H.MILLING "+height_left+" x "+length_left+" x "+breadth_left+"\n")
            f.write("2 faces milling")
            f.write ( "................................................................................\n")
   
        elif(i=="FITTING"):
            f.write ( "FITTING.........................................................  \n")
            f.write ( "................................................................................\n")
   
        elif(i=="R.DRILLING"):
            f.write ( "RADIAL DRILLING...  "+left_dia+"------"+hole_count+"........... \n ")
            f.write ( "................................................................................\n")
   
        
        elif(i=="CYL.GRINDING"):
            f.write ( "CYLLINDRICAL GRINDING       ...... "+height+" x "+length+" x "+breadth+"\n")
            f.write ( "................................................................................\n")
   
        elif(i=="INT.GRINDING"):
            f.write ( "INTERNAL GRINDING   "+dia+"------"+hole_count+" ......................................................  \n")
            f.write ( "................................................................................\n")
   
         
        
    
    