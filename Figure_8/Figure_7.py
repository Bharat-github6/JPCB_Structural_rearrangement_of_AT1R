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


#/home/bpoudel/projects/gpcr/6do1-active-state/ANTON2/6DO1/SOPC/FNmut
sopc_r1i=pd.read_csv('descriptor_inactive', delim_whitespace=True)
sopc_r1i.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297','none', 'none']
time1=np.linspace(0,20, len(sopc_r1i))

sopc_r2i=pd.read_csv('descriptor_active', delim_whitespace=True)
sopc_r2i.columns=['time', 'TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6', 'NpxxY','N300_S115', 'L78_Y297', 'none', 'none']
time2=np.linspace(0,20, len(sopc_r2i))


#plt.figure(figsize=(10,10))
ax1=plt.subplot(2,3,1)
window=20
ax1.plot(time1, sopc_r1i[['TM1-TM6']].rolling(window).mean()*10, color='tab:green', label='Rep1')
ax1.plot(time2, sopc_r2i[['TM1-TM6']].rolling(window).mean()*10, color='tab:blue', label='Rep2')
ax1.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax1.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax1.set_ylabel('F55$^{1.59}$-D236$^{6.31}$ ($\AA$)', fontsize=12)
ax1.set_title( 'TM1-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
ax1.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.set_xlim(0,20)
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)


ax2=plt.subplot(2,3,2)
ax2.plot(time1, sopc_r1i[['TM3-TM6']].rolling(window).mean()*10, color='tab:green', label='Rep1')
ax2.plot(time2, sopc_r2i[['TM3-TM6']].rolling(window).mean()*10, color='tab:blue', label='Rep2')
ax2.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
ax2.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
ax2.set_ylabel('R126$^{3.50}$-D236$^{6.31}$ ($\AA$)', fontsize=12)

ax2.set_title( 'TM3-TM6 (C$_\\alpha$-C$_\\alpha$)', fontsize=12)
ax2.yaxis.set_major_locator(MultipleLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.set_xlim(0,20)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
#plt.xlabel('Time (u"\u03bcs)', fontsize=12)

ax3=plt.subplot(2,3,3)
ax3.plot(time1, sopc_r1i[['NpxxY']].rolling(window).mean()*10, color='tab:green', label='Rep1')
ax3.plot(time2, sopc_r2i[['NpxxY']].rolling(window).mean()*10, color='tab:blue',label='Rep2')
ax3.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
ax3.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
ax3.set_ylabel('Y215$^{5.58}$-Y302$^{7.53}$ ($\AA$)', fontsize=12)
ax3.set_title( 'TM5-TM7 (OH-OH)', fontsize=12)
ax3.yaxis.set_major_locator(MultipleLocator(5))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax3.set_xlim(0,20)

ax4=plt.subplot(2,3,4)
ax4.plot(time1, sopc_r1i[['N300_S115']].rolling(window).mean()*10, color='tab:green', label='Rep1')
ax4.plot(time2, sopc_r2i[['N300_S115']].rolling(window).mean()*10, color='tab:blue', label='Rep2')
#plt.axhline(y=5, linestyle='dashed', color='tab:orange', lw=1.5)
#plt.axhline(y=12, linestyle='dashed', color='0.5',lw=1.5)
ax4.axhline(y=6.1, linestyle='dashed', color='tab:orange', lw=1.5)
ax4.axhline(y=9.4, linestyle='dashed', color='0.5',lw=1.5)
ax4.set_ylabel('S115$^{3.39}$-N295$^{7.46}$ ($\AA$)', fontsize=12)
ax4.set_title( 'TM3-TM7 (COM-COM)', fontsize=12)
ax4.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax4.yaxis.set_major_locator(MultipleLocator(4))
ax4.yaxis.set_minor_locator(AutoMinorLocator(4))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))
ax4.set_xlim(0,20)
ax4.set_ylim(4,12)

ax5=plt.subplot(2,3,5)
ax5.plot(time1, sopc_r1i[['L78_Y297']].rolling(window).mean()*10,color='tab:green', label='Inactive @$t=0$')
ax5.plot(time2, sopc_r2i[['L78_Y297']].rolling(window).mean()*10,color='tab:blue', label='Active @$t=0$')
ax5.axhline(y=9.1, linestyle='dashed', color='tab:orange', lw=1.5, label='6OS0 Active Ref.')
ax5.axhline(y=6.6, linestyle='dashed', color='0.5',lw=1.5, label='4YAY Inctive Ref.')
ax5.set_ylabel('L78$^{2.54}$-Y292$^{7.43}$ ($\AA$)', fontsize=12)
ax5.set_title( 'TM2-TM7 (COM-COM)', fontsize=12)
ax5.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax5.yaxis.set_major_locator(MultipleLocator(2))
ax5.yaxis.set_minor_locator(AutoMinorLocator(2))
ax5.xaxis.set_minor_locator(AutoMinorLocator(5))
ax5.set_xlim(0,20)
ax5.set_ylim(4,12)

leg=ax5.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.7,1), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)

ax1.text(-0.24, 1.08, 'a', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.24, 1.08, 'b', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.24, 1.08, 'c', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax4.text(-0.24, 1.08, 'd', transform=ax4.transAxes, ha='center', fontsize=14, fontweight='bold')
ax5.text(-0.24, 1.08, 'e', transform=ax5.transAxes, ha='center', fontsize=14, fontweight='bold')
fig = plt.gcf()


plt.subplots_adjust(top=0.90, bottom=0.115, left=0.08, right=0.91, hspace=0.58, wspace=0.35)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_7.png', dpi=600)    
