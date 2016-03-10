#import front_view
import top_view
import dxf_reader
import parameters_input
dxf_reader.read_msg()                                                           #1 read dxf file

                                                                                #2 read input parametrs
parameters_input.read_param_material()
parameters_input.read_param_heat_tratment()
parameters_input.read_param_job_size()



top_view.layer_name()

top_view.entities_name()