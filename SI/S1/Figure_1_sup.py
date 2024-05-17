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


popc_r1= pd.read_csv('POPC/descriptor_rep1', delim_whitespace=True)
popc_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
popc_r1=popc_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_popcr1=np.linspace(0,5, len(popc_r1))

popc_r2= pd.read_csv('POPC/descriptor_rep2', delim_whitespace=True)
popc_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
popc_r2=popc_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_popcr2=np.linspace(0,5, len(popc_r2))

popc=pd.concat([popc_r1,popc_r2], axis=1)


dmpc_r1= pd.read_csv('DMPC/descriptor_rep1', delim_whitespace=True)
dmpc_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
dmpc_r1=dmpc_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_dmpcr1=np.linspace(0,5, len(dmpc_r1))

dmpc_r2= pd.read_csv('DMPC/descriptor_rep2', delim_whitespace=True)
dmpc_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
dmpc_r2=dmpc_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_dmpcr2=np.linspace(0,5, len(dmpc_r2))

dmpc=pd.concat([dmpc_r1, dmpc_r2], axis=1)


sopc_r1= pd.read_csv('SOPC/descriptor_rep1', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
sopc_r1=sopc_r1[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
sopc_r1=sopc_r1[0:2084]
time_sopcr1=np.linspace(0,5, len(sopc_r1))

sopc_r2= pd.read_csv('SOPC/descriptor_rep2', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
sopc_r2=sopc_r2[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
sopc_r2=sopc_r2[0:2084]
time_sopcr2=np.linspace(0,5, len(sopc_r2))

sopc=pd.concat([sopc_r1, sopc_r2], axis=1)


window = 5

ax=plt.subplot(2,3,1)
ax.plot(time_popcr2,(popc_r2[['TM1-TM6']].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax.plot(time_dmpcr2,(dmpc_r2[['TM1-TM6']].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax.plot(time_sopcr2,(sopc_r2[['TM1-TM6']].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')

width=0.3
start=5.5
sp = 0.4

box_parts = ax.boxplot((sopc[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax.boxplot((popc[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax.boxplot((dmpc[['TM1-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax.set_ylim(17,37)
ax.set_xlim(0,5)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(4))
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
rect = Rectangle((5.2,17),1.5, 20, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)

ax1=plt.subplot(2,3,2)
box_parts = ax1.boxplot((sopc[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax1.boxplot((popc[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax1.boxplot((dmpc[['TM3-TM6']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,6), 1.5, 16, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)

ax1.plot(time_popcr2,(popc_r2[['TM3-TM6']].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax1.plot(time_dmpcr2,(dmpc_r2[['TM3-TM6']].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax1.plot(time_sopcr2,(sopc_r2[['TM3-TM6']].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
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
box_parts = ax2.boxplot((sopc[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax2.boxplot((popc[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax2.boxplot((dmpc[['NpxxY']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((5.2,2), 1.5, 18, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)

ax2.plot(time_popcr2,(popc_r2[['NpxxY']].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax2.plot(time_dmpcr2,(dmpc_r2[['NpxxY']].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax2.plot(time_sopcr2,(sopc_r2[['NpxxY']].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
ax2.set_xlim(0,5)
ax2.axhline(y=5, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=12, linestyle='--', lw=1.5, color='0.5')
ax2.set_ylim(2,20)
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
box_parts = ax3.boxplot((sopc[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax3.boxplot((popc[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax3.boxplot((dmpc[['N300_S115']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((5.2,4), 1.5, 9, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)

ax3.plot(time_popcr2,(popc_r2[['N300_S115']].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax3.plot(time_dmpcr2,(dmpc_r2[['N300_S115']].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax3.plot(time_sopcr2,(sopc_r2[['N300_S115']].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
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
box_parts = ax6.boxplot((sopc[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax6.boxplot((popc[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

box_parts = ax6.boxplot((dmpc[['L78_Y297']][1667:2084].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,4), 1.5, 8, clip_on=False, ec='k', fill=False)
ax6.add_patch(rect)

ax6.plot(time_dmpcr2,(dmpc_r2[['L78_Y297']].rolling(window).mean()*10),color='tab:red', label='DMPC (di-C14:0)')
ax6.plot(time_popcr2,(popc_r2[['L78_Y297']].rolling(window).mean()*10),color='tab:green',label='POPC (C16:0,C18:1)')
ax6.plot(time_sopcr2,(sopc_r2[['L78_Y297']].rolling(window).mean()*10), color='tab:blue', label='SOPC (C18:0,C18:1)')
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
x_label=['DMPC', 'POPC', 'SOPC']
x=[1, 2, 3]
thickness=[35.8, 38.3,40.5]
thickness_err=[0.77,0.35,0.35]
#y=[0,5,10, 15, 20]
positions=np.arange(len(x_label))
plt.bar(positions[0], thickness[0], width=0.4, color='tab:red',edgecolor='black')
plt.bar(positions[1], thickness[1], width=0.4, color='tab:green',edgecolor='black')
plt.bar(positions[2], thickness[2], width=0.4, color='tab:blue',edgecolor='black')
plt.errorbar(positions, thickness, yerr=thickness_err, fmt='none', color='black', capsize=5)
plt.xticks(positions, x_label)
plt.ylabel('Bilayer Thickness', fontsize=12)
ax7.set_ylim(33, 44)
ax7.set_ylabel('Bilayer thickness ($\AA$)', fontsize=12)
ax7.xaxis.set_major_locator(MultipleLocator(1))
ax7.yaxis.set_major_locator(MultipleLocator(2))
ax7.yaxis.set_minor_locator(AutoMinorLocator(2))

leg=ax6.legend(ncol=5,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(0.4,3), markerscale=7 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)

ax.text(-0.24, 1.08, 'a', transform=ax.transAxes, ha='center', fontsize=13, fontweight='bold')
ax1.text(-0.24, 1.08, 'b', transform=ax1.transAxes, ha='center', fontsize=13, fontweight='bold')
ax2.text(-0.24, 1.08, 'c', transform=ax2.transAxes, ha='center', fontsize=13, fontweight='bold')
ax3.text(-0.24, 1.08, 'd', transform=ax3.transAxes, ha='center', fontsize=13, fontweight='bold')
ax6.text(-0.24, 1.08, 'e', transform=ax6.transAxes, ha='center', fontsize=13, fontweight='bold')
ax7.text(-0.24, 1.08, 'f', transform=ax7.transAxes, ha='center', fontsize=13, fontweight='bold')
fig = plt.gcf()


plt.subplots_adjust(top=0.88, bottom=0.115, left=0.08, right=0.91, hspace=0.58, wspace=0.73)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_1_sup.png', dpi=600)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
