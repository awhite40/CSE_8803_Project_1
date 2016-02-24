import numpy as np
import random
import math
import map
from matplotlib import pyplot as plt
from collections import namedtuple


MartaFF = np.loadtxt('Marta_floor_field.txt')
VarsityFF = np.loadtxt('Varsity_floor_field.txt')
NorthAveFF = np.loadtxt('NorthAve_floor_field.txt')
PetersParkingDeckFF = np.loadtxt('PetersParkingDeck_floor_field.txt')
EastCampusDormsFF = np.loadtxt('EastCampusDorms_floor_field.txt')
BusStopFF = np.loadtxt('BusStop_floor_field.txt')
StudentCenterFF = np.loadtxt('StudentCenter_floor_field.txt')

def findFF(destination):
	if destination == 'Marta':
		FF = MartaFF
	elif destination == 'Varsity':
		FF = VarsityFF
	elif destination == 'North_Ave':
		FF = NorthAveFF
	elif destination == 'Peters_Parking_Deck':
		FF = PetersParkingDeckFF
	elif destination == 'East_Campus_Dorms':
		FF = EastCampusDormsFF
	elif destination == 'Bus_Stop':
		FF = BusStopFF
	elif destination == 'Student_Center':
		FF = StudentCenterFF
	return FF


personStruct = namedtuple("personStruct", "index gate destin x y status")
active_list = []
m = personStruct(0, 'C', 'NorthAve', 800, 800, 1)
active_list.append(m)
map.map[800, 800] = 1
m = personStruct(1, 'C', 'Marta', 801, 800, 1)
active_list.append(m)
map.map[801, 800] = 1
m = personStruct(2, 'C', 'Peters_Parking_Deck', 802, 800, 1)
active_list.append(m)
map.map[802, 800] = 1
m = personStruct(3, 'C', 'East_Campus_Dorms', 803, 800, 1)
active_list.append(m)
map.map[803, 800] = 1

shuffle = [0,1,2,3]
# shuffle = [0]
total_so_far = 4
total_active = 4
# total_active = 1
time = 0.5

def validneighbors(position, matrix):
	(x,y) = position
	neighbors = [(x-1,y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x,y-1), (x+1, y-1)]
	neighbors = [p for p in neighbors if matrix[p] == 0]
	return neighbors

def move(people_list, k, time):
	global total_active
	if people_list[k].status == 1:
		floorfield = findFF(people_list[k].destin)
		(x,y) = (people_list[k].x, people_list[k].y)

		if floorfield[x,y] <= 9:			# if the person is at the gate, then make him disappear
			map.map[x,y] = 0.0				# clear the previous cell in the map
			people_list[k] = people_list[k]._replace(status = 0)	# clear the person's position and make him inactive
			total_active = total_active - 1									# reduce one active person
			print "person number", k, "has arrived at", people_list[k].destin, "at time", time

		else:							# if the person is in the middle of the map
			infinity = float("inf")
			P = validneighbors((x,y), map.map)
			if len(P) > 0: # if the people_list[k] can move
				# M = []
				# for i in range(len(P)):
					# R = floorfield[P[i]]  # distance between the possible cell and the cloest block of marta gate to the people_list[k]
				# 	M.append(1.0 / R)
	
				# rand = random.random()	# random number from uniform distribution
				# N = 1.0 / np.sum(M)		# normalization constant
				# m_sum = 0.0				# cumulative probability
				# for i in range(len(M)):
				# 	M[i] = M[i] * N 						# normalize probability of moving to P[i]
				# 	m_sum = m_sum + M[i]					# get cumulative probability of moving to P[i]
				# 	if rand < m_sum:						# once have find the P[i], break out of the loop
				# 		move_target = P[i]
				# 		break

				if len(P)==1:
					move_target = P[0]
				elif len(P)>1:
					D = [floorfield[P[i]] for i in range(len(P))]
					temp_target = [p for (d,p) in sorted(zip(D,P), key=lambda pair: pair[0])][0]
					if floorfield[temp_target] <= floorfield[x,y]:
						move_target = temp_target
					else:
						move_target = (x,y)

				map.map[people_list[k].x, people_list[k].y] = 0.0				# clear the previous cell in the map
				map.map[move_target[0], move_target[1]] = 1.0	# block the newly occupied cell
				people_list[k] = people_list[k]._replace(x=move_target[0], y=move_target[1])


def waitforcw(people_list, k, closedcws, cwstart, cwend):
	if people_list[k].status == 1:

		floorfield = findFF(people_list[k].destin)
		(x,y) = (people_list[k].x, people_list[k].y)
		for cw in closedcws:
			startloc = cwstart[cw]
			endloc = cwend[cw]
			cwstartvalue = floorfield[startloc]
			# print 'cwstartvalue is', cwstartvalue
			cwendvalue = floorfield[endloc]
			# print 'endloc is', endloc
			# print 'cwendvalue is', cwendvalue

			if cwstartvalue - cwendvalue > 5:
				if floorfield[x,y] > cwstartvalue  and floorfield[x,y] < cwstartvalue+5:
					people_list[k] = people_list[k]._replace(status = 2)
					print 'person', k, 'ran into a red light at', (x,y)
					break
			elif cwendvalue - cwstartvalue > 5:
				if floorfield[x,y] > cwendvalue  and floorfield[x,y] < cwendvalue+5:
					people_list[k] = people_list[k]._replace(status = 2)
					print 'person', k, 'ran into a red light at', (x,y)
					break

def greenlight(people_list, k):
	(x,y) = (people_list[k].x, people_list[k].y)
	if people_list[k].status == 2:
		people_list[k] = people_list[k]._replace(status = 1)
		print 'person', k, 'continued walking at', (x,y)

cwclosetime = 0.0
cwopentime = 0.0
while total_active != 0:
	if time%240 == 0:
		cwclosetime = time
		cwopentime = cwclosetime + 60
		closedcws = random.sample(map.Crosswalks, 3)

	random.shuffle(shuffle)
	for person in shuffle:
		if time < cwopentime and time >= cwclosetime:
			waitforcw(active_list, person, closedcws, map.cwstart, map.cwend)
		elif time == cwopentime:
			greenlight(active_list, person)
		move(active_list, person, time)
	# if time < 10:
	# 	for place in birth:
	# 		if map.map[place[0], place[1]] == 0:
	# 			total_so_far = total_so_far + 1
	# 			total_active = total_active + 1
	# 			m = personStruct(total_so_far, place[0], place[1], 1)
	# 			active_list.append(m)
	# 			shuffle.append(total_so_far-1)
	time = time + 0.5
	# print total_active
# print "time is", time
# print "total number of people simulated is", total_so_far






