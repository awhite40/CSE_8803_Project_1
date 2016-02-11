# Creating matrix to represent a map of Bobby-Statium and the surrounding areas
import numpy as np
from matplotlib import pyplot as plt

# Creating empty Map
map = np.empty((1600, 1600,)) * np.NAN

# Creating pathway to MARTA
start = 800
# 1st crosswalk

M_cw1_S_x = start
M_cw1_S_y = start
M_cw1_E_x = M_cw1_S_x + 4
M_cw1_E_y = M_cw1_S_y + 42

#print M_cw1_E_x, M_cw1_E_y
#M_cw1_E = (M_cw1_S[0] + 4, M_cw1_S[1] + 42)
map[M_cw1_S_x:M_cw1_E_x, M_cw1_S_y:M_cw1_E_y] = 0

# 1st Sidewalk

M_sw1_S_x = M_cw1_S_x
M_sw1_S_y = M_cw1_E_y
M_sw1_E_x = M_sw1_S_x + 5
M_sw1_E_y = M_sw1_S_y + 176

#print M_sw1_S_x, M_sw1_S_y, M_sw1_E_x, M_sw1_E_y
map[M_sw1_S_x:M_sw1_E_x, M_sw1_S_y:M_sw1_E_y] = 0

# 2nd Crosswalk
M_cw2_S_x = M_sw1_S_x
M_cw2_S_y = M_sw1_E_y
M_cw2_E_x = M_cw2_S_x + 4
M_cw2_E_y = M_cw2_S_y + 19

map[M_cw2_S_x:M_cw2_E_x, M_cw2_S_y:M_cw2_E_y] = 0

# 2nd Sidewalk part 1 - up to Varsity
M_sw2_S_x = M_cw2_S_x - 1
M_sw2_S_y = M_cw2_E_y
M_sw2_E_x = M_sw2_S_x + 6
M_sw2_E_y = M_sw2_S_y + 195
map[M_sw2_S_x:M_sw2_E_x, M_sw2_S_y:M_sw2_E_y] = 0


# 2nd Sidewalk part 2

M_sw2b_S_x = M_sw2_S_x
M_sw2b_S_y = M_sw2_E_y
M_sw2b_E_x = M_sw2b_S_x + 6
M_sw2b_E_y = M_sw2b_S_y + 67
map[M_sw2b_S_x:M_sw2b_E_x, M_sw2b_S_y:M_sw2b_E_y] = 0

# 3rd Crosswalk
M_cw3_S_x = M_sw2b_S_x + 1
M_cw3_S_y = M_sw2b_E_y
M_cw3_E_x = M_cw3_S_x + 4
M_cw3_E_y = M_cw3_S_y + 15

map[M_cw3_S_x:M_cw3_E_x, M_cw3_S_y:M_cw3_E_y] = 0

# 3rd Sidewalk
M_sw3_S_x = M_cw3_S_x - 1
M_sw3_S_y = M_cw3_E_y
M_sw3_E_x = M_sw3_S_x + 6
M_sw3_E_y = M_sw3_S_y + 217
map[M_sw3_S_x:M_sw3_E_x, M_sw3_S_y:M_sw3_E_y] = 0

# 4th Crosswalk
M_cw4_S_x = M_sw3_S_x + 1
M_cw4_S_y = M_sw3_E_y
M_cw4_E_x = M_cw4_S_x + 4
M_cw4_E_y = M_cw4_S_y + 27

map[M_cw4_S_x:M_cw4_E_x, M_cw4_S_y:M_cw4_E_y] = 0



# Creating Pathway to NorthAve Apartments

# 1st crosswalk - 32 spaces south
N_cw1_S_x = M_cw1_S_x
N_cw1_S_y = 800 - 4
N_cw1_E_x = N_cw1_S_x + 32
N_cw1_E_y = N_cw1_S_y + 4

map[N_cw1_S_x:N_cw1_E_x, N_cw1_S_y:N_cw1_E_y] = 0


# 2nd Crosswalk - 42 spaces East
N_cw2_S_x = N_cw1_E_x
N_cw2_S_y = N_cw1_S_y
N_cw2_E_x = N_cw2_S_x + 4
N_cw2_E_y = N_cw2_S_y + 42
#print N_cw2_E_x, N_cw2_E_y
map[N_cw2_S_x:N_cw2_E_x, N_cw2_S_y:N_cw2_E_y] = 0


# Sidewalk 185 spaces south
N_sw1_S_x = N_cw2_S_x
N_sw1_S_y = N_cw2_E_y
N_sw1_E_x = N_sw1_S_x + 189
N_sw1_E_y = N_sw1_S_y + 3
map[N_sw1_S_x:N_sw1_E_x, N_sw1_S_y:N_sw1_E_y] = 0

# Drive to gate - 60 spaces east
N_sw2_S_x = N_sw1_E_x
N_sw2_S_y = N_sw1_S_y
N_sw2_E_x = N_sw2_S_x + 4
N_sw2_E_y = N_sw2_S_y + 60
map[N_sw2_S_x:N_sw2_E_x, N_sw2_S_y:N_sw2_E_y] = 0

# Other side of street to Marta
# sidewalk 1
M2_sw1_S_x = N_cw2_S_x
M2_sw1_S_y = N_cw2_E_y +3
M2_sw1_E_x = M2_sw1_S_x + 5
M2_sw1_E_y = M2_sw1_S_y + 176

#print M_sw1_S_x, M_sw1_S_y, M_sw1_E_x, M_sw1_E_y
map[M2_sw1_S_x:M2_sw1_E_x, M2_sw1_S_y:M2_sw1_E_y] = 0
#map[836:841,842:1018] = 0
# Crosswalk 2
M2_cw2_S_x = M2_sw1_S_x
M2_cw2_S_y = M2_sw1_E_y
M2_cw2_E_x = M2_cw2_S_x + 4
M2_cw2_E_y = M2_cw2_S_y + 19

map[M2_cw2_S_x:M2_cw2_E_x, M2_cw2_S_y:M2_cw2_E_y] = 0

# map[836:840,1018:1037] = 0
# Sidewalk 2
M2_sw2_S_x = M2_cw2_S_x - 1
M2_sw2_S_y = M2_cw2_E_y
M2_sw2_E_x = M2_sw2_S_x + 6
M2_sw2_E_y = M2_sw2_S_y + 195 +67
map[M2_sw2_S_x:M2_sw2_E_x, M2_sw2_S_y:M2_sw2_E_y] = 0
#map[835:841,1037:1299] = 0
#Crosswalk 3
M2_cw3_S_x = M2_sw2_S_x + 1
M2_cw3_S_y = M2_sw2_E_y
M2_cw3_E_x = M2_cw3_S_x + 4
M2_cw3_E_y = M2_cw3_S_y + 15

map[M2_cw3_S_x:M2_cw3_E_x, M2_cw3_S_y:M2_cw3_E_y] = 0

# 3rd Sidewalk
M2_sw3_S_x = M2_cw3_S_x - 1
M2_sw3_S_y = M2_cw3_E_y
M2_sw3_E_x = M2_sw3_S_x + 6
M2_sw3_E_y = M2_sw3_S_y + 217
map[M2_sw3_S_x:M2_sw3_E_x, M2_sw3_S_y:M2_sw3_E_y] = 0

# 4th Crosswalk
M2_cw4_S_x = M2_sw3_S_x + 1
M2_cw4_S_y = M2_sw3_E_y
M2_cw4_E_x = M2_cw4_S_x + 4
M2_cw4_E_y = M2_cw4_S_y + 28

map[M2_cw4_S_x:M2_cw4_E_x, M2_cw4_S_y:M2_cw4_E_y] = 0

# Crosswalk back up
M_cw5 =M_cw4_E_y -4
print M_cw4_E_x, M2_cw4_S_x, M_cw5, M2_cw4_E_y

map[M_cw4_E_x:M2_cw4_S_x, M_cw5:M2_cw4_E_y] = 0


# Bobby Dodd Statium Sidewalks -
# East side  headed north 8 squares wide 457 long
BD_E_E_x = start
BD_E_E_y = start
BD_E_S_x = BD_E_E_x - 457
BD_E_S_y = BD_E_E_y - 8
#print BD_E_S_y, BD_E_S_x
map[BD_E_S_x:BD_E_E_x, BD_E_S_y:BD_E_E_y] = 0

# South Side  - 4 squares wide 505 long small parking lot at 408
BD_S_E_x = 804
BD_S_E_y = 800
BD_S_S_x = BD_E_E_x - 4
BD_S_S_y = BD_E_E_y - 505
# print BD_S_S_y, BD_S_S_x
map[BD_S_S_x:BD_S_E_x, BD_S_S_y:BD_S_E_y] = 0


# West side - no sidewalk
#Cherry Street 4 squares wide up to bobby dodd way 457
Cherry_E_x = BD_S_S_x
Cherry_E_y = BD_S_S_y + 4
Cherry_S_x = Cherry_E_x - 457
Cherry_S_y = Cherry_E_y - 4
# print 'Start', Cherry_S_y, Cherry_S_x, 'End', Cherry_E_y, Cherry_E_x
map[Cherry_S_x:Cherry_E_x, Cherry_S_y:Cherry_E_y] = 0


#North side - Bobby Dodd way 5 squares wide 505 long to cherry
BD_N_E_x = BD_E_S_x + 4
BD_N_E_y = BD_E_S_y +  8
BD_N_S_x = BD_N_E_x - 5
BD_N_S_y = BD_N_E_y - 505
# print BD_N_S_y, BD_N_S_x
map[BD_N_S_x:BD_N_E_x, BD_N_S_y:BD_N_E_y] = 0

# Corner

corner = np.tri(19,34,-1)
corner = np.fliplr(corner)
corner[corner == 0] = 'nan'
corner[corner == 1] = 0
s1 = start - 19 - 4
s2 = start - 34 - 8
map[s1:start-4,s2:start-8] = corner

#Exit locations

# Marta
M1 = M_cw4_S_x - 40
M2 = M_cw4_S_x
M3 = M_cw4_E_y
M4 = M_cw4_E_y + 40
# print M1, M2, M3, M4
map[M1:M2, M3:M4] = 50
plt.text(M3, M1, 'Marta')

# Varsity
V1 = M_sw2_S_x - 40
V2 = M_sw2_S_x
V3 = M_sw2_E_y
V4 = M_sw2_E_y + 40
# print V1, V2, V3, V4
map[V1:V2, V3:V4] = 50
plt.text(V3, V1, 'Varsity')

# North Ave
NA1 = N_sw2_S_x - 40
NA2 = N_sw2_S_x
NA3 = N_sw2_E_y
NA4 = N_sw2_E_y + 40
# print NA1, NA2, NA3, NA4
map[NA1:NA2, NA3:NA4] = 50
plt.text(NA3, NA1, 'North Ave Apt')

plt.imshow(map)
#plt.colorbar()
labels = ('Red - Locations \n'
          'Blue - Sidewalks')
plt.text(1650,600,labels)
plt.show()
