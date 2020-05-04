#Code by B.Varuni
#Date 4 May,2020
#Released Under GNU GPL

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

gain = 192.989*10**9			
num = []
char_eq = [1,-193*10**3,192.989*10**10]
zeros=np.roots(num)
poles=np.roots(char_eq)
Transfer_function = signal.lti(zeros,poles,np.array([gain]))
T, ystep = signal.step(Transfer_function)
print(T)	
plt.plot(T,ystep)
plt.grid()
plt.title("Step response")
plt.xlabel("Time")
plt.ylabel("y(t)")
#if using termux
plt.savefig('./figs/ee18btech11005/ee18btech11005_3.pdf')
plt.savefig('./figs/ee18btech11005/ee18btech11005_3.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11005/ee18btech11005_3.pdf"))
#else
plt.show()
