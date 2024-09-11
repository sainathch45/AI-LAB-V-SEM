import math
from collections import deque
a=int(input("Jug A capacity:"))
b=int(input("Jug B capacity:"))
ai=int(input("Initial water in jug A:"))
bi=int(input("Initial water in jug B:"))
af=int(input("Final in A:"))
bf=int(input("Final in B:"))

if a<=0 or b<=0:
    print("Jug capacities must be +ve")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("-ve Values not allowed")
    exit(1)
if ai==af and bi==bf:
    print(f"Initial state is already the final stae: jug a = {ai} and jug b= {bi}")
    exit()

def bfs_wjug(a,b,ai,bi,af,bf):
    visited=set()
    queue=deque([(ai,bi,[])])

    while queue:
        curr_ai,curr_bi,ops=queue.popleft()

        if(curr_ai,curr_bi) in visited:
            continue
        visited.add((curr_ai,curr_bi))

        if curr_ai == af and curr_bi == bf:
            for i,op in enumerate(ops):
                print(f"Step {i+1}: {op}")
            print(f"final state reached: jug a = {curr_ai} and jug b= {curr_bi}")
            return

        possible_ops=[
            (a,curr_bi,"Fill Jug A"),
            (curr_ai,b,"Fill Jug B"),
            (0,curr_bi,"Empty Jug A"),
            (curr_ai,0,"Empty Jug B"),
            (curr_ai - min(curr_ai,b-curr_bi),curr_bi + min(curr_ai, b- curr_bi),"Pour from Jug A to B"),
            (curr_ai + min(curr_bi,a-curr_ai),curr_bi - min(curr_bi, a- curr_ai),"Pour from Jug B to A"),]


        for next_ai,next_bi,op in possible_ops:
            if(next_ai,next_bi) not in visited:
                queue.append((next_ai, next_bi,ops+[op]))
    print("No solution found.")
    return

gcd= math.gcd(a,b)
if(af<=a and bf<=b) and (af%gcd==bf%gcd==0):
    bfs_wjug(a,b,ai,bi,af,bf)
else:
    print("The final state is not achievable with the given capacities.")
    exit()
    
    
