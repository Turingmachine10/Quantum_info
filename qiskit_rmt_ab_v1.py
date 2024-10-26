import numpy as np

from qiskit.quantum_info import random_unitary as randU
from qiskit.quantum_info import random_density_matrix as rmt
from qiskit.quantum_info import partial_trace
from qiskit.quantum_info import entropy
import matplotlib.pyplot as plt

runs=5 #number of random trials
n=5 # number of lattice
p=rmt(4**n) #dim
y=np.zeros(n+1,dtype=np.complex_)

nl=0 #

for j in range(0,2*n+1,2):
    
    I=0
    J=np.arange(0,j)
    for i in range(runs):
        U=randU(4**n)
        UpU_=p.evolve(U)
        
        pj=partial_trace(UpU_,list(J))
        e=entropy(pj)
        if i%200==0:
            print(i,e)
        I+=e

    print(I)
    y[nl]=I/runs
    nl+=1
    k=I

yb=np.zeros(n+1,dtype=np.complex_)
nl=0
for j in range(2*n,-1,-2):
    
    I=0
    J=np.arange(0,j)
    for i in range(runs):
        U=randU(4**n)
        UpU_=p.evolve(U)
        
        pj=partial_trace(UpU_,list(J))
        e=entropy(pj)
        '''
        if i%200==0:
            print(i,e)

        '''
        I+=e
        
    print(I)
    yb[nl]=I/runs
    nl+=1
    k=I


Va=np.zeros(n+1)


for i in range(0,n+1):
    Va[i]=4*(n-i)/(4*n) #vol of subsystem/vol of system for each iteration

Vb=Va 
    

print(max)

plt.plot(Va,y)
plt.plot(Vb,yb)
plt.title("5 samples")
plt.xlabel("Volume ratio")
plt.ylabel("Entanglement entropy")
plt.show()


