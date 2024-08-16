import numpy as np
import math  as m
import MDAnalysis as mda
import math as m
import MDAnalysis.transformations as trans
import sys

##############################################################
def trajectory_multiple(xtcfile, start, end):
	list_traj = []
	for i in range(start, end):
		list_traj.append(xtcfile + "." + str(i) + ".xtc")
	return list_traj
##############################################################
#GRO1       = "step5_assembly.psf"
GRO1       = "topol.tpr"
#GRO2       = "../../prod/equ.5.gro"
XTC       = "topol.xtc"
#XTC       = "prot_equil_2000-2500ns_TM_domain_centered.xtc"
##############################################################
OUTPUT5  =  open("grid_u.txt"        , "w")
OUTPUT6  =  open("grid_l.txt"        , "w")
comfile  =  open("prot_com.txt"        , "w")
helixu = np.zeros((7,3))
helixl = np.zeros((7,3))
##############################################################
STEP = 1
step  = 1
halfstep = step * 0.5
step_INV = 1.0 / step
list_traj = trajectory_multiple(XTC, 0, 1)
print (list_traj)
##############################################################
u = mda.Universe(GRO1,XTC)
#PROC = u.select_atoms('segid PROC')
#prob = u.select_atoms('segid seg_1_PROB')
cent = u.select_atoms('protein and resid 107 and name CA')
protein = u.select_atoms('protein')
protein_CA = u.select_atoms('protein and name CA')
#system = u.select_atoms('protein or segid MEMB')
system = u.select_atoms('protein or resname SOPC POPC DMPC')
s=8
h1u = u.select_atoms('protein and resid '+str(26-s)+':'+str(29-s))
h1l = u.select_atoms('protein and resid '+str(53-s)+':'+str(57-s))
h2l = u.select_atoms('protein and resid '+str(62-s)+':'+str(65-s))
h2u = u.select_atoms('protein and resid '+str(86-s)+':'+str(89-s))
h3u = u.select_atoms('protein and resid '+str(98-s)+':'+str(102-s))
h3l = u.select_atoms('protein and resid '+str(128-s)+':'+str(131-s))
h4l = u.select_atoms('protein and resid '+str(143-s)+':'+str(146-s))
h4u = u.select_atoms('protein and resid '+str(163-s)+':'+str(165-s))
h5u = u.select_atoms('protein and resid '+str(194-s)+':'+str(197-s))
h5l = u.select_atoms('protein and resid '+str(221-s)+':'+str(224-s))
h6l = u.select_atoms('protein and resid '+str(242-s)+':'+str(245-s))
h6u = u.select_atoms('protein and resid '+str(270-s)+':'+str(273-s))
h7u = u.select_atoms('protein and resid '+str(280-s)+':'+str(283-s))
h7l = u.select_atoms('protein and resid '+str(306-s)+':'+str(309-s))

transforms = [trans.unwrap(system), trans.center_in_box(protein_CA), trans.wrap(system), trans.unwrap(system)]
u.trajectory.add_transformations(*transforms)

N_frames         = len(u.trajectory)
X_length         = u.dimensions[0]
Y_length         = u.dimensions[1]
#START		 = int(0.5 * N_frames)
#START		 = int(0.5 * N_frames)

## We are analyzing from 4 to 5 us. The trajectories are saved every 480 ps (stride of 2 frames per the original 240 ps write frequency)
## START = 4,000,000 ps / 480 ps = 8,330
## END   = 5,000,000 ps / 480 ps = 10,420
START = 60416
END   = 62650

##############################################################
print ("Trajectory is read :-)" )
print ("Number of frames: " + str(N_frames))
print ("The dimention of the box in x-y plane: x = " + str(X_length) + " and y = " + str(Y_length))
print ("-------------------------------------")
##############################################################
x_max =  70
y_max =  70
x_min =  -5
y_min =  -5

N       = int((x_max - x_min) * step_INV) + 1
M       = int((y_max - y_min) * step_INV) + 1
C_u     = np.zeros((N, M, 2))
C_l     = np.zeros((N, M, 2))
initial_selection = u.select_atoms("name P")
COM               = initial_selection.center_of_geometry()
Z_c               = COM[2]
##############################################################
c=0
for ts in u.trajectory[START:END:STEP]:

	#print (str(ts.frame) + " out of " + str(N_frames))
	print (str(ts.frame) + " out of " + str(END))
	#tmp = protein_CA.center_of_mass()
	#print(tmp)
	#comfile.write('{0} {1} {2} {3}\n'.format(ts.frame, tmp[0], tmp[1], tmp[2]))
	upper = u.select_atoms("(name P and prop z > " + str(Z_c) + ")")
	U     = upper.positions
	lower = u.select_atoms("(name P and prop z < " + str(Z_c) + ")")
	L     = lower.positions

	x_u     = U[:,0]
	y_u     = U[:,1]
	z_u     = U[:,2]

	x_l     = L[:,0]
	y_l     = L[:,1]
	z_l     = L[:,2]

	length = len(x_u)
	length_INV = 1.0 / len(x_u)
	for k in range(0, length):
		I = int((x_u[k] - x_min) * step_INV)
		J = int((y_u[k] - y_min) * step_INV)
		C_u[I][J][0] = C_u[I][J][0] + 1
		C_u[I][J][1] = C_u[I][J][1] + z_u[k]

	length = len(x_l)
	length_INV = 1.0 / len(x_l)
	for k in range(0, length):
		I = int((x_l[k] - x_min) * step_INV)
		J = int((y_l[k] - y_min) * step_INV)
		C_l[I][J][0] = C_l[I][J][0] + 1
		C_l[I][J][1] = C_l[I][J][1] + z_l[k]
	
	helixu[0] += h1u.center_of_mass()
	helixl[0] += h1l.center_of_mass()
	helixu[1] += h2u.center_of_mass()
	helixl[1] += h2l.center_of_mass()
	helixu[2] += h3u.center_of_mass()
	helixl[2] += h3l.center_of_mass()
	helixu[3] += h4u.center_of_mass()
	helixl[3] += h4l.center_of_mass()
	helixu[4] += h5u.center_of_mass()
	helixl[4] += h5l.center_of_mass()
	helixu[5] += h6u.center_of_mass()
	helixl[5] += h6l.center_of_mass()
	helixu[6] += h7u.center_of_mass()
	helixl[6] += h7l.center_of_mass()
	c+=1

helixu /= c
helixl /= c

np.savetxt('helices_u.txt', helixu)
np.savetxt('helices_l.txt', helixl)

z_u_ave = np.mean(z_u)
z_l_ave = np.mean(z_l)
##############################################################
for i in range(0, N):
	for j in range(0 , M):
		if C_u[i][j][0] != 0:
			OUTPUT5.write('{}    '.format(x_min + i * step + halfstep))
			OUTPUT5.write('{}    '.format(y_min + j * step + halfstep))
			OUTPUT5.write('{}  \n'.format(C_u[i][j][1] / C_u[i][j][0]))

		if C_u[i][j][0] == 0:
			OUTPUT5.write('{}    '.format(x_min + i * step + halfstep))
			OUTPUT5.write('{}    '.format(y_min + j * step + halfstep))
			OUTPUT5.write('{}  \n'.format(z_u_ave))
			#OUTPUT5.write('NAN  \n')

for i in range(0, N):
	for j in range(0 , M):
		if C_l[i][j][0] != 0:
			OUTPUT6.write('{}    '.format(x_min + i * step + halfstep))
			OUTPUT6.write('{}    '.format(y_min + j * step + halfstep))
			OUTPUT6.write('{}  \n'.format(C_l[i][j][1] / C_l[i][j][0]))


		if C_l[i][j][0] == 0:
			OUTPUT6.write('{}    '.format(x_min + i * step + halfstep))
			OUTPUT6.write('{}    '.format(y_min + j * step + halfstep))
			OUTPUT6.write('{}  \n'.format(z_l_ave))
			#OUTPUT6.write('NAN  \n')
