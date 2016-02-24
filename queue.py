# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 00:42:06 2016

@author: sumsen
"""

import numpy as np
import random
import math
#import map
from matplotlib import pyplot as plt
from collections import namedtuple


def people_gen():
            gate_count = 5
            people_per_gate = 100
            destination_count = 7
            start = 800
            x=0
            y=0
            total_people = gate_count * people_per_gate
            global total_active
            personStruct = namedtuple("personStruct", "index gate destin x y status")  # create struct for each person, with index, destination, position,active(1)or not(0)
            active_list = []  
            i=1
            for i in range((total_people)):
                    x = y = 0
                    gate_range = random.random() 
                    if gate_range >= 0 and gate_range < 0.2:
                        gate_name = 'Gate A'
                        grid_range = random.random() 
                        """
                        if grid_range >=0 and grid_range < (1/16):
                            print grid_range
                            x = (start-4) 
                            y = (start - 109 + 1)
                        elif grid_range >=(1/16) and grid_range < (2/16):
                            x = (start-4) 
                            y = (start - 109 + 2)
                            
                            """
                        for j in range(16):
                                x = (start-4)
                                #print j
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range >=(j/16.0) and grid_range < ((j+1)/16.0):
                                    y = (start - 109 + j+1)    
                        
                    elif gate_range >=0.2 and gate_range < 0.4:
                        gate_name = 'Gate B'
                        grid_range_B = random.random() 
                        for jb in range(16):
                                x = (470) #Need to verify
                                #print jb
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_B >=(jb/16.0) and grid_range_B < ((jb+1)/16.0):
                                    y = (start - 109 + jb+1)  #Need to verify
                    elif gate_range >=0.4 and gate_range < 0.6:
                        gate_name = 'Gate C'
                        grid_range_C = random.random() 
                        for jc in range(16):
                                x = (796) #Need to verify
                                #print jc
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_C >=(jc/16.0) and grid_range_C < ((jc+1)/16.0):
                                    y = (758+jc)  #Need to verify
                    elif gate_range >=0.6 and gate_range < 0.8:
                        gate_name = 'Gate D'
                        grid_range_D = random.random() 
                        for jd in range(16):
                                x = (start + 81 -457) #Need to verify
                                #print jd
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_D >=(jd/16.0) and grid_range_D < ((jd+1)/16.0):
                                    y = (200+jd)  #Need to verify -check
                    elif gate_range >=0.8 and gate_range < 1.0:
                        gate_name = 'Gate E'
                        grid_range_E = random.random() 
                        for je in range(16):
                                x = (start + 112) #Need to verify
                                #print je
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_E >=(je/16.0) and grid_range_E < ((je+1)/16.0):
                                    y = (300+je)  #Need to verify -check
                        
                    
                    dest_range = random.random() 
                    if dest_range >= 0 and dest_range < 0.14:
                        destination = 'Marta'
                    elif dest_range >=0.14 and dest_range < 0.28:
                        destination = 'Varsity'
                    elif dest_range >=0.28 and dest_range < 0.42:
                        destination = 'North Ave'
                    elif dest_range >=0.42 and dest_range < 0.56:
                        destination = 'Peters Parking Deck'
                    elif dest_range >=0.56 and dest_range < 0.7:
                        destination = 'East Campus Dorms'
                    elif dest_range >=0.7 and dest_range < 0.84:
                        destination = 'Bus Stop'
                    elif dest_range >=0.84 and dest_range < 1.00:
                        destination = 'Student Center'
                        
                    m = personStruct(i,gate_name,destination,800, 1557, 1)    # create person 0
                    print "i is: "+str(i) + " gate_name is:"+ str(gate_name) + " destination is:"+ str(destination) + " x is:" +str(x) + " y is:" +str(y)

                    #determine x and y
                        
                    active_list.append(m)
                                        
            return active_list


new_active_list = people_gen()