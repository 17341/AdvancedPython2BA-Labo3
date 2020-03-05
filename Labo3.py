#Question 1 :
print ("Question1 : ")
def call1(fonction):
    return fonction()
def hello():
    print("Hello")

call1(hello)

#Question 2 : 
print ("Question2 : ")
def call2(fonction,*args):
    return fonction(*args)
def add(a,b):
    return a+b

print(call2(add,2,9))

#Question 3 :
print ("Question3 : ")
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
#Question 4 :
    #C'est le meme code que pour la question 5 mais n = 1
#Question 5 :
print ("Question5 : ")
import time

def sleep(n):
    def decorator(f):
        def wrapper(*args,**kwargs): #Le **kwargs ici n'est pas necessaire mais on prefere le mettre tout le temps .
            time.sleep(n)
            result = f(*args,**kwargs)
            return result
        return wrapper
    return decorator

@sleep(5)           
def printnum(i):    # on defini f = printnum
    print (i)

cnt = 3
while cnt > 0:
    printnum (cnt)
    cnt -= 1
print ("KA-BOOM!")

#Question 6 : 
print ("Question6 : ")
def binrep(n):
    while n > 0 : 
        bit = n%2
        n//= 2
        yield bit
        
b = binrep(12) #b est un objet du generateur
while True : 
    try:
        print(next(b))
    except StopIteration : 
        break

#Question 7 : 
print ("Question7 : ")
class NaturalIterator:
    def __init__(self,n):
        self.__generator = binrep(n)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.__generator)

class Natural : 
    def __init__(self,n):
        self.__n = n
    def __iter__(self):
        return NaturalIterator(self.__n)

for e in Natural(42):
    print(e)