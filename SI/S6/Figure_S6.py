import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from IPython.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>"))
from matplotlib.patches import Rectangle

DMPC_C29_act1=pd.read_csv('data/DMPC_Active_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
DMPC_C29_act1.columns=['time', 'num']

DMPC_C39_act1=pd.read_csv('data/DMPC_Active_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
DMPC_C39_act1.columns=['time', 'num']



DMPC_C29_act2=pd.read_csv('data/DMPC_active_C29_rep2.xvg', delim_whitespace='True', skiprows=24)
DMPC_C29_act2.columns=['time', 'num']


DMPC_C39_act2=pd.read_csv('data/DMPC_active_C39_rep2.xvg', delim_whitespace='True', skiprows=24)
DMPC_C39_act2.columns=['time', 'num']


DMPC_act_C29=pd.concat([DMPC_C29_act1, DMPC_C29_act2], axis=1)
DMPC_act_C39=pd.concat([DMPC_C39_act1, DMPC_C39_act2], axis=1)



DMPC_C29_inact1=pd.read_csv('data/DMPC_Inactive_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
DMPC_C29_inact1.columns=['time', 'num']
#time=np.linspace(0,5,len(POPC_C29_act1))

DMPC_C39_inact1=pd.read_csv('data/DMPC_Inactive_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
DMPC_C39_inact1.columns=['time', 'num']



DMPC_C29_inact2=pd.read_csv('data/DMPC_Inactive_C29_rep2.xvg', delim_whitespace='True')
DMPC_C29_inact2.columns=['time', 'num']
#time=np.linspace(0,5,len(POPC_C29_act1))

DMPC_C39_inact2=pd.read_csv('data/DMPC_Inactive_C39_rep2.xvg', delim_whitespace='True')
DMPC_C39_inact2.columns=['time', 'num']

DMPC_inact_C29=pd.concat([DMPC_C29_inact1, DMPC_C29_inact2], axis=1)
DMPC_inact_C39=pd.concat([DMPC_C39_inact1, DMPC_C39_inact2], axis=1)


POPC_C29_act1=pd.read_csv('data/POPC_Active_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
POPC_C29_act1.columns=['time', 'num']
#time=np.linspace(0,5,len(POPC_C29_act1))

POPC_C39_act1=pd.read_csv('data/POPC_Active_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
POPC_C39_act1.columns=['time', 'num']


POPC_C29_act2=pd.read_csv('data/POPC_active_C29_rep2.xvg', delim_whitespace='True', skiprows=24)
POPC_C29_act2.columns=['time', 'num']
#time=np.linspace(0,5,len(POPC_C29_act1))

POPC_C39_act2=pd.read_csv('data/POPC_active_C39_rep2.xvg', delim_whitespace='True', skiprows=24)
POPC_C39_act2.columns=['time', 'num']

POPC_act_C29=pd.concat([POPC_C29_act1, POPC_C29_act2], axis=1)
POPC_act_C39=pd.concat([POPC_C39_act1, POPC_C39_act2], axis=1)


#######

POPC_C29_inact1=pd.read_csv('data/POPC_Inactive_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
POPC_C29_inact1.columns=['time', 'num']

POPC_C39_inact1=pd.read_csv('data/POPC_Inactive_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
POPC_C39_inact1.columns=['time', 'num']

POPC_C29_inact2=pd.read_csv('data/POPC_Inactive_C29_rep2.xvg', delim_whitespace='True', skiprows=24)
POPC_C29_inact2.columns=['time', 'num']

POPC_C39_inact2=pd.read_csv('data/POPC_Inactive_C39_rep2.xvg', delim_whitespace='True', skiprows=24)
POPC_C39_inact2.columns=['time', 'num']


POPC_inact_C29=pd.concat([POPC_C29_inact1, POPC_C29_inact2], axis=1)
POPC_inact_C39=pd.concat([POPC_C39_inact1, POPC_C39_inact2], axis=1)

SOPC_C39_act1=pd.read_csv('data/SOPC_Protein_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
SOPC_C39_act1.columns=['time', 'num']
SOPC_C39_act1=SOPC_C39_act1[0:4167]


SOPC_C29_act1=pd.read_csv('data/SOPC_Protein_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
SOPC_C29_act1.columns=['time', 'num']
SOPC_C29_act1=SOPC_C29_act1[0:4167]


SOPC_C39_act2=pd.read_csv('data/SOPC_active_C39_rep2.xvg', delim_whitespace='True', skiprows=24)
SOPC_C39_act2.columns=['time', 'num']
SOPC_C39_act2=SOPC_C39_act2[0:4167]


SOPC_C29_act2=pd.read_csv('data/SOPC_active_C29_rep2.xvg', delim_whitespace='True', skiprows=24)
SOPC_C29_act2.columns=['time', 'num']
SOPC_C29_act2=SOPC_C29_act2[0:4167]


SOPC_act_C29=pd.concat([SOPC_C29_act1, SOPC_C29_act2], axis=1)
SOPC_act_C39=pd.concat([SOPC_C39_act1, SOPC_C39_act2], axis=1)



SOPC_C29_inact1=pd.read_csv('data/SOPC_Protein_C29_rep1.xvg', delim_whitespace='True', skiprows=24)
SOPC_C29_inact1.columns=['time', 'num']
SOPC_C29_inact1=SOPC_C29_inact1[4167:8334]
SOPC_C29_inact1.reset_index(drop=True, inplace=True)

SOPC_C39_inact1=pd.read_csv('data/SOPC_Protein_C39_rep1.xvg', delim_whitespace='True', skiprows=24)
SOPC_C39_inact1.columns=['time', 'num']
SOPC_C39_inact1=SOPC_C39_inact1[4167:8334]
SOPC_C39_inact1.reset_index(drop=True, inplace=True)


SOPC_C29_inact2=pd.read_csv('data/SOPC_Inactive_C29_rep2.xvg', delim_whitespace='True', skiprows=24)
SOPC_C29_inact2.columns=['time', 'num']

#df.set_index('A', inplace=True)

SOPC_C39_inact2=pd.read_csv('data/SOPC_Inactive_C39_rep2.xvg', delim_whitespace='True', skiprows=24)
SOPC_C39_inact2.columns=['time', 'num']


SOPC_inact_C29=pd.concat([SOPC_C29_inact1, SOPC_C29_inact2], axis=1)
SOPC_inact_C39=pd.concat([SOPC_C39_inact1, SOPC_C39_inact2], axis=1)

from matplotlib.ticker import MaxNLocator,MultipleLocator
from matplotlib.ticker import AutoMinorLocator
windows=15
###plt.figure(figsize=(

width=0.3
start=5.5
sp = 0.4

ax=plt.subplot(2,3,1)


box_parts = ax.boxplot((DMPC_act_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax.boxplot((DMPC_act_C39[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)

ax.plot(np.linspace(0,5,len(DMPC_C29_act1)), DMPC_C29_act1[['num']].rolling(windows).mean(), color='tab:blue', label='C29' )
ax.plot(np.linspace(0,5,len(DMPC_C39_act1)), DMPC_C39_act1[['num']].rolling(windows).mean() ,color='tab:green',  label='C39')
ax.set_ylim(0,30)
ax.set_xlim(0,5)
ax.set_ylabel('No. of contacts', fontsize=15)
ax.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.set_title('DMPC', fontsize=12)



ax1=plt.subplot(2,3,4)

box_parts = ax1.boxplot((DMPC_inact_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)


box_parts = ax1.boxplot((DMPC_inact_C39[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)


ax1.plot(np.linspace(0,5,len(DMPC_C29_inact1)), DMPC_C29_inact1[['num']].rolling(windows).mean(), color='tab:blue', label='C29' )
ax1.plot(np.linspace(0,5,len(DMPC_C39_inact1)), DMPC_C39_inact1[['num']].rolling(windows).mean(), color='tab:green', label='C39' )
ax1.set_ylim(0,30)
ax1.set_xlim(0,5)
ax1.yaxis.set_major_locator(MaxNLocator(6))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_major_locator(MaxNLocator(5))
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)
ax1.set_title('DMPC', fontsize=12)
ax1.set_ylabel('No. of contacts', fontsize=15)

ax2=plt.subplot(2,3,5)

box_parts = ax2.boxplot((POPC_inact_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax2.boxplot((POPC_inact_C39[['num']][1667:2084].dropna().to_numpy().flatten()),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)
for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)

ax2.plot(np.linspace(0,5,len(POPC_C29_inact1)), POPC_C29_inact1[['num']].rolling(windows).mean(), color='tab:blue', label='C29' )
ax2.plot(np.linspace(0,5,len(POPC_C39_inact1)), POPC_C39_inact1[['num']].rolling(windows).mean(), color='tab:green', label='C39' )
ax2.set_ylim(0,30)
ax2.set_xlim(0,5)
ax2.set_ylabel('No. of contacts', fontsize=15)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)
ax2.yaxis.set_major_locator(MaxNLocator(6))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_major_locator(MaxNLocator(5))
ax2.set_title('POPC', fontsize=12)



ax3=plt.subplot(2,3,2)

box_parts = ax3.boxplot((POPC_act_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax3.boxplot((POPC_act_C39[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)

ax3.plot(np.linspace(0,5,len(POPC_C29_act1)), POPC_C29_act1[['num']].rolling(windows).mean(),color='tab:blue',  label='C29' )
ax3.plot(np.linspace(0,5,len(POPC_C39_act1)), POPC_C39_act1[['num']].rolling(windows).mean() ,color='tab:green',  label='C39')
#ax3.legend()
ax3.set_ylim(0,30)
ax3.set_xlim(0,5)
ax3.set_ylabel('No. of contacts', fontsize=15)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)
ax3.set_title('POPC', fontsize=12)
ax3.yaxis.set_major_locator(MaxNLocator(6))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_major_locator(MaxNLocator(5))

ax4=plt.subplot(2,3,6)

box_parts = ax4.boxplot((SOPC_inact_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax4.boxplot((SOPC_inact_C39[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax4.add_patch(rect)

ax4.plot(np.linspace(0,5,len(SOPC_C29_inact1)), SOPC_C29_inact1[['num']].rolling(windows).mean(), color='tab:blue', label='C29' )
ax4.plot(np.linspace(0,5,len(SOPC_C39_inact1)), SOPC_C39_inact1[['num']].rolling(windows).mean(), color='tab:green', label='C39')
ax4.set_ylim(0,30)
ax4.set_xlim(0,5)
ax4.set_ylabel('No. of contacts', fontsize=15)
ax4.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)
ax4.yaxis.set_major_locator(MaxNLocator(6))
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_major_locator(MaxNLocator(5))
ax4.set_title('SOPC', fontsize=12)


ax5=plt.subplot(2,3,3)

box_parts = ax5.boxplot((SOPC_act_C29[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax5.boxplot((SOPC_act_C39[['num']][1667:2084].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)


for line in plt.gca().get_lines(): line.set_clip_on(False)
rect = Rectangle((5.2,0),1, 30, clip_on=False, ec='k', fill=False)
ax5.add_patch(rect)

plt.plot(np.linspace(0,5,len(SOPC_C29_act1)), SOPC_C29_act1[['num']].rolling(windows).mean(),color='tab:blue',  label='Contacts between AT1R & sn1 chain' )
plt.plot(np.linspace(0,5,len(SOPC_C39_act1)), SOPC_C39_act1[['num']].rolling(windows).mean() ,color='tab:green', label='Contacts between AT1R & sn2 chain')
#plt.legend()
plt.ylim(0,30)
plt.xlim(0,5)
ax5.set_ylabel('No. of contacts', fontsize=15)
plt.xlabel('Time', fontsize=15)
ax5.yaxis.set_major_locator(MaxNLocator(6))
ax5.yaxis.set_minor_locator(AutoMinorLocator(5))
ax5.xaxis.set_minor_locator(AutoMinorLocator(5))
ax5.xaxis.set_major_locator(MaxNLocator(5))
plt.title('SOPC', fontsize=12)
ax5.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=15)


leg=ax5.legend(ncol=2,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-1.4,1.4), markerscale=7 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)


fig = plt.gcf()
plt.subplots_adjust(top=0.85, bottom=0.115, left=0.13, right=0.91, hspace=0.45, wspace=0.73)
plt.Figure.set_size_inches(fig,(11, 7))
plt.savefig('Figure_1_sup.png', dpi=600)
plt.savefig('Figure_1_sup.svg', dpi=600)
#plt.subplots_adjust(hspace=0.4, wspace=0.4)
