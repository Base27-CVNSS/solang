#!/usr/bin/env python3
"""Mô hình B_A = (C*d*L, P*C*d, P*d, C*d*L**2).
Giáo dục / số minh họa, KHÔNG phải chỉ số blockchain thực tế.
Không phụ thuộc thư viện ngoài. Python >=3.8.
"""
import math
import sys

A = ((0, 1, 1, 1), (1, 1, 1, 0), (1, 0, 1, 0), (0, 1, 1, 2))

def forward(m):
    """M = (P,C,Delta,L) trong [0,1]^4; 0**0 == 1."""
    if len(m) != 4 or any(not math.isfinite(x) or x < 0 or x > 1 for x in m):
        raise ValueError("Phải nhập 4 số hữu hạn trong [0,1]")
    return tuple(math.prod(x**a for x,a in zip(m,row)) for row in A)

def inverse(o):
    """O=(I,V,R,T) >0; trả lại M, hoặc raise nếu không thuộc miền ảnh."""
    if len(o) != 4 or any(not math.isfinite(x) or x <= 0 or x > 1 for x in o):
        raise ValueError("Nghịch đảo yêu cầu 4 giá trị trong (0,1]")
    I,V,R,T = o
    out = (V*T/(I*I), V/R, I*I*R/(V*T), T/I)
    if any(x > 1+1e-10 or x <= 0 for x in out):
        raise ValueError("Không thuộc miền ảnh của mô hình với M trong (0,1]")
    return tuple(min(1.0,x) for x in out)

def self_test():
    import itertools, random
    assert forward((.75,1,.95,1)) == (.95,.7124999999999999,.7124999999999999,.95) or all(
        abs(a-b)<1e-12 for a,b in zip(forward((.75,1,.95,1)),(.95,.7125,.7125,.95)))
    for m in itertools.product((0.0,1.0),repeat=4):
        o=forward(m)
        assert all(x in (0.0,1.0) for x in o)
        assert all(o[j] == float(all(m[i] == 1 or A[j][i] == 0 for i in range(4))) for j in range(4))
    r=random.Random(27)
    for _ in range(1000):
        m=tuple(r.uniform(.08,1) for _ in range(4))
        o=forward(m)
        back=inverse(o)
        assert all(abs(x-y)<1e-9 for x,y in zip(m,back))
    try: inverse((.5,.9,.3,.3))
    except ValueError: pass
    else: raise AssertionError("Infeasible outputs not rejected")
    print("PASS: Boolean(16), 1000 inverse tests, infeasible point, Ethereum arithmetic.")

if __name__ == "__main__":
    if len(sys.argv)==2 and sys.argv[1]=="--self-test":
        self_test()
    elif len(sys.argv)==5:
        m=tuple(map(float,sys.argv[1:]))
        o=forward(m)
        print("Input M (P,C,Delta,L) =",m)
        print("Output O (I,V,R,T) =",o)
        print("Hợp lệ TRONG MÔ HÌNH:",all(x>0 for x in m))
        print("Đây là điểm mô phỏng, KHÔNG đại diện chỉ số đo mạng thật.")
    else:
        print("Cách dùng: python3 examples/blockchain_equation.py P C DELTA L")
        print("Hoặc: python3 examples/blockchain_equation.py --self-test")
