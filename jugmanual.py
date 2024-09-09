import math
a=int(input("Enter jug A cap: "))
b=int(input("Enter jug B cap: "))
ai=int(input("Initial water in jug A: "))
bi=int(input("Initial water in jug B: "))
af=int(input("Final state of jug A: "))
bf=int(input("Final state of jug B: "))

if a<=0 or b<=0:
    printf("Jug caps must be +ve")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("-ve values are not allowed")
    exit(1)

def wjug(a,b,ai,bi,af,bf):
    print("List of ops: ")
    print("1. Fill jug A completely")
    print("2. Fill jug B completely")
    print("3. Empty jug A")
    print("4. Empty jug B")
    print("5. Pour from A to B until B is full or A is empty")
    print("6. Pour from B to A until A is full or B is empty")
    print("7. Pour from B to A")
    print("8. Pour from A to B")

    while ai!=af or bi!=bf:
        op=int(input("Enter operation(1-8):"))
        if op==1:
            ai=a
        elif op==2:
            bi=b
        elif op==3:
            ai=0
        elif op==4:
            bi=0
        elif op==5:
            pour_amt=min(a,b-bi)
            ai-=pour_amt
            bi+=pour_amt
        elif op==6:
            pour_amt=min(b,a-ai)
            bi-=pour_amt
            ai+=pour_amt
        elif op==7:
            pour_amt=min(b,a-ai)
            ai+=pour_amt
            bi-=pour_amt
        elif op==8:
            pour_amt=min(a,b-bi)
            bi+=pour_amt
            ai-=pour_amt
        else:
            print("Invalid operation. Please choose a number between 1 & 8")
            continue
        print(f"jug A: {ai} , Jug B: {bi}")
        if ai==af and bi==bf:
            print("Final state reached: Jug A= ",ai,", Jug B= ",bi)
            return
    print("Final state reached: Jug A= ",ai,", Jug B= ",bi)
gcd=math.gcd(a,b)
if(af<=a and bf<=b) and (af%gcd==bf%gcd==0):
    wjug(a,b,ai,bi,af,bf)
else:
    print("Final state not achieavable")
    exit(1)
        
            
            
            
    
