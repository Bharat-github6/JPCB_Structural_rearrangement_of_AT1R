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
#/home/bpoudel/projects/gpcr/6do1-active-state/ANTON2/6DO1/SOPC/FNmut
sopc_r1i=pd.read_csv('descriptor_rep1', delim_whitespace=True)
sopc_r1i.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
time1=np.linspace(0,10, len(sopc_r1i))


sopc_r2i=pd.read_csv('descriptor_rep2', delim_whitespace=True)
sopc_r2i.columns=['time', 'TM1-TM6', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
time2=np.linspace(0,10, len(sopc_r2i))


width=0.5
start=10.5
sp = 0.65


#plt.figure(figsize=(10,10))
ax=plt.subplot(2,3,1)
window=15

box_parts = ax.boxplot((sopc_r1i[['TM1-TM6']][3334:4168].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax.boxplot((sopc_r2i[['TM1-TM6']][6668:8336].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((10.2,10),1.3 , 25, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)


ax.plot(time1, sopc_r1i[['TM1-TM6']].rolling(window).mean()*10,color='tab:blue', label='Rep1')
ax.plot(time2, sopc_r2i[['TM1-TM6']].rolling(window).mean()*10, color= 'tab:green',  label='Rep2')
#plt.plot(time2, sopc_r2i[['TM1-TM6']].rolling(window).mean()*10, label='Rep2')
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.set_ylabel( 'TM1-TM6 Dist. ($\AA$)', fontsize=11)
ax.set_ylabel('F55$^{1.59}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax.set_title('TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
ax.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#plt.xticks(fontsize=15)
#plt.yticks(fontsize=15)
ax.axvline(x=1, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=2, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=3, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=4, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=5, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=6, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=7, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=8, linestyle='dashed', color='black', alpha=0.2)
ax.axvline(x=9, linestyle='dashed', color='black', alpha=0.2)
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax.set_title('TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#plt.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)
#plt.text('F77A/N111G',bbox_to_anchor=(2,25), fontsize=12)
ax.set_xlim(0,10)
ax.set_ylim(10,35)

ax1=plt.subplot(2,3,2)


box_parts = ax1.boxplot((sopc_r1i[['TM3-TM6']][3334:4168].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax1.boxplot((sopc_r2i[['TM3-TM6']][6668:8336].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

rect = Rectangle((10.2,5),1.3 , 15, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)

ax1.plot(time1, sopc_r1i[['TM3-TM6']].rolling(window).mean()*10,color='tab:blue', label='Rep1')
ax1.plot(time2, sopc_r2i[['TM3-TM6']].rolling(window).mean()*10,color='tab:green', label='Rep2')
ax1.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
ax1.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
ax1.set_ylabel('R126$^{3.50}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax1.set_title('TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#ax1.set_ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=11)
#plt.xlabel('Time ($\mu$s)', fontsize=15)
#plt.xticks(fontsize=15)
#plt.yticks(fontsize=15)
ax1.axvline(x=1, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=2, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=3, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=4, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=5, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=6, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=7, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=8, linestyle='dashed', color='black', alpha=0.2)
ax1.axvline(x=9, linestyle='dashed', color='black', alpha=0.2)
ax1.set_xlim(0,10)
ax1.set_ylim(5,20)
ax1.yaxis.set_major_locator(MaxNLocator(4))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_title('TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#plt.xlabel('Time (u"\u03bcs)', fontsize=12)

ax2=plt.subplot(2,3,3)

box_parts = ax2.boxplot((sopc_r1i[['NpxxY']][3334:4168].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax2.boxplot((sopc_r2i[['NpxxY']][6668:8336].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((10.2,0),1.3 , 30, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)
ax2.plot(time1, sopc_r1i[['NpxxY']].rolling(window).mean()*10, color='tab:blue', label='Rep1')
ax2.plot(time2, sopc_r2i[['NpxxY']].rolling(window).mean()*10,color='tab:green',  label='Rep2')
ax2.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
ax2.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
#ax2.set_ylabel( 'NPxxY Dist. ($\AA$)', fontsize=11)
ax2.set_ylabel('Y215$^{5.58}$-Y302$^{7.53}$ ($\AA$)', fontsize=12)
ax2.set_title('TM5-TM7 (OH-OH)', fontsize=12)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#plt.xlabel('Time ($\mu$s)', fontsize=15)
#plt.xticks(fontsize=15)
ax2.axvline(x=1, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=2, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=3, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=4, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=5, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=6, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=7, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=8, linestyle='dashed', color='black', alpha=0.2)
ax2.axvline(x=9, linestyle='dashed', color='black', alpha=0.2)
ax2.yaxis.set_major_locator(MaxNLocator(7))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#plt.yticks([2,4,6,8,10,12], fontsize=15)
ax2.set_xlim(0,10)
ax2.set_ylim(0,30)
ax2.set_title('TM5-TM7 (OH-OH)', fontsize=12)

ax3=plt.subplot(2,3,4)

box_parts = ax3.boxplot((sopc_r1i[['N300_S115']][3334:4168].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax3.boxplot((sopc_r2i[['N300_S115']][6668:8336].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((10.2,5),1.3 , 10, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)

for line in plt.gca().get_lines(): line.set_clip_on(False)

ax3.plot(time1, sopc_r1i[['N300_S115']].rolling(window).mean()*10,color='tab:blue', label='Rep1')
ax3.plot(time2, sopc_r2i[['N300_S115']].rolling(window).mean()*10, color='tab:green', label='Rep2')
#plt.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
#plt.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
ax3.axhline(y=6.1, linestyle='dashed', color='tab:orange', lw=1.5)
ax3.axhline(y=9.4, linestyle='dashed', color='0.5',lw=1.5)
#ax3.set_ylabel( 'TM3-TM7 Dist. ($\AA$)', fontsize=11)
ax3.set_ylabel('S115$^{3.39}$-N295$^{7.46}$ ($\AA$)', fontsize=12)
ax3.set_title('TM3-TM7 (COM-COM)', fontsize=12)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#ax3.set_xlabel('Time ($\mu$s)', fontsize=15)
#ax3.xticks(fontsize=15)
ax3.set_ylim(5,15)
#plt.yticks([2,4,6,8,10,12], fontsize=15)
ax3.axvline(x=1, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=2, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=3, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=4, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=5, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=6, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=7, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=8, linestyle='dashed', color='black', alpha=0.2)
ax3.axvline(x=9, linestyle='dashed', color='black', alpha=0.2)
ax3.yaxis.set_major_locator(MaxNLocator(3))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.set_xlim(0,10)
ax3.set_yticks([5,10,15])
#ax3.set_title('TM3-TM7 (COM-COM)', fontsize=12)

ax4=plt.subplot(2,3,5)

box_parts = ax4.boxplot((sopc_r1i[['L78_Y297']][3334:4168].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax4.boxplot((sopc_r2i[['L78_Y297']][6668:8336].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


rect = Rectangle((10.2,5),1.3, 5, clip_on=False, ec='k', fill=False)
ax4.add_patch(rect)
for line in plt.gca().get_lines(): line.set_clip_on(False)


ax4.plot(time1, sopc_r1i[['L78_Y297']].rolling(window).mean()*10,color='tab:blue', label='Rep1')
ax4.plot(time2, sopc_r2i[['L78_Y297']].rolling(window).mean()*10, color='tab:green', label='Rep2')
#plt.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
#plt.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
#ax4.axhline(y=9.1, linestyle='dashed', color='tab:orange', lw=1.5)
#ax4.axhline(y=6.8, linestyle='dashed', color='0.5',lw=1.5)
#ax4.set_ylabel( 'TM2-TM7 Dist. ($\AA$)', fontsize=11)
ax4.set_ylabel('L78$^{2.54}$-Y292$^{7.43}$ ($\AA$)', fontsize=12)
ax4.set_title('TM2-TM7 (COM-COM)', fontsize=12)
ax4.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#ax4.set_xlabel('Time ($\mu$s)', fontsize=15)
#plt.xticks(fontsize=15)
ax4.set_ylim(5,10)
ax4.set_yticks([5,10])
#plt.yticks([2,4,6,8,10,12], fontsize=15)
ax4.axvline(x=1, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=2, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=3, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=4, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=5, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=6, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=7, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=8, linestyle='dashed', color='black', alpha=0.2)
ax4.axvline(x=9, linestyle='dashed', color='black', alpha=0.2)
ax4.yaxis.set_major_locator(MaxNLocator(1))
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))
ax4.axhline(y=8.50, linestyle='--', lw=1.5, color='tab:orange', label='6OS0, Active Ref.')
ax4.axhline(y=5.8, linestyle='--', lw=1.5, color='0.5', label='4YAY, Inactive Ref.')



#plt.legend()
ax4.set_xlim(0,10)
#ax4.set_title('TM2-TM7 (COM-COM)', fontsize=12)
ax.text(-0.24, 1.15, 'a', transform=ax.transAxes, ha='center', fontsize=13, fontweight='bold')
ax1.text(-0.24, 1.15, 'b', transform=ax1.transAxes, ha='center', fontsize=13, fontweight='bold')
ax2.text(-0.24, 1.15, 'c', transform=ax2.transAxes, ha='center', fontsize=13, fontweight='bold')
ax3.text(-0.24, 1.15, 'd', transform=ax3.transAxes, ha='center', fontsize=13, fontweight='bold')
ax4.text(-0.24, 1.15, 'e', transform=ax4.transAxes, ha='center', fontsize=13, fontweight='bold')


leg=ax4.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.2, 1.1), markerscale=7 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)


fig=plt.gcf()

plt.subplots_adjust(top=0.88, bottom=0.115, left=0.08, right=0.91, hspace=0.65, wspace=0.73)
plt.Figure.set_size_inches(fig,(11, 5))
#plt.subplots_adjust(top=0.90, bottom=0.115, left=0.1, right=0.92, hspace=0.4, wspace=0.4)
plt.savefig('Figure_S4.png', dpi=600)
