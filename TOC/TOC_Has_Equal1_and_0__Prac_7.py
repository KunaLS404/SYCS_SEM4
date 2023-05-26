
a=0
b=0

def state_q0(n):
    global a,b
    if(len(n)==0):
        state_q2()
    else:
        if(n[0]=="0"):
            a+=1
            state_q0(n[1:])
        elif(n[0]=="1"):
            b+=1
            state_q1(n[1:])

def state_q1(n):
    global a,b
    if(len(n)==0):
        state_q2()
    else:
        if(n[0]=="1"):
            b+=1
            state_q1(n[1:])
        elif(n[0]=="0"):
            a+=1
            state_q0(n[1:])

def state_q2():
    global a,b
    if(a==b):
        print("Equal")
    else:
        print("Not Equal")

n="1001"
state_q0(n)
