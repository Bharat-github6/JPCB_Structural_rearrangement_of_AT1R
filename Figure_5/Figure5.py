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

st5= pd.read_csv('/home/poudelb/Desktop/JPCB/various_tension_starting_inactive/descriptor_5', delim_whitespace=True)
st5.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
st5=st5[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_st5=np.linspace(0,10, len(st5))

st10=pd.read_csv('/home/poudelb/Desktop/JPCB/various_tension_starting_inactive/descriptor_10', delim_whitespace=True)
st10.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
st10=st10[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_st10=np.linspace(0,10, len(st10))

st15=pd.read_csv('/home/poudelb/Desktop/JPCB/various_tension_starting_inactive/descriptor_20us', delim_whitespace=True)
st15.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
st15=st15[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_st15=np.linspace(0,5, len(st15))

st20=pd.read_csv('/home/poudelb/Desktop/JPCB/various_tension_starting_inactive/descriptor_20', delim_whitespace=True)
st20.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
st20=st20[['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297']]
time_st20=np.linspace(0,5, len(st20))

window = 8

ax=plt.subplot(2,3,1)
ax.plot(time_st5,(st5[['TM1-TM6']].rolling(window).mean()*10),color='tab:green')
ax.plot(time_st10,(st10[['TM1-TM6']].rolling(window).mean()*10),color='tab:red')
ax.plot(time_st15,(st15[['TM1-TM6']].rolling(window).mean()*10),color='tab:blue')
ax.plot(time_st20,(st20[['TM1-TM6']].rolling(window).mean()*10),color='black')
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.set_ylim(17,37)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('F55$^{1.59}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax.set_title('TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax.set_title('TM1-TM6', fontsize=12)
ax.set_xlim(0,5)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)



ax1=plt.subplot(2,3,2)
ax1.plot(time_st5,(st5[['TM3-TM6']].rolling(window).mean()*10),color='tab:green')
ax1.plot(time_st10,(st10[['TM3-TM6']].rolling(window).mean()*10),color='tab:red')
ax1.plot(time_st15,(st15[['TM3-TM6']].rolling(window).mean()*10),color='tab:blue')
ax1.plot(time_st20,(st20[['TM3-TM6']].rolling(window).mean()*10),color='black')
ax1.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
#ax1.set_ylim(6,21)
ax1.set_xlim(0,5)
ax1.set_ylabel('R126$^{3.50}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax1.set_title('TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
#ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=14)
ax1.yaxis.set_major_locator(MultipleLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax1.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)

ax2=plt.subplot(2,3,3)

ax2.plot(time_st5,(st5[['NpxxY']].rolling(window).mean()*10),color='tab:green')
ax2.plot(time_st10,(st10[['NpxxY']].rolling(window).mean()*10),color='tab:red')
ax2.plot(time_st15,(st15[['NpxxY']].rolling(window).mean()*10),color='tab:blue')
ax2.plot(time_st20,(st20[['NpxxY']].rolling(window).mean()*10),color='black')
ax2.set_xlim(0,5)
ax2.axhline(y=5, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=12, linestyle='--', lw=1.5, color='0.5')
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax2.set_ylabel('Y215$^{5.58}$-Y302$^{7.53}$ ($\AA$)', fontsize=12)
ax2.set_title('TM5-TM7 (OH-OH)', fontsize=12)
ax2.yaxis.set_major_locator(MultipleLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)


ax3=plt.subplot(2,3,4)

ax3.plot(time_st5,(st5[['N300_S115']].rolling(window).mean()*10),color='tab:green')
ax3.plot(time_st10,(st10[['N300_S115']].rolling(window).mean()*10),color='tab:red')
ax3.plot(time_st15,(st15[['N300_S115']].rolling(window).mean()*10),color='tab:blue')
ax3.plot(time_st20,(st20[['N300_S115']].rolling(window).mean()*10),color='black')
#ax3.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)
ax3.set_ylabel('S115$^{3.39}$-N295$^{7.46}$ ($\AA$)', fontsize=12)
ax3.set_title('TM3-TM7 (COM-COM)', fontsize=12)
ax3.axhline(y=9.4, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=6.1, linestyle='--', lw=1.5, color='tab:orange')
#ax3.set_ylim(4,15)
ax3.set_xlim(0,5)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax3.yaxis.set_major_locator(MultipleLocator(2))
ax3.yaxis.set_minor_locator(AutoMinorLocator(2))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax3.xaxis.set_major_locator(MultipleLocator(5))

ax6=plt.subplot(2,3,5)
ax6.plot(time_st5,(st5[['L78_Y297']].rolling(window).mean()*10),color='tab:green',label='$\gamma=$ 5 mN/m')
ax6.plot(time_st10,(st10[['L78_Y297']].rolling(window).mean()*10),color='tab:red', label='$\gamma=$ 10 mN/m')
ax6.plot(time_st15,(st15[['L78_Y297']].rolling(window).mean()*10),color='tab:blue', label='$\gamma=$ 15 mN/m')
ax6.plot(time_st20,(st20[['L78_Y297']].rolling(window).mean()*10),color='black', label='$\gamma= 20 $  mN/m')
ax6.set_ylabel('L78$^{2.54}$-Y292$^{7.43}$ ($\AA$)', fontsize=12)
ax6.set_title('TM2-TM7 (COM-COM)', fontsize=12)
ax6.axhline(y=6.6, linestyle='--', lw=1.5, color='0.5', label='4YAY')
ax6.axhline(y=9.1, linestyle='--', lw=1.5, color='tab:orange', label='6OS0')
#ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
#ax3.axhline(y=22.56, linestyle='--', lw=1.5, color='tab:orange')
#ax6.set_ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax6.set_ylim(4,12)
ax6.set_xlim(0,5)
ax6.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax6.yaxis.set_major_locator(MultipleLocator(2))
ax6.yaxis.set_minor_locator(AutoMinorLocator(2))
ax6.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax6.xaxis.set_major_locator(MultipleLocator(5))
#ax6.axvline(x=10, linestyle='dashed', color='black', alpha=0.3)
#ax6.legend()

#leg=ax6.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(0.5,1.5), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

#for i in leg.legendHandles:
#    i.set_linewidth(2)


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


leg=ax6.legend(ncol=6,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(0.5,2.97), markerscale=11 ,columnspacing=1, handletextpad=0.5, handlelength=1.6, fontsize=12)
for i in leg.legendHandles:
    i.set_linewidth(2)


ax.text(-0.24, 1.05, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.24, 1.05, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.24, 1.05, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.24, 1.05, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax6.text(-0.24, 1.05, 'e', transform=ax6.transAxes, ha='center', fontsize=14, fontweight='bold')
#ax7.text(-0.24, 1.05, 'f', transform=ax7.transAxes, ha='center', fontsize=14, fontweight='bold')
fig = plt.gcf()

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.08, right=0.94, hspace=0.58, wspace=0.45)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_5_newdata.png', dpi=600)
plt.savefig('Figure_5_newdate.svg', dpi=600)
