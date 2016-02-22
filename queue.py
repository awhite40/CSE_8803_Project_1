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
            total_people = gate_count * people_per_gate
            global total_active
            personStruct = namedtuple("personStruct", "index gate destin x y status")  # create struct for each person, with index, destination, position,active(1)or not(0)
            active_list = []  
            i=1
            for i in range((total_people)):
                    gate_range = random.random() 
                    if gate_range >= 0 and gate_range < 0.2:
                        gate_name = 'A'
                    elif gate_range >=0.2 and gate_range < 0.4:
                        gate_name = 'B'
                    elif gate_range >=0.4 and gate_range < 0.6:
                        gate_name = 'C'
                    elif gate_range >=0.6 and gate_range < 0.8:
                        gate_name = 'D'
                    elif gate_range >=0.8 and gate_range < 1.0:
                        gate_name = 'E'
                    
                    dest_range = random.random() 
                    if dest_range >= 0 and dest_range < 0.25:
                        destination = 'Marta'
                    elif dest_range >=0.25 and dest_range < 0.5:
                        destination = '2nd dest'
                    elif dest_range >=0.50 and dest_range < 0.75:
                        destination = '3rd dest'
                    elif dest_range >=0.75 and dest_range < 1.0:
                        destination = '4th dest'
                        
                    m = personStruct(i,gate_name,destination,800, 1557, 1)    # create person 0
                    print "i is: "+str(i) + " gate_name is:"+ str(gate_name) + " destination is:"+ str(destination)

                    #determine x and y
                        
                    active_list.append(m)
                                        
            return active_list


new_active_list = people_gen()