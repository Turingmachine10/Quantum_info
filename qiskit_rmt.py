import numpy as np

from qiskit.quantum_info import random_unitary as randU
from qiskit.quantum_info import random_density_matrix as rmt
from qiskit.quantum_info import partial_trace
from qiskit.quantum_info import entropy
import matplotlib.pyplot as plt


n=8
p=rmt(2**8)
y=np.zeros(n,dtype=np.complex_)

for j in range(1,n,2):
    
    I=0
    J=np.arange(0,j+1)
    for i in range(2500):
        U=randU(2**8)
        UpU_=p.evolve(U)
        
        pj=partial_trace(UpU_,list(J))
        e=entropy(pj)
        if i%200==0:
            print(i,e)
        I+=e

    print(I)
    y[j]=I/2500
    
    k=I

V=np.zeros(n/2)
for i in range(len(J)):
    V[i]=(2**J[i])/2**(7-j[i])
#x=np.linspace(0,2,5000)
print(max)
#print(p)
plt.plot(V,y[::2])
plt.show()
