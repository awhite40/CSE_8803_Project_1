# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 00:42:06 2016

@author: sumsen
"""

import numpy as np
#import random
import math
import merst
import Map
from matplotlib import pyplot as plt
from collections import namedtuple


def people_gen():
            gate_count = 5
            people_per_gate = 100
            destination_count = 7
            start = 800
            x=0
            y=0
            status = 1
            total_people = gate_count * people_per_gate
            global total_active
            personStruct = namedtuple("personStruct", "index gate destin x y status")  # create struct for each person, with index, destination, position,active(1)or not(0)
            active_list = []  
            i=1
            for i in range((total_people)):
                    x = y = 0
                    #gate_range = random.random()
                    gate_range = merst.myrandom()
                    #print gate_range
                    if gate_range >= 0 and gate_range < 0.2:
                        gate_name = 'Gate_A'
                        #grid_range = random.random()
                        grid_range = merst.myrandom()
                        for j in range(16):
                                x = (796)
                                #print j
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range >=(j/16.0) and grid_range < ((j+1)/16.0):
                                    y = (691 + j)    
                        
                    elif gate_range >=0.2 and gate_range < 0.4:
                        gate_name = 'Gate_B'
                        #grid_range_B = random.random()
                        grid_range_B = merst.myrandom()
                        for jb in range(16):
                                y = (564) #verified
                                #print jb
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_B >=(jb/16.0) and grid_range_B < ((jb+1)/16.0):
                                    x = (470 + jb)  #Need to verify
                                    #print '@#$%'
                                    #print x
                    elif gate_range >=0.4 and gate_range < 0.6:
                        gate_name = 'Gate_C'
                        #grid_range_C = random.random() 
                        grid_range_C = merst.myrandom()
                        for jc in range(16):
                                y = (757) #Need to verify
                                #print jc
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_C >=(jc/16.0) and grid_range_C < ((jc+1)/16.0):
                                    y = (796+jc)  #Need to verify
                    elif gate_range >=0.6 and gate_range < 0.8:
                        gate_name = 'Gate_D'
                        #grid_range_D = random.random() 
                        grid_range_D = merst.myrandom()
                        for jd in range(16):
                                x = (424) #Need to verify
                                #print jd
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_D >=(jd/16.0) and grid_range_D < ((jd+1)/16.0):
                                    y = (666+jd)  #Need to verify -check
                    elif gate_range >=0.8 and gate_range < 1.0:
                        gate_name = 'Gate_E'
                        #grid_range_E = random.random()
                        grid_range_E = merst.myrandom()
                        for je in range(16):
                                y = (800) #Need to verify
                                #print je
                                #print j/16.0
                                #print ((j+1)/16.0)
                                if grid_range_E >=(je/16.0) and grid_range_E < ((je+1)/16.0):
                                    y = (455+je)  #Need to verify -check
                        
                    
                    #dest_range = random.random()
                    dest_range = merst.myrandom()
                    if dest_range >= 0 and dest_range < 0.14:
                        destination = 'Marta'
                    elif dest_range >=0.14 and dest_range < 0.28:
                        destination = 'Varsity'
                    elif dest_range >=0.28 and dest_range < 0.42:
                        destination = 'North_Ave'
                    elif dest_range >=0.42 and dest_range < 0.56:
                        destination = 'Peters_Parking_Deck'
                    elif dest_range >=0.56 and dest_range < 0.7:
                        destination = 'East_Campus_Dorms'
                    elif dest_range >=0.7 and dest_range < 0.84:
                        destination = 'Bus_Stop'
                    elif dest_range >=0.84 and dest_range < 1.00:
                        destination = 'Student_Center'
                        
                    print Map.map[x,y]
                    print "i: "+str(i) + " gate_name:"+ str(gate_name) + " destination:"+ str(destination) + " x:" +str(x) + " y:" +str(y) + " status: " +str(1) #try
                    if Map.map[x,y] == 0:  
                        m = personStruct(i,gate_name,destination,x,y,status)    # create person 0
                        
                        
                        print m  #verifying that everything is random
                    #determine x and y
                        
                        active_list.append(m)
                                        
            return active_list


new_active_list = people_gen()