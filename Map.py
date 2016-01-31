# Creating matrix to represent a map of Bobby-Statium and the surrounding areas
import numpy as np
from matplotlib import pyplot as plt

# Creating empty Map
map = np.empty((1600, 1600,)) * np.NAN

# Creating pathway to MARTA

# 1st crosswalk
##CW1 = np.ones((4,38,))
map[800:804,800:842] = 1
# 1st Sidewalk
##SW1 = np.ones((5,176,))
map[800:805,842:1018] = 1
# 2nd Crosswalk
map[800:804,1018:1037] = 1
# 2nd Sidewalk part 1 - up to Varsity
map[799:805,1037:1232] = 1
# 2nd Sidewalk part 2
map[799:805,1232:1299] = 1
# 3rd Crosswalk
map[800:804, 1299:1314] = 1
# 3rd Sidewalk
map[799:805, 1314:1531] = 1
# 4th Crosswalk
map[800:804, 1531:1558] = 1


# Creating Pathway to NorthAve Apartments

#1st crosswalk - 32 spaces south
map[804:836,800:804] = 1
# 2nd Crosswalk - 42 spaces East
map[836:840,800:842] = 1
# Sidewalk 185 spaces south
map[840:1028,842:845] = 1
# Drive to gate - 60 spaces east
map[1024:1028,845:905] = 1

# Other side of street to Marta
# sidewalk 1
map[836:841,842:1018] = 1
# Crosswalk 2
map[836:840,1018:1037] = 1
# Sidewalk 2
map[835:841,1037:1299] = 1
#Crosswalk 3
map[836:840,1299:1314] = 1
#Sidewalk 3
map[835:841,1314:1531] = 1
#Crosswalk 4
map[836:840,1531:1558] = 1



plt.imshow(map)
plt.colorbar()
plt.show()