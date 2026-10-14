
def scalar_mult(val, vec):
    v = []
    for a in vec:
        v.append(a*val)
    return v

def normalise(vec):
    total = 0
    for i in range(len(vec)):
        total += vec[i]**2
    total = total **.5
    new_vec = scalar_mult(1/total, vec)
    return new_vec

def sub(v1, v2):
    if len(v1) != len(v2):
        raise
    v = []
    for i in range(len(v1)):
        v.append(v1[i]-v2[i])
    return v

def add(v1, v2):
    if len(v1) != len(v2):
        raise
    v = []
    for i in range(len(v1)):
        v.append(v1[i]+v2[i])
    return v

def dot(v1, v2):
    if len(v1) != len(v2):
        raise
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def cross(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]
    
