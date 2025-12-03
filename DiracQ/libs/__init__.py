import os, sys
import uuid
import numpy
import numpy as np
from numpy import array, matrix, zeros, ones, eye, pi
from numpy import matmul, kron, hstack, vstack
from numpy import sin, cos, log2, pi, e
from functools import reduce
from itertools import *


"""**Basis Vectors**"""
# Z Basis
KET_0 =array([[1.],  [0.]])
KET_1 =array([[0.],  [1.]])

# X Basis or Hadamard Basis
KET_XP = (KET_0 + KET_1)/np.sqrt(2)
KET_XM = (KET_0 - KET_1)/np.sqrt(2)

# Y Basis
KET_YP = (KET_0 + 1j*KET_1)/np.sqrt(2)
KET_YM = (KET_0 - 1j*KET_1)/np.sqrt(2)



###### ----------------------------- ######
"""**Pauli's  Matrices(not scaled in $hslash$)**"""

PauliX     =  array([[complex(0., 0.), complex(1., 0.)],
                     [complex(1., 0.), complex(0., 0.)]])

PauliY     =  array([[complex(0., 0.), -complex(0., 1.)],
                     [complex(0., 1.), complex(0., 0.)]])

PauliZ     =  array([[complex(1., 0.), -complex(0., 0.)],
                     [complex(0., 0.), -complex(1., 0.)]])


##Order: Source -> S, Target -> T
CNOT = array([[1., 0., 0., 0.],
              [0., 1., 0., 0.],
              [0., 0., 0., 1.],
              [0., 0., 1., 0.]])

INV_CNOT = array([[1.,0.,0.,0.],
                  [0.,0.,0.,1.],
                  [0.,0.,1.,0.],
                  [0.,1.,0.,0.]])


CZ = array([[1.,0.,0.,0.],
            [0.,1.,0.,0.],
            [0.,0.,1.,0.],
            [0.,0.,0.,-1.]])


INV_CZ = array([[1.,0.,0.,0.],
                [0.,0.,1.,0.],
                [0.,0.,0.,-1.],
                [0.,1.,0.,0.]])

"""**Bell States(2x2)**"""
BELL_00 = kron(KET_0, KET_0) + kron(KET_1, KET_1)
BELL_00 = BELL_00/pow(2, 0.5)

BELL_01 = kron(KET_0, KET_1) + kron(KET_1, KET_0)
BELL_01 = BELL_01/pow(2, 0.5)

BELL_10 = kron(KET_1, KET_0) - kron(KET_0, KET_1)
BELL_10 = BELL_10/pow(2, 0.5)

BELL_11 = kron(KET_0, KET_0) - kron(KET_1, KET_1)
BELL_11 = BELL_11/pow(2, 0.5)

"""***Single Qubit Unitary Operators***"""

X = array([[0., 1.,],[1., 0.]])
Y = array([[0., -1j,],[1j, 0.]])
Z = array([[1., 0.,],[0., -1.]])
H = array([[1., 1.,],[1., -1.]])/pow(2, 0.5)



