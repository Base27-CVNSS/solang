#!/usr/bin/env python3
"""Pure stdlib regression checks for Blockchain Equation tutorial."""
import itertools
import math
import pathlib
import random
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]/"examples"))
from blockchain_equation import A, forward, inverse

def eq(x,y,eps=1e-9):
    return math.isclose(x,y,rel_tol=eps,abs_tol=eps)

def main():
    # Theorem 1 / examples:
    samples={
       "ideal": ((1,1,1,1),(1,1,1,1)),
       "bitcoin_hypothetical": ((.85,1,1,1),(1,.85,.85,1)),
       "ethereum_hypothetical": ((.75,1,.95,1),(.95,.7125,.7125,.95)),
       "central_db": ((0,.8,.5,.3),(.12,0,0,.036)),
       "no_consensus": ((.5,1,0,1),(0,0,0,0)),
    }
    for name,(m,want) in samples.items():
       assert all(eq(x,y) for x,y in zip(forward(m),want)),name
    # Theorem 7:
    for M in itertools.product([0.,1.], repeat=4):
       O=forward(M)
       assert all(o in [0.,1.] for o in O)
       for j in range(4):
          assert O[j] == float(all(M[i]==1 or A[j][i]==0 for i in range(4)))
    rng=random.Random(2026)
    for k in range(1000):
       M=tuple(rng.uniform(.1,1) for _ in range(4))
       O=forward(M)
       assert all(0<=x<=1 for x in O)
       # Theorem 5 log-equivalence:
       assert all(eq(math.log(O[j]), sum(A[j][i]*math.log(M[i]) for i in range(4)))
                  for j in range(4))
       # Theorem 9 inversion:
       assert all(eq(u,v) for u,v in zip(inverse(O),M))
       # Theorem 2 monotonicity for each coordinate:
       for i in range(4):
          higher=list(M)
          higher[i]=min(1,M[i]+0.15)
          assert all(n+1e-12>=old for n,old in zip(forward(higher),O))
       # Feasible image: T<=I, V<=R, V*T<=I*I, I*I*R<=V*T
       I,V,R,T=O
       assert T<=I+1e-12 and V<=R+1e-12
       assert V*T<=I*I+1e-12 and I*I*R<=V*T+1e-12
    # Out of image:
    try:inverse((.5,.9,.3,.3))
    except ValueError:pass
    else:raise AssertionError("Reject infeasible outputs")
    print("PASS 5 scenarios + Boolean 16 + 1000 randomized property tests, inverse, monotonicity.")
if __name__=="__main__":main()
