from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,MultipleLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Rectangle
#from pandas import rolling_mean
import pandas as pd
import numpy as np
import matplotlib

params = {'legend.fontsize': 20,
          'legend.handlelength': 5}

matplotlib.rc('xtick', labelsize=11)
matplotlib.rc('ytick', labelsize=11)
#use('Agg')
font = {'family' : 'sans serif', 'size' : '10'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=0.9)

simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)


ST5_r1= pd.read_csv('ST5_rep1', delim_whitespace=True)
ST5_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST5_r1=ST5_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
ST5_r1=ST5_r1[0:2084]
time_ST5r1=np.linspace(0,5, len(ST5_r1))

ST5_r2= pd.read_csv('ST5_rep2', delim_whitespace=True)
ST5_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST5_r2=ST5_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_ST5r2=np.linspace(0,5, len(ST5_r2))

ST5=pd.concat([ST5_r1,ST5_r2], axis=1)


ST10_r1= pd.read_csv('ST_10_rep1_20us', delim_whitespace=True)
ST10_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST10_r1=ST10_r1[0:2084]
ST10_r1=ST10_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_ST10r1=np.linspace(0,5, len(ST10_r1))

ST10_r2= pd.read_csv('ST10_rep2', delim_whitespace=True)
ST10_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST10_r2=ST10_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_ST10r2=np.linspace(0,5, len(ST10_r2))

ST10=pd.concat([ST10_r1, ST10_r2], axis=1)


ST15_r1= pd.read_csv('ST15rep1', delim_whitespace=True)
ST15_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST15_r1=ST15_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
#ST15_r1=sopc_r1[0:2084]
time_ST15r1=np.linspace(0,5, len(ST15_r1))

ST15_r2= pd.read_csv('ST15_rep2', delim_whitespace=True)
ST15_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST15_r2=ST15_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
#sopc_r2=sopc_r2[0:2084]
time_ST15r2=np.linspace(0,5, len(ST15_r2))

ST15=pd.concat([ST15_r1, ST15_r2], axis=1)

ST20_r1= pd.read_csv('ST20_rep1', delim_whitespace=True)
ST20_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST20_r1=ST20_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
#ST15_r1=sopc_r1[0:2084]
time_ST20r1=np.linspace(0,5, len(ST20_r1))

ST20_r2= pd.read_csv('ST20_rep2', delim_whitespace=True)
ST20_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
ST20_r2=ST20_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
#ST20_r2=sopc_r2[0:2084]
time_ST20r2=np.linspace(0,5, len(ST20_r2))

ST20=pd.concat([ST20_r1, ST20_r2], axis=1)



window = 8

ax=plt.subplot(2,3,1)
ax.plot(time_ST5r2,(ST5_r2[['TM1-TM6']].rolling(window).mean()*10),color='tab:green')
ax.plot(time_ST10r2,(ST10_r2[['TM1-TM6']].rolling(window).mean()*10),color='tab:red')
ax.plot(time_ST15r2,(ST15_r2[['TM1-TM6']].rolling(window).mean()*10), color='tab:blue')
ax.plot(time_ST20r2,(ST20_r2[['TM1-TM6']].rolling(window).mean()*10), color='grey')
width=0.3
start=5.5
sp = 0.4

box_parts = ax.boxplot((ST5[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax.boxplot((ST10[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

box_parts = ax.boxplot((ST15[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax.boxplot((ST20[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax.set_ylim(10,37)
ax.set_xlim(0,5)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.set_ylabel('F55$^{1.59}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax.set_title('TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax.set_title('TM1-TM6 (\mathrm{C_\{alpha}}-\mathrm{C_\{alpha}})', fontsize=12)
ax.set_xlim(0,5)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,10),2, 27, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)

ax1=plt.subplot(2,3,2)

ax1.plot(time_ST5r2,(ST5_r2[['TM3-TM6']].rolling(window).mean()*10),color='tab:green')
ax1.plot(time_ST10r2,(ST10_r2[['TM3-TM6']].rolling(window).mean()*10),color='tab:red')
ax1.plot(time_ST15r2,(ST15_r2[['TM3-TM6']].rolling(window).mean()*10), color='tab:blue')
ax1.plot(time_ST20r2,(ST20_r2[['TM3-TM6']].rolling(window).mean()*10), color='grey')
width=0.3
start=5.5
sp = 0.4

box_parts = ax1.boxplot((ST5[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax1.boxplot((ST10[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

box_parts = ax1.boxplot((ST15[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)
    
box_parts = ax1.boxplot((ST20[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,6), 2, 16, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)

ax1.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
ax1.set_ylim(6,22)
ax1.set_xlim(0,5)
ax1.set_ylabel('R126$^{3.50}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax1.set_title('TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax1.set_title('TM3-TM6 (\mathrm{C_{\alpha}}-\mathrm{C_{\alpha}})', fontsize=12)
#ax1.set_ylabel('TM3-TM6 Dist. ($\AA$)', fontsize=14)
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax1.yaxis.set_major_locator(MultipleLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_major_locator(MaxNLocator(5))

ax2=plt.subplot(2,3,3)
ax2.plot(time_ST5r2,(ST5_r2[['NpxxY']].rolling(window).mean()*10),color='tab:green')
ax2.plot(time_ST10r2,(ST10_r2[['NpxxY']].rolling(window).mean()*10),color='tab:red')
ax2.plot(time_ST15r2,(ST15_r2[['NpxxY']].rolling(window).mean()*10), color='tab:blue')
ax2.plot(time_ST20r2,(ST20_r2[['NpxxY']].rolling(window).mean()*10), color='grey')
width=0.3
start=5.5
sp = 0.4

box_parts = ax2.boxplot((ST5[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax2.boxplot((ST10[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

box_parts = ax2.boxplot((ST15[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)
    
box_parts = ax2.boxplot((ST20[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((5.2,2), 2, 33, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
ax2.set_xlim(0,5)
ax2.axhline(y=5, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=12, linestyle='--', lw=1.5, color='0.5')
ax2.set_ylim(2,35)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax2.set_ylabel('Y215$^{5.58}$-Y302$^{7.53}$ ($\AA$)', fontsize=12)
ax2.set_title('TM5-TM7 (OH-OH)', fontsize=12)
#ax2.set_ylabel('NPxxY Dist. ($\AA$)', fontsize=11)
ax2.yaxis.set_major_locator(MultipleLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
ax2.xaxis.set_major_locator(MaxNLocator(5))


ax3=plt.subplot(2,3,4)
ax3.plot(time_ST5r2,(ST5_r2[['N300_S115']].rolling(window).mean()*10),color='tab:green')
ax3.plot(time_ST10r2,(ST10_r2[['N300_S115']].rolling(window).mean()*10),color='tab:red')
ax3.plot(time_ST15r2,(ST15_r2[['N300_S115']].rolling(window).mean()*10), color='tab:blue')
ax3.plot(time_ST20r2,(ST20_r2[['N300_S115']].rolling(window).mean()*10), color='grey')
width=0.3
start=5.5
sp = 0.4

box_parts = ax3.boxplot((ST5[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax3.boxplot((ST10[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

box_parts = ax3.boxplot((ST15[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)
    
box_parts = ax3.boxplot((ST20[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((5.2,4), 2, 9, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)

ax3.set_ylabel('S115$^{3.39}$-N295$^{7.46}$ ($\AA$)', fontsize=12)
ax3.set_title('TM3-TM7 (COM-COM)', fontsize=12)
#ax3.set_ylabel( 'TM3-TM7 Dist. ($\AA$)', fontsize=11)
ax3.axhline(y=9.0, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=6.12, linestyle='--', lw=1.5, color='tab:orange')
ax3.set_ylim(4,13)
ax3.set_xlim(0,5)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax3.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_major_locator(MaxNLocator(5))

ax6=plt.subplot(2,3,5)

ax6.plot(time_ST5r2,(ST5_r2[['L78_Y297']].rolling(window).mean()*10),color='tab:green',label='$\gamma=$ 5 mN/m')
ax6.plot(time_ST10r2,(ST10_r2[['L78_Y297']].rolling(window).mean()*10),color='tab:red',label='$\gamma=$ 10 mN/m')
ax6.plot(time_ST15r2,(ST15_r2[['L78_Y297']].rolling(window).mean()*10), color='tab:blue',label='$\gamma=$ 15 mN/m')
ax6.plot(time_ST20r2,(ST20_r2[['L78_Y297']].rolling(window).mean()*10), color='grey',label='$\gamma=$ 20 mN/m')
width=0.3
start=5.5
sp = 0.4

box_parts = ax6.boxplot((ST5[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax6.boxplot((ST10[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

box_parts = ax6.boxplot((ST15[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax6.boxplot((ST20[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,4), 2, 8, clip_on=False, ec='k', fill=False)
ax6.add_patch(rect)

#ax6.set_ylabel( 'TM2-TM7. ($\AA$)', fontsize=12)
ax6.axhline(y=8.50, linestyle='--', lw=1.5, color='tab:orange', label='6OS0, Active Ref.')
ax6.axhline(y=5.8, linestyle='--', lw=1.5, color='0.5', label='4YAY, Inactive Ref.')
ax6.set_ylim(4,12)
ax6.set_xlim(0,5)
ax6.set_ylabel('L78$^{2.54}$-Y292$^{7.43}$ ($\AA$)', fontsize=12)
ax6.set_title('TM2-TM7 (COM-COM)', fontsize=12)
ax6.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#ax6.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=14)
ax6.yaxis.set_major_locator(MultipleLocator(5))
#ax6.set_yticks([10,15,20])
ax6.yaxis.set_minor_locator(AutoMinorLocator(5))
ax6.xaxis.set_minor_locator(AutoMinorLocator(5))
ax6.xaxis.set_major_locator(MaxNLocator(5))

ax7=plt.subplot(2,3,6)
x_label=['0','5','10','15','20']
x=[0,5,10,15,20]
thickness=[40.5,39.6,37.8, 37.2, 34.8]
thickness_err=[0.77,0.35,0.35,0.63,0.98]
y=[0,5,10, 15, 20]
#popc=[38.2,37.5,36.5]
popc_thickness=38.3
dmpc_thickness=35.8
sopc_thickness=40.5
st10_thickness=37.8
ax7.plot(x,thickness, marker='s',markersize=4,color='tab:blue', label='SOPC')
ax7.plot(0,popc_thickness, marker='>',markersize=4, color='tab:green', label='POPC')
#ax6.plot(y,popc,marker='>',markersize=4, color='tab:green', label='POPC')
#ax7.plot(0, 38.3, yerr=0.5,marker='v', markersize=4, color='tab:green', label='POPC')
ax7.plot(0,dmpc_thickness, marker='D', markersize=4,color='tab:red', label='DMPC')
plt.errorbar(x,thickness,yerr=thickness_err, color='tab:blue')
plt.errorbar(0, dmpc_thickness, yerr=0.5, color='tab:red')
plt.errorbar(0, popc_thickness, yerr=0.6, color='tab:green')
plt.xticks(x,x_label)
plt.ylabel('Bilayer Thickness', fontsize=11)
ax7.text(1.0,35.6, 'DMPC', color='tab:red', fontsize=12, fontweight='medium')
ax7.text(1.0,38.2, 'POPC', color='tab:green', fontsize=12, fontweight='medium')
ax7.text(5.5,40, 'SOPC', color='tab:blue', fontsize=12, fontweight='medium')
#ax6.text(1.0,42.5, 'SOPC:SOPE', color='grey', fontsize=11, fontweight='medium')
ax7.set_ylim(33,44)
ax7.set_ylabel('Bilayer thickness ($\AA$)', fontsize=12)
ax7.xaxis.set_major_locator(MultipleLocator(5))
##ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax7.yaxis.set_major_locator(MultipleLocator(2))
ax7.yaxis.set_minor_locator(AutoMinorLocator(2))
ax7.set_xlabel('Tension (mN/m)', fontsize=12)

leg=ax6.legend(ncol=6,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(0.4,3.1), markerscale=7 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)

ax.text(-0.24, 1.11, 'a', transform=ax.transAxes, ha='center', fontsize=13, fontweight='bold')
ax1.text(-0.24, 1.11, 'b', transform=ax1.transAxes, ha='center', fontsize=13, fontweight='bold')
ax2.text(-0.24, 1.11, 'c', transform=ax2.transAxes, ha='center', fontsize=13, fontweight='bold')
ax3.text(-0.24, 1.11, 'd', transform=ax3.transAxes, ha='center', fontsize=13, fontweight='bold')
ax6.text(-0.24, 1.11, 'e', transform=ax6.transAxes, ha='center', fontsize=13, fontweight='bold')
ax7.text(-0.24, 1.11, 'f', transform=ax7.transAxes, ha='center', fontsize=13, fontweight='bold')
fig = plt.gcf()


plt.subplots_adjust(top=0.85, bottom=0.115, left=0.08, right=0.91, hspace=0.58, wspace=0.82)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_S7.png', dpi=600)
plt.savefig('Figure_S7.svg', dpi=600)
