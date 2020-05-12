import re
import sys
"""
#Question 1:
pattern1 = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
p1= re.compile(pattern1)
print(p1.match('+32 488 30 38 89') is not None)

pattern2 = r'\-?|\+?[1-9]+$'
p2= re.compile(pattern2)
print(p2.match('780') is not None)

pattern3 = r'[1-9][A-Z]{3}[1-9]{3}|[1-9][1-9]{3}[A-Z]{3}'
p3= re.compile(pattern3)
print(p3.match('7MMM888') is not None)

pattern4 = r'[A-Z]:\\*'
p4= re.compile(pattern4)
m4 = p4.match('C:\python.py') 
print(m4 is not None)
if m4 is not None:
    pass

#Question 2:
pattern5 = r'\+\d+|\-\d+|\d+'
p5 = re.compile(pattern5)
with open (sys.argv[1]) as file :
    for i, line in enumerate(file):
        instances=p5.findall(line)
        if len(instances)!= 0:
            print("Line {}:{}".format(i+1,",".join(instances)))

#Question 3:
pattern6 = r'^(?P<protocol>[^/:]+)://(?P<domain>[^/]+)/(?P<path>.*)$'
p6 = re.compile(pattern6)
url= sys.argv[1]
result = p6.match(url)
groups = ['protocol','domain','path']
for group in groups:
    if(result.group(group)) is not None:
        print("{}: {}".format(group.capitalize(),result.group(group)))
"""
#Question 4:
def checkregescrossword(lineregex,columregex,answer):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    point = 0
    for elem in answer:
        list1.append(elem)
    for i in range(3):
        for elem in list1:    
            list2.append(elem[i])
        list3.append(list2[0:3])
        del list2[0:3]
    for elem in list3:
        list4.append("".join(elem))
    for i in range(3):
        pattern7 = lineregex[i]
        p7 = re.compile(pattern7)
        result7= p7.match(list1[i])
        pattern8 = columregex[i]
        p8 = re.compile(pattern8)
        result8= p8.match(list4[i])
        if result7 and result8 is not None : 
            point += 1
        else:
            pass
    if point == 3 :
        print("Bien joué")
    else :
        print("Faux")
#checkregescrossword(["(EC|CD)[ABS]",".[GROS]+","C?[KS]+"],["[^CBF](MC|XD)","[CRT]*[ACK]","[AIOEU]*S"],["ECA","MRO","CKS"])