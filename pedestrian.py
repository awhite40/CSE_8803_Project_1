import numpy as np
import random
import math
import Map
from matplotlib import pyplot as plt
from collections import namedtuple
import matplotlib.animation as manimation

# Code for animaiting the map images
MapWriter = manimation.writers['map_image']
metadata = dict(title='Map Movie')
writer = MapWriter(fps=2, metadata=metadata)
fig = map.map

personStruct = namedtuple("personStruct", "index x y status")  # create struct for each person, recording the person's index, position and whether he is active
active_list = [] 			# list of all people created by the simulation
m = personStruct(0, 800, 1557, 1)	# create person 0
active_list.append(m)			# put person 0 into the list
map.map[800, 800] = 1			# mark the person's position on the map
m = personStruct(1, 801, 800, 1)
active_list.append(m)
map.map[801, 800] = 1
m = personStruct(2, 802, 800, 1)
active_list.append(m)
map.map[802, 800] = 1
m = personStruct(3, 803, 800, 1)
active_list.append(m)
map.map[803, 800] = 1

shuffle = [0,1,2,3]	# array of all people in the simulation. will be shuffled later to update in a random order
total_so_far = 4	# total number of people generated so far
total_active = 4	# total number of people currently active in the simulation
time = 0.0		# initial time
birth = [(800, 800), (801, 800), (802, 800), (803, 800)]	# cells that can generate people
marta = [(800,1558), (801,1558), (802,1558), (803, 1558)]	# cells that people can disappear

def move(people_list, k):	# function to move a person
	global total_active
	if people_list[k].status == 1:	# if the kth person is currently active, then move him

		if people_list[k].y == 1556:   # if the person is one cell away from the marta, then move him into one of the three available cells on y = 1557
			move_target = 0
			P = [(people_list[k].x-1, people_list[k].y + 1), (people_list[k].x, people_list[k].y + 1), (people_list[k].x + 1, people_list[k].y + 1)]  # list of the three possible cells
			for i in range(len(P)):
				if Map.map[P[i]] == 0:
					move_target = P[i]
					break
			if move_target != 0:
				Map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
				Map.map[move_target[0], move_target[1]] = 1.0	# block the newly occupied cell
				people_list[k] = people_list[k]._replace(x=move_target[0], y=move_target[1])

		elif people_list[k].y == 1557:		# if the person is right next to the marta entrance, make him disappear
			Map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
			people_list[k] = people_list[k]._replace(x=0, y=0, status = 0)			# clear the position of the person to 0
			total_active = total_active - 1							# minus 1 active person in the simulation

		else:	# if the person is not at the end of the road, do normal move
			infinity = float("inf")
			destination = (infinity, infinity) # the cloest block of marta gate to the people_list[k]
			for exit in marta:
				if math.sqrt((exit[0] - people_list[k].x)**2 + (exit[1] - people_list[k].y)**2) < math.sqrt((destination[0] - people_list[k].x)**2 + (destination[1] - people_list[k].y)**2):
					destination = exit

			# the five cells that the people_list[k] can move to
			P = [(people_list[k].x - 1, people_list[k].y + 1), (people_list[k].x, people_list[k].y + 1), (people_list[k].x + 1, people_list[k].y + 1), (people_list[k].x - 1, people_list[k].y), (people_list[k].x + 1, people_list[k].y)]

			M = []
			for i in range(len(P)):
				R = math.sqrt((P[i][0] - destination[0])**2 + (P[i][1] - destination[1])**2)  # distance between the possible cell and the cloest block of marta gate to the people_list[k]
				if Map.map[P[i]] == 0:  # if the cell is not blocked, calculate M
					M.append(1.0 / R)
				else:					# if the cell is blocked, M = 0
					M.append(0.0)

			can_move = False
			for m in M:					# if at least one M[i] is not zero, then the people_list[k] can move
				if m != 0.0:
					can_move = True
					break

			if can_move == True:		# if the people_list[k] can move
				rand = random.random()	# random number from uniform distribution
				N = 1.0 / np.sum(M)		# normalization constant
				m_sum = 0.0				# cumulative probability
				for i in range(len(M)):
					if M[i] != 0.0:
						M[i] = M[i] * N 						# normalize probability of moving to P[i]
						m_sum = m_sum + M[i]					# get cumulative probability of moving to P[i]
						if rand < m_sum:						# once have find the P[i], break out of the loop
							move_target = P[i]
							break
				Map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
				Map.map[move_target[0], move_target[1]] = 1.0	# block the newly occupied cell
				people_list[k] = people_list[k]._replace(x=move_target[0], y=move_target[1])

# simulate until all people have exited through marta
with writer.saving(map, "Map_movie.mp4", 2):
    while total_active != 0:
    	random.shuffle(shuffle)			# shuffle the list of people in the simulation so we can update all of them in a random order
    	for person in shuffle:
    		move(active_list, person)	# move each person

    	if time < 10:				# for the first 10 seconds, people will be generated on the four cells (if they are available) every 0.5 second
    		for place in birth:
    			if Map.map[place[0], place[1]] == 0:
    				total_so_far = total_so_far + 1				# update total number of people so far
    				total_active = total_active + 1				# update total number of active people
    				m = personStruct(total_so_far, place[0], place[1], 1)	# create a peroson
    				active_list.append(m)					# put the person in list
    				shuffle.append(total_so_far-1)				# put the person in the shuffle list
    	time = time + 0.5
        moviewriter.grab_frame								# discrete time step: 0.5s
	# print total_active
print "time is", time
print "total_so_far is", total_so_far
