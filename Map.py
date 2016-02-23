# Creating matrix to represent a map of Bobby-Statium and the surrounding areas


# Finish exits
# Look up code for visualization
import numpy as np
from matplotlib import pyplot as plt

# Creating empty Map
map = np.empty((1100, 1600,)) * np.NAN

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

Mcw1_loc = [(M_cw1_S_x,M_cw1_S_y)]
i=0
while i<=3:
    j=0
    while j<=41:
        num = M_cw1_S_x + i
        num2 = M_cw1_S_y +j
        Mcw1_new = (num,num2)
        Mcw1_loc.append(Mcw1_new)
        j=j+1
    i=i+1

#print Mcw1_loc
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

Mcw2_loc = [(M_cw2_S_x,M_cw2_S_y)]
i=0
while i<=3:
    j=0
    while j<=18:
        num = M_cw2_S_x + i
        num2 = M_cw2_S_y +j
        Mcw2_new = (num,num2)
        Mcw2_loc.append(Mcw2_new)
        j=j+1
    i=i+1


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

Mcw3_loc = [(M_cw3_S_x,M_cw3_S_y)]
i=0
while i<=3:
    j=0
    while j<=14:
        num = M_cw3_S_x + i
        num2 = M_cw3_S_y +j
        Mcw3_new = (num,num2)
        Mcw3_loc.append(Mcw3_new)
        j=j+1
    i=i+1


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

Mcw4_loc = [(M_cw4_S_x,M_cw4_S_y)]
i=0
while i<=3:
    j=0
    while j<=26:
        num = M_cw4_S_x + i
        num2 = M_cw4_S_y +j
        Mcw4_new = (num,num2)
        Mcw4_loc.append(Mcw4_new)
        j=j+1
    i=i+1

# Corner

corner = np.tri(19,34,-1)
corner = np.fliplr(corner)
corner[corner == 0] = 'nan'
corner[corner == 1] = 0
s1 = start - 19 - 4
s2 = start - 34 - 8
map[s1:start-4,s2:start-8] = corner
#print s1,s2

# Creating Pathway to NorthAve Apartments

# 1st crosswalk - 32 spaces south
N_cw1_S_x = M_cw1_S_x
N_cw1_S_y = 800 - 4
N_cw1_E_x = N_cw1_S_x + 32
N_cw1_E_y = N_cw1_S_y + 4

map[N_cw1_S_x:N_cw1_E_x, N_cw1_S_y:N_cw1_E_y] = 0

Ncw1_loc = [(N_cw1_S_x,N_cw1_S_y)]
i=0
while i<=3:
    j=0
    while j<=31:
        num = N_cw1_S_x + j
        num2 = N_cw1_S_y + i
        Ncw1_new = (num,num2)
        Ncw1_loc.append(Ncw1_new)
        j=j+1
    i=i+1


# 2nd Crosswalk - 42 spaces East
N_cw2_S_x = N_cw1_E_x
N_cw2_S_y = N_cw1_S_y
N_cw2_E_x = N_cw2_S_x + 4
N_cw2_E_y = N_cw2_S_y + 42
#print N_cw2_E_x, N_cw2_E_y
map[N_cw2_S_x:N_cw2_E_x, N_cw2_S_y:N_cw2_E_y] = 0

Ncw2_loc = [(N_cw2_S_x,N_cw2_S_y)]
i=0
while i<=3:
    j=0
    while j<=41:
        num = N_cw2_S_x + i
        num2 = N_cw2_S_y +j
        Ncw2_new = (num,num2)
        Ncw2_loc.append(Ncw2_new)
        j=j+1
    i=i+1


# Crosswalk back up
N_cw3_S_x = M_cw1_S_x
N_cw3_S_y = 800 + 42
N_cw3_E_x = N_cw3_S_x + 32
N_cw3_E_y = N_cw3_S_y + 4

map[N_cw3_S_x:N_cw3_E_x, N_cw3_S_y:N_cw3_E_y] = 0

Ncw3_loc = [(N_cw3_S_x,N_cw3_S_y)]
i=0
while i<=3:
    j=0
    while j<=31:
        num = N_cw3_S_x + j
        num2 = N_cw3_S_y + i
        Ncw3_new = (num,num2)
        Ncw3_loc.append(Ncw3_new)
        j=j+1
    i=i+1

# Sidewalk 185 spaces south
N_sw1_S_x = N_cw2_S_x
N_sw1_S_y = N_cw2_E_y
N_sw1_E_x = N_sw1_S_x + 189
N_sw1_E_y = N_sw1_S_y + 4
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
M2_sw1_S_y = N_cw2_E_y +4
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


M2cw2_loc = [(M2_cw2_S_x,M2_cw2_S_y)]
i=0
while i<=3:
    j=0
    while j<=41:
        num = M2_cw2_S_x + i
        num2 = M2_cw2_S_y +j
        M2cw2_new = (num,num2)
        M2cw2_loc.append(M2cw2_new)
        j=j+1
    i=i+1


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

M2cw3_loc = [(M2_cw3_S_x,M2_cw3_S_y)]
i=0
while i<=3:
    j=0
    while j<=41:
        num = M2_cw3_S_x + i
        num2 = M2_cw3_S_y +j
        M2cw3_new = (num,num2)
        M2cw3_loc.append(M2cw3_new)
        j=j+1
    i=i+1

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

M2cw4_loc = [(M2_cw4_S_x,M2_cw4_S_y)]
i=0
while i<=3:
    j=0
    while j<=41:
        num = M2_cw4_S_x + i
        num2 = M2_cw4_S_y +j
        M2cw4_new = (num,num2)
        M2cw4_loc.append(M2cw4_new)
        j=j+1
    i=i+1

# Crosswalk back up
M_cw5 =M_cw4_E_y -4
# print M_cw4_E_x, M2_cw4_S_x, M_cw5, M2_cw4_E_y

map[M_cw4_E_x:M2_cw4_S_x, M_cw5:M2_cw4_E_y] = 0


# Bobby Dodd Statium Sidewalks -
# East side  headed north 8 squares wide 457 long
BD_E_E_x = start
BD_E_E_y = start
BD_E_S_x = BD_E_E_x - 457
BD_E_S_y = BD_E_E_y - 8
#print BD_E_S_y, BD_E_S_x
map[BD_E_S_x:BD_E_E_x, BD_E_S_y:BD_E_E_y] = 0

# Across the street
BD2_E_E_x = start
BD2_E_E_y = start +50
BD2_E_S_x = BD2_E_E_x - 457
BD2_E_S_y = BD2_E_E_y - 8
#print BD_E_S_y, BD_E_S_x
map[BD2_E_S_x:BD2_E_E_x, BD2_E_S_y:BD2_E_E_y] = 0
# crosswalk
BD_cw1_S_x = start - 457
BD_cw1_S_y = start
BD_cw1_E_x = BD_cw1_S_x + 4
BD_cw1_E_y = BD_cw1_S_y + 42

map[BD_cw1_S_x:BD_cw1_E_x, BD_cw1_S_y:BD_cw1_E_y] = 0
print BD_cw1_S_x, BD_cw1_E_x,BD_cw1_S_y, BD_cw1_E_y


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

#Plaza
P_N_S_x = BD_N_E_x
P_N_S_y = BD_N_E_y -79
P_N_E_x = P_N_S_x + 76
P_N_E_y = P_N_S_y -107
map[P_N_S_x:P_N_E_x,P_N_E_y:P_N_S_y] = 0

# Path to gate B
PB_S_x = P_N_S_x
PB_S_y = P_N_E_y -73
PB_E_x = PB_S_x + 123
PB_E_y = PB_S_y + 23
map[PB_S_x:PB_E_x,PB_S_y:PB_E_y] = 0
#print PB_S_x,PB_E_x,PB_S_y,PB_E_y

# Path to Peters Parking Deck
PP_S_x = PB_S_x - 267
PP_S_y = PB_S_y - 11
PP_E_x = PB_S_x
PP_E_y = PB_S_y
map[PP_S_x:PP_E_x,PP_S_y:PP_E_y] = 0
# print PP_S_x,PP_S_y,PP_E_x,PP_E_y


#Exit locations
# Peter's exit
PP_loc = [(PP_S_x,PP_E_y)]
i=0
while i<=15:
    num = PP_S_x + i
    PPnew = (num,PP_E_y)
    PP_loc.append(PPnew)
    map[num, PP_E_y] = 50
    i=i+1
plt.text(PP_E_y, PP_S_x, 'Peters Parking Deck')

# Entrance to east campus dorms - 103 spaces north of north ave
EC_S_x =M_sw1_S_x - 103
EC_S_y = M_sw1_S_y + 8
EC_loc = [(EC_S_x, EC_S_y)]
i=0
while i<=15:
    num = EC_S_x + i
    ECnew = (num,EC_S_y)
    EC_loc.append(ECnew)
    map[num, EC_S_y] = 50
    i=i+1
plt.text(EC_S_y, EC_S_x, 'East Campus Dorms')

# Bus stop
BS_S_x =M_sw1_E_x
BS_S_y = M_sw1_S_y + 8
BS_loc = [(BS_S_x, BS_S_y)]
i=0
while i<=15:
    num = BS_S_y + i
    BSnew = (BS_S_x, num)
    BS_loc.append(BSnew)
    map[BS_S_x,num] = 50
    i=i+1
plt.text(BS_S_y, BS_S_x, 'Bus Stop')


# To the student Center - 187 squares north of North Ave on Cherry Street
SC_S_x =Cherry_E_x - 187
SC_S_y = Cherry_S_y
SC_loc = [(SC_S_x, SC_S_y)]
i=0
while i<=15:
    num = SC_S_x + i
    SCnew = (num,SC_S_y)
    SC_loc.append(SCnew)
    map[num, SC_S_y] = 50
    i=i+1
plt.text(SC_S_y, SC_S_x, 'To the Student Center')





# Marta
M1 = M_cw4_S_x - 40
M2 = M_cw4_S_x
M3 = M_cw4_E_y
M4 = M_cw4_E_y + 40
# print M1, M2, M3, M4
map[M1:M2, M3:M4] = 50
plt.text(M3, M1, 'Marta')
Mloc = [(M_cw4_S_x,M_cw4_E_y)]
i=1
while i<=3:
    num = M_cw4_S_x + i
    Mnew = (num,M_cw4_E_y)
    Mloc.append(Mnew)
    i=i+1
# print Mloc

# Varsity
V1 = M_sw2_S_x - 40
V2 = M_sw2_S_x
V3 = M_sw2_E_y
V4 = M_sw2_E_y + 40
# print V1, V2, V3, V4
map[V1:V2, V3:V4] = 50
plt.text(V3, V1, 'Varsity')
Vloc = [(V2,V3)]
i=1
while i<=15:
    num = V3+i
    Vnew = (V2,num)
    Vloc.append(Vnew)
    i=i+1

# North Ave
NA1 = N_sw2_S_x - 40
NA2 = N_sw2_S_x
NA3 = N_sw2_E_y
NA4 = N_sw2_E_y + 40
# print NA1, NA2, NA3, NA4
map[NA1:NA2, NA3:NA4] = 50
plt.text(NA3, NA1, 'North Ave Apt')
NAloc = [(N_sw2_S_x,N_sw2_E_y)]
i=1
while i<=3:
    num = N_sw2_S_x + i
    NAnew = (num,N_sw2_E_y)
    NAloc.append(NAnew)
    i=i+1

# Gates
# Gate C
C1 = 796
C2 = 758
Cloc = [(C1,C2)]
i=1
while i<=15:
    num = C1+i
    num2 = C2 -1
    Cnew = (num,num2)
    Cloc.append(Cnew)
    i=i+1
plt.text(C2, C1-20, 'Gate C')

# Gate A - sixteen spaces wide
A1 = start - 6
A2 = A1 + 2
A3 = start - 109
A4 = A3 + 16
map[A1:A2,A3:A4] = 50
plt.text(A3-100, A1-15, 'Gate A')
Aloc = [(A2,A3)]
i=1
while i<=15:
    num = A3+i
    Anew = (A2,num)
    Aloc.append(Anew)
    i=i+1
# print Aloc


# Gate B
B1 = PB_E_x - 12
B2 = PB_E_x
B3 = PB_E_y
B4 = PB_E_y + 1
map[B1:B2,B3:B4] = 50
plt.text(B3 - 50, B1+50, 'Gate B')
Bloc = [(B2,B3)]
i=1
while i<=15:
    num = B2 + i
    Bnew = (num,B3)
    Bloc.append(Bnew)
    i=i+1
# print Bloc


# Gate D
D1 = P_N_E_x
D2 = P_N_E_x + 1
D3 = P_N_S_y - 55
D4 = D3 + 12
map[D1:D2,D3:D4] = 50
plt.text(D3,D1+30, 'Gate D')
Dloc = [(D2,D3)]
i=1
while i<=15:
    num = D3+i
    Dnew = (D2,num)
    Dloc.append(Dnew)
    i=i+1
# print Dloc


# Gate E
E1 =BD_E_S_x + 100
E2 = E1 + 12
E3 = start
E4 = E3 + 2
map[E1:E2,E3:E4] = 50
plt.text(E3+10,E1+30, 'Gate E')
Eloc = [(E2,E3)]
i=1
while i<=15:
    num = E2 + i
    Enew = (num,E3)
    Eloc.append(Enew)
    i=i+1
# print Eloc
plt.imshow(map)
#plt.colorbar()
labels = ('Red - Locations \n'
          'Blue - Sidewalks')
plt.text(1650,600,labels)
plt.show()
Gates = {'Gate A':Aloc,'Gate B':Bloc,'Gate C':Cloc,'Gate D':Dloc,'Gate E':Eloc}
# print Aloc
Exits = {'Marta':Mloc,'Varsity':Vloc,'North Ave':NAloc, 'Peters Parking Deck':PP_loc, 'East Campus Dorms':EC_loc,'Bus Stop':BS_loc, 'Student Center':SC_loc}
Crosswalks = {'Marta CW1':Mcw1_loc, 'Marta CW2':Mcw2_loc, 'Marta CW3':Mcw3_loc, 'Marta CW4':Mcw4_loc,'North Ave CW1':Ncw1_loc, 'North Ave CW2':Ncw2_loc, 'North Ave CW3':Mcw3_loc, 'Marta 2 CW2':M2cw2_loc,'Marta 2 CW3':M2cw3_loc, 'Marta 2 CW4':M2cw4_loc}





