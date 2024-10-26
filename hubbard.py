from math import pi
import matplotlib.pyplot as plt
#import numba
import scipy

import numpy as np
import rustworkx as rx
from qiskit_nature.second_q.hamiltonians.lattices import (
    BoundaryCondition,
    Lattice,
    LatticeDrawStyle,
    LineLattice)
from qiskit_nature.second_q.hamiltonians import FermiHubbardModel

from qiskit_nature.second_q.mappers import JordanWignerMapper #fermionic operator to spin operator mapper

import qiskit
from qiskit.quantum_info import entropy,partial_trace


mapper = JordanWignerMapper()

from qiskit_algorithms import NumPyMinimumEigensolver #hamiltonian solver

numpy_solver = NumPyMinimumEigensolver() #uses exact diagonalisation

from qiskit_nature.second_q.algorithms import GroundStateEigensolver




num_nodes = 4
boundary_condition = BoundaryCondition.OPEN
line_lattice = LineLattice(num_nodes=num_nodes, boundary_condition=boundary_condition)

t=-3.497 #kinetic
v=0 #onsite potential
u=5 #on-site interaction energy

fhm=FermiHubbardModel(line_lattice.uniform_parameters(uniform_interaction=t,uniform_onsite_potential=v,),onsite_interaction=u,)

ham=fhm.second_q_op().simplify()
print(ham)

qubit_fhm=mapper.map(ham)
print(qubit_fhm)


m=qubit_fhm.to_matrix()
print("matrix computed")

e,v=np.linalg.eigh(m) #very slow for 6 lattices (computes all the eigenvalues)
#e,v=scipy.sparse.linalg.eigsh(m,2,which="SM",maxiter=100,)

print("eigenvalues computed")

dmf=qiskit.quantum_info.DensityMatrix(v[:,0],dims=(4,)*num_nodes)
#ee3=entropy(partial_trace(dmf,[0,1,2]))

print("computing entanglement entropies")

vr=np.zeros(num_nodes+1)
en=np.zeros(num_nodes+1)

def compute_entro(dmf):
    for i in range(num_nodes+1):
        en[i]=entropy(partial_trace(dmf,list(range(i))))
        print(en[i])
        vr[i]=4*(num_nodes-i)/(4*num_nodes)
    print(e)
    plt.plot(vr,en)
    plt.show()




compute_entro(dmf)
