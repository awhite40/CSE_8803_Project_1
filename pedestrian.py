import numpy as np
import random
import math
import map
from matplotlib import pyplot as plt
from collections import namedtuple

personStruct = namedtuple("personStruct", "index x y status")
active_list = []
m = personStruct(0, 800, 1557, 1)
active_list.append(m)
map.map[800, 800] = 1
m = personStruct(1, 801, 800, 1)
active_list.append(m)
map.map[801, 800] = 1
m = personStruct(2, 802, 800, 1)
active_list.append(m)
map.map[802, 800] = 1
m = personStruct(3, 803, 800, 1)
active_list.append(m)
map.map[803, 800] = 1

shuffle = [0,1,2,3]
total_so_far = 4
total_active = 4
time = 0.0
birth = [(800, 800), (801, 800), (802, 800), (803, 800)]
marta = [(800,1558), (801,1558), (802,1558), (803, 1558)]

def move(people_list, k):
	global total_active
	if people_list[k].status == 1:

		if people_list[k].y == 1556:
			move_target = 0
			P = [(people_list[k].x-1, people_list[k].y + 1), (people_list[k].x, people_list[k].y + 1), (people_list[k].x + 1, people_list[k].y + 1)]
			for i in range(len(P)):
				if map.map[P[i]] == 0:
					move_target = P[i]
					break
			if move_target != 0:
				map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
				map.map[move_target[0], move_target[1]] = 1.0	# block the newly occupied cell
				people_list[k] = people_list[k]._replace(x=move_target[0], y=move_target[1])

		elif people_list[k].y == 1557:
			map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
			people_list[k] = people_list[k]._replace(x=0, y=0, status = 0)
			total_active = total_active - 1

		else:
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
				if map.map[P[i]] == 0:  # if the cell is not blocked, calculate M
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
				map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
				map.map[move_target[0], move_target[1]] = 1.0	# block the newly occupied cell
				people_list[k] = people_list[k]._replace(x=move_target[0], y=move_target[1])

while total_active != 0:
	random.shuffle(shuffle)
	for person in shuffle:
		move(active_list, person)

	if time < 10:
		for place in birth:
			if map.map[place[0], place[1]] == 0:
				total_so_far = total_so_far + 1
				total_active = total_active + 1
				m = personStruct(total_so_far, place[0], place[1], 1)
				active_list.append(m)
				shuffle.append(total_so_far-1)
	time = time + 0.5
	print total_active
print "time is", time
print "total_so_far is", total_so_far
