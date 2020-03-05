#Question 1 :

def call1(fonction):
    return fonction()
def hello():
    print("Hello")

call1(hello)

#Question 2 : 

def call2(fonction,*args):
    return fonction(*args)
def add(a,b):
    return a+b

print(call2(add,2,9))

#Question 3 :

def compute(a,b,op=add):
    return op(a,b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mult(a,b):
    return a*b
def call3(fonction,*args,**kwargs):
    return fonction(*args,**kwargs)

print(call3(compute,2,9))
print(call3(compute,2,9,op = sub))
print(call3(compute,2,9,op = div))
print(call3(compute,2,9,op = mult))