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

i1=pd.read_csv('rep1/rep1', delim_whitespace=True)
i1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
time_i1=np.linspace(0,5, len(i1))

i2=pd.read_csv('rep1/rep2', delim_whitespace=True)
i2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297', 'none', 'none']
time_i2=np.linspace(0,5, len(i2))

sopc_i=pd.concat([i1,i2], axis=1)


a1=pd.read_csv('rep2/rep1', delim_whitespace=True)
a1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
time_a1=np.linspace(0,5, len(a1))

a2=pd.read_csv('rep2/rep2', delim_whitespace=True)
a2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297', 'none', 'none']

a2=a2[0:len(a1)]
time_a2=np.linspace(0,5, len(a2))

sopc_a=pd.concat([a1,a2], axis=1)



plt.figure(figsize=(11,5))
ax1=plt.subplot(2,3,1)
window=5

width=0.5
start=5.5
sp = 0.65

box_parts = ax1.boxplot((sopc_a[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax1.boxplot((sopc_i[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((5.2,12),1.3 , 27, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)


ax1.plot(time_a1, a1[['TM1-TM6']].rolling(window).mean()*10, color='tab:blue', label='Active')
ax1.plot(time_i1, i1[['TM1-TM6']].rolling(window).mean()*10,color='tab:green', label='Intermediate')
#ax1.plot(time_in2, in2[['TM1-TM6']].rolling(window).mean()*10, color='tab:red',label='Inactive')
ax1.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax1.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax1.set_ylabel('F55$^{1.59}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax1.set_title('TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax1.set_title( 'TM1-TM6', fontsize=12)
ax1.yaxis.set_major_locator(MaxNLocator(6))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_major_locator(MaxNLocator(5))
ax1.set_ylim(12, 39)
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax1.set_xlim(0,5)


ax2=plt.subplot(2,3,2)

box_parts = ax2.boxplot((sopc_a[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax2.boxplot((sopc_i[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

rect = Rectangle((5.2,4),1.3 , 19, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)
    
ax2.plot(time_a1, a1[['TM3-TM6']].rolling(window).mean()*10,color='tab:blue', label='Active')
ax2.plot(time_i1, i1[['TM3-TM6']].rolling(window).mean()*10,color='tab:green', label='Intermediate')
#ax2.plot(time_in2, in2[['TM3-TM6']].rolling(window).mean()*10,color='tab:red', label='Inactive')
ax2.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
ax2.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
ax2.set_ylabel('R126$^{3.50}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax2.set_title('TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax2.set_title( 'TM3-TM6', fontsize=12)
plt.ylim(4,23)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax2.yaxis.set_major_locator(MaxNLocator(4))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_major_locator(MaxNLocator(5))
ax2.set_xlim(0,5)


ax3=plt.subplot(2,3,3)

box_parts = ax3.boxplot((sopc_a[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax3.boxplot((sopc_i[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((5.2,0),1.3 , 32, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)
ax3.plot(time_a1, a1[['NpxxY']].rolling(window).mean()*10,color='tab:blue', label='Active')
ax3.plot(time_i1, i1[['NpxxY']].rolling(window).mean()*10, color='tab:green',label='Intermediate')
#ax3.plot(time_in2, in2[['NpxxY']].rolling(window).mean()*10,color='tab:red', label='Inactive')
ax3.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
ax3.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
ax3.set_ylabel('Y215$^{5.58}$-Y302$^{7.53}$ ($\AA$)', fontsize=12)
ax3.set_title( ' TM5-TM7 (OH-OH)', fontsize=12)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax3.yaxis.set_major_locator(MaxNLocator(5))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_major_locator(MaxNLocator(5))
ax3.set_xlim(0,5)
ax3.set_ylim(0,32)

ax4=plt.subplot(2,3,4)

box_parts = ax4.boxplot((sopc_a[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax4.boxplot((sopc_i[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((5.2,4),1.3 , 8, clip_on=False, ec='k', fill=False)
ax4.add_patch(rect)

for line in plt.gca().get_lines(): line.set_clip_on(False)

ax4.plot(time_a1, a1[['N300_S115']].rolling(window).mean()*10,color='tab:blue', label='Active')
ax4.plot(time_i1, i1[['N300_S115']].rolling(window).mean()*10,color='tab:green', label='Intermediate')
#ax4.plot(time_in2, in2[['N300_S115']].rolling(window).mean()*10,color='tab:red', label='Inactive')
ax4.axhline(y=6.1, linestyle='dashed', color='tab:orange', lw=1.5)
ax4.axhline(y=9.4, linestyle='dashed', color='0.5',lw=1.5)
ax4.set_title( 'TM3-TM7 (COM-COM)', fontsize=12)
ax4.set_ylabel('S115$^{3.39}$-N295$^{7.46}$ ($\AA$)', fontsize=12)
ax4.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax4.xaxis.set_major_locator(MaxNLocator(5))
ax4.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_major_locator(MaxNLocator(5))
#ax4.set_ylim(0,20)
#ax4.set_xticks(fontsize=15)
#ax4.set_yticks([6,8,10,12], fontsize=15)
ax4.set_xlim(0,5)
ax4.set_ylim(4,12)


ax5=plt.subplot(2,3,5)

box_parts = ax5.boxplot((sopc_a[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax5.boxplot((sopc_i[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((5.2,4),1.3, 8, clip_on=False, ec='k', fill=False)
ax5.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)

ax5.plot(time_a1, a1[['L78_Y297']].rolling(window).mean()*10,color='tab:blue', label='d(TM1-TM6)=25 $\AA$ @$t=0$')
ax5.plot(time_i1, i1[['L78_Y297']].rolling(window).mean()*10, color='tab:green',label='d(TM1-TM6)=28 $\AA$ @$t=0$')
#ax5.plot(time_in2, in2[['L78_Y297']].rolling(window).mean()*10,color='tab:red', label='d(TM1-TM6)=21 $\AA$ @$t=0$')
ax5.axhline(y=9.1, linestyle='dashed', color='tab:orange', lw=1.5, label="6OS0, Active Ref.")
ax5.axhline(y=6.6, linestyle='dashed', color='0.5',lw=1.5, label="4YAY, Inactive Ref.")
ax5.set_title( 'TM2-TM7 (COM-COM)', fontsize=12)
ax5.set_ylabel('L78$^{2.54}$-Y292$^{7.43}$ ($\AA$)', fontsize=12)
ax5.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax5.yaxis.set_major_locator(MaxNLocator(5))
ax5.yaxis.set_minor_locator(AutoMinorLocator(2))
ax5.xaxis.set_minor_locator(AutoMinorLocator(5))
ax5.xaxis.set_major_locator(MaxNLocator(5))
ax5.set_ylim(4,12)
ax5.set_xlim(0,5)
#plt.xlabel('Time (u"\u03bcs)', fontsize=12)
leg=ax5.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.35,1), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)

ax1.text(-0.2, 1.10, 'a', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.2, 1.10, 'b', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.2, 1.10, 'c', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax4.text(-0.2, 1.10, 'd', transform=ax4.transAxes, ha='center', fontsize=14, fontweight='bold')
ax5.text(-0.2, 1.10, 'e', transform=ax5.transAxes, ha='center', fontsize=14, fontweight='bold')

fig = plt.gcf()

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.1, right=0.90, hspace=0.58, wspace=0.85)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_6_sup.png', dpi=600)
plt.savefig('Figure_6_sup.svg', dpi=600)
