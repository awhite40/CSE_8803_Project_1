# Creating matrix to represent a map of Bobby-Statium and the surrounding areas
import numpy as np
from matplotlib import pyplot as plt

# Creating empty Map
map = np.empty((1600, 1600,)) * np.NAN

# Creating pathway to MARTA

# 1st crosswalk

M_cw1_S_x = 800
M_cw1_S_y = 800
M_cw1_E_x = M_cw1_S_x + 4
M_cw1_E_y = M_cw1_S_y + 42

print M_cw1_E_x, M_cw1_E_y
#M_cw1_E = (M_cw1_S[0] + 4, M_cw1_S[1] + 42)
map[M_cw1_S_x:M_cw1_E_x, M_cw1_S_y:M_cw1_E_y] = 0

# 1st Sidewalk

M_sw1_S_x = M_cw1_S_x
M_sw1_S_y = M_cw1_E_y
M_sw1_E_x = M_sw1_S_x + 5
M_sw1_E_y = M_sw1_S_y + 176

print M_sw1_S_x, M_sw1_S_y, M_sw1_E_x, M_sw1_E_y
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
N_cw1_S_x = M_cw1_S_x + 4
N_cw1_S_y = 800
N_cw1_E_x = M_cw1_S_x + 32
N_cw1_E_y = M_cw1_S_y + 4

map[N_cw1_S_x:N_cw1_E_x, N_cw1_S_y:N_cw1_E_y] = 0


# 2nd Crosswalk - 42 spaces East
N_cw2_S_x = N_cw1_E_x
N_cw2_S_y = N_cw1_S_y
N_cw2_E_x = N_cw2_S_x + 4
N_cw2_E_y = N_cw2_S_y + 42
print N_cw2_E_x, N_cw2_E_y
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
map[836:841,842:1018] = 0
# Crosswalk 2
map[836:840,1018:1037] = 0
# Sidewalk 2
map[835:841,1037:1299] = 0
#Crosswalk 3
map[836:840,1299:1314] = 0
#Sidewalk 3
map[835:841,1314:1531] = 0
#Crosswalk 4
map[836:840,1531:1558] = 0



plt.imshow(map)
plt.colorbar()
plt.show()
