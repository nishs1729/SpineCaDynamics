#!/usr/bin/env python

import numpy as np
from collections import Counter,OrderedDict

tmin_base = 0 # start of simulation at base voltage 
tmax_base = 0.011 # end of base voltage and start of AP 
tmax = 1 # end of simulation
t_step = 1e-5 # time step 
tau = 0.01 # decay time constant of AP

peak_V = 100 # peak of the action potential in mV

# Do not change from here on
mem_pot_base = [-65 for t in np.arange(tmin_base,tmax_base,t_step)] 
mem_pot_ap = [-65+(peak_V*np.exp(-1*(t-tmax_base)/tau)) for t in np.arange(tmax_base,tmax,t_step)] # Membrane voltage profile 
mem_pot = mem_pot_base + mem_pot_ap
times = np.arange(tmin_base,tmax,t_step)

alpha0 = [8.08,13.4,8.78,34.7] # 1/ms
beta0 = [5.76,12.6,16.3,3.68] # 1/ms
V = [49.14,42.08,55.31,26.55] # mV

for i in [1,2,3,4]:
    alpha = [1000*alpha0[i-1] * np.exp(v/V[i-1]) for v in mem_pot]
    beta = [1000*beta0[i-1] * np.exp(-v/V[i-1]) for v in mem_pot]
    f = r'./vdcc_alpha_'+str(i)+'.txt'
    np.savetxt(f,zip(times,alpha),fmt='%1.7f %f')
    f = r'./vdcc_beta_'+str(i)+'.txt'
    np.savetxt(f,zip(times,beta),fmt='%1.7f %f')

gamma = 3.72e-12 # siemens
F = 96485.33 # coulomb/mole
Na = 6.022e23 # 1/mole
kca = [gamma*Na*v*(1e-3)*(0.393 - np.exp(-v/80.36))/(2*F*(1.0 - np.exp(v/80.36))) for v in mem_pot]
np.savetxt(r'./vdcc_kca.txt',zip(times,kca),fmt='%1.7f %f')

# vrange=np.arange(-80,0,5)
# plt.plot(vrange,[kca(v) for v in vrange],'b-')
# plt.show()
