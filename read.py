import matplotlib.pyplot as mat
import pandas as pd 
import numpy as np
from scipy.io import wavfile as wav
type = 'freewrite';
num = 7;
tablet = pd.read_table('./exports/NLS_'+str(num)+'_'+type     +'.tab.txt', header=0);
eye = pd.read_table('./exports/NLS_'+str(num)+'_'+type+'.eye.txt', header=0);
rate, audio = wav.read('./exports/NLS_'+str(num)+'_'+type+'.wav');
tab_t = tablet[['T']];
tab_x = tablet[['X']];
tab_y = tablet[['Y']];
tab_p = tablet[['P']];
eye_t = eye[['T']];
eye_x = eye[['X']];
eye_y = eye[['Y']];
fig = mat.figure();
ax1 = fig.add_subplot(3,1,1);
ax2 = fig.add_subplot(3,1,2);
ax3 = fig.add_subplot(3,1,3);
ax1.plot(tab_t, tab_x, '-b', label='tablet x'); 
ax1.plot(tab_t,tab_y, '-r', label='tablet y');
ax1.plot(tab_t,tab_p, '-g', label='tablet p');
ax2.plot(eye_t, eye_x, '-b', label='eye x'); 
ax2.plot(eye_t, eye_y, '-r', label='eye y');
ax3.plot(audio);
leg = ax1.legend();
leg2 = ax2.legend();
fig.savefig('plot'+str(num)+'_'+type+'.png');
