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

kB = [1200 * np.exp(-v/17) for v in mem_pot]
kU = [10800 * np.exp(v/47) for v in mem_pot]
f = r'./nmdar_kB_BAP.txt'
np.savetxt(f,zip(times,kB),fmt='%1.7f %f')
f = r'./nmdar_kU_BAP.txt'
np.savetxt(f,zip(times,kU),fmt='%1.7f %f')

gamma = 3.72e-12 # siemens
F = 96485.33 # coulomb/mole
Na = 6.022e23 # 1/mole
kca = [gamma*Na*v*(1e-3)*(0.393 - np.exp(-v/80.36))/(2*F*(1.0 - np.exp(v/80.36))) for v in mem_pot]
np.savetxt(r'./nmdar_kca_BAP.txt',zip(times,kca),fmt='%1.7f %f')

