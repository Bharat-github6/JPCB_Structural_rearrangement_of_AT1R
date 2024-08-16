import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 16})

# Open files
with open('grid_u.txt', 'r') as fileID_u, open('grid_l.txt', 'r') as fileID_l:
    # Read data
    U = np.fromstring(fileID_u.read(), sep=' ').reshape(-1, 3)
    L = np.fromstring(fileID_l.read(), sep=' ').reshape(-1, 3)

helixu = np.loadtxt('helices_u.txt')
helixl = np.loadtxt('helices_l.txt')

labels=['TM1', 'TM2', 'TM3', 'TM4', 'TM5', 'TM6', 'TM7']

# Define limits
MIN_x = -2
MAX_x = 74
MIN_y = -2
MAX_y = 74

# Filter data
mask_u = (MIN_x < U[:, 0]) & (U[:, 0] < MAX_x) & (MIN_y < U[:, 1]) & (U[:, 1] < MAX_y)
mask_l = (MIN_x < L[:, 0]) & (L[:, 0] < MAX_x) & (MIN_y < L[:, 1]) & (L[:, 1] < MAX_y)

x_u, y_u, z_u = U[mask_u].T
x_l, y_l, z_l = L[mask_l].T

#z_u_const = ma.masked_where(z_u != U[0,2], z_u)
#z_l_const = ma.masked_where(z_l != L[0,2], z_l)
#print(z_u_const.compressed())
#print(z_l_const)

# Create grid
delta_x = 1
delta_y = 1
X_u = np.arange(x_u[0], x_u[-1] + delta_x, delta_x)
Y_u = np.arange(y_u[0], y_u[-1] + delta_y, delta_y)
X_l = np.arange(x_l[0], x_l[-1] + delta_x, delta_x)
Y_l = np.arange(y_l[0], y_l[-1] + delta_y, delta_y)

# Interpolate data
Z_u = np.zeros((len(Y_u), len(X_u)))
Z_l = np.zeros((len(Y_l), len(X_l)))

for i in range(len(X_u)):
    for j in range(len(Y_u)):
        k = j + i * len(Y_u)
        Z_u[j, i] = z_u[k]

for i in range(len(X_l)):
    for j in range(len(Y_l)):
        k = j + i * len(Y_l)
        Z_l[j, i] = z_l[k]

Z_u_const = ma.masked_where(Z_u != U[0,2], Z_u)
Z_l_const = ma.masked_where(Z_l != L[0,2], Z_l)

#zmin=2
#zmax=34
#levels = np.linspace(zmin, zmax, 17)

zmin=12
zmax=30
levels = np.linspace(zmin, zmax, 10)

# Plot upper surface
fig,ax = plt.subplots()
cs = ax.contourf(X_u, Y_u, Z_u - 0.5 * (np.mean(z_u) + np.mean(z_l)), levels=levels)
#ax.contour(cs, colors='k', lw=1)
for c in cs.collections:
    c.set_rasterized(True)
cbar = fig.colorbar(cs,  orientation='vertical', pad=-0.2)
cbar.ax.tick_params(labelsize=16)
cbar.set_label(label=r'Thickness ($\mathrm{\AA}$)', fontsize=16)
ax.contourf(X_u, Y_u, Z_u_const - 0.5 * (np.mean(z_u) + np.mean(z_l)), 1, colors='white', linewidth=1, rasterize=True)
for i in range(7):
    circle = plt.Circle((helixu[i,0], helixu[i,1]), 4, color='mistyrose', ec='k', lw=1)
    ax.add_patch(circle)
    ax.text(helixu[i,0], helixu[i,1], labels[i], ha='center', va='center_baseline', fontsize=10, weight='bold')

#plt.colorbar(label=r'Thickness ($\AA$)', ticks=np.linspace(7, 30, 5), orientation='vertical')

plt.axis('scaled')
plt.xlabel(r'$x \ (\mathrm{\AA})$')
plt.ylabel(r'$y \ (\mathrm{\AA})$')
#plt.xticks(np.arange(0, 201, 50))
#plt.yticks(np.arange(0, 201, 50))
#plt.axis([0, 72, 0, 72])
plt.xticks(np.arange(0, 65, 10))
plt.yticks(np.arange(0, 65, 10))
plt.xlim((0,62))
plt.ylim((0,62))
plt.tight_layout(rect=[-0.15,-0.05,1.06,1.03])
fig.set_figwidth(5.8)
plt.savefig('thickness_upper.png', dpi=600)
plt.savefig('thickness_upper.svg', dpi=600)
plt.close()

# Plot lower surface
fig,ax = plt.subplots()
cs = ax.contourf(X_l, Y_l, -Z_l + 0.5 * (np.mean(z_u) + np.mean(z_l)), levels=levels)
#plt.colorbar(label=r'$z \ (\AA)$', ticks=np.linspace(7, 30, 5), orientation='vertical')
#cbar = plt.colorbar(label=r'$z \ (\mathrm{\AA})$', orientation='vertical')
for c in cs.collections:
    c.set_rasterized(True)
cbar = fig.colorbar(cs,  orientation='vertical', pad=-0.2)
cbar.ax.tick_params(labelsize=16)
cbar.set_label(label=r'Thickness ($\mathrm{\AA}$)', fontsize=16)
ax.contourf(X_l, Y_l, Z_l_const - 0.5 * (np.mean(z_u) + np.mean(z_l)), 1, colors='white', linewidth=1)
for i in range(7):
    circle = plt.Circle((helixl[i,0], helixl[i,1]), 4, color='mistyrose', ec='k', lw=1)
    ax.add_patch(circle)
    ax.text(helixl[i,0], helixl[i,1], labels[i], ha='center', va='center_baseline', fontsize=10, weight='bold')


plt.axis('square')
plt.xlabel(r'$x \ (\mathrm{\AA})$')
plt.ylabel(r'$y \ (\mathrm{\AA})$')
plt.xticks(np.arange(0, 65, 10))
plt.yticks(np.arange(0, 65, 10))
#plt.axis([0, 72, 0, 72])
plt.xlim((0,62))
plt.ylim((0,62))
plt.tight_layout(rect=[-0.15,-0.05,1.06,1.03])
fig.set_figwidth(5.8)
plt.savefig('thickness_lower.png', dpi=600)
plt.savefig('thickness_lower.svg', dpi=600)

