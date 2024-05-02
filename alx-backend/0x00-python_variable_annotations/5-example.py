from typing import List

vector = List[float]

def vectorFunction(v:vector) -> vector:
    return v; 

x = vectorFunction([4.6, 5.7])
print(x)