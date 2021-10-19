#!/usr/bin/env python2
#import dxf_reader
import front_view
import top_view

def shape():
    if(front_view.is_rectangle() and top_view.is_circle()) or ( front_view.is_circle() and top_view.is_rectangle()):
                                                                                    #check for rectangle.
        return "cylinder"
    elif(front_view.is_circle() and top_view.is_circle()):
        
        return "SPHERE"

    elif(front_view.is_rectangle() and top_view.is_rectangle()):
        return "CUBOID"
