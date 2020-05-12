import tkinter
import re
from Labo2 import checkregescrossword
app = tkinter.Tk()
app.title("Cross Word")
app.resizable(width = False , height = False)

lineregex = ["(EC|CD)[ABS]",".[GROS]+","C?[KS]+"]
columregex = ["[^CBF](MC|XD)","[CRT]*[ACK]","[AIOEU]*S"]
answer = [] #doit etre ecrit

for n in range(len(lineregex)):
    line = tkinter.Label(app, text = lineregex[n])
    line.grid(row =n+1 , column =0)
for n in range(len(columregex)):
    line = tkinter.Label(app, text = columregex[n])
    line.grid(row =0 , column =n+1)

entry1 = tkinter.Entry(app,width = 2)
entry1.grid(row = 1, column = 1)
entry2 = tkinter.Entry(app,width = 2)
entry2.grid(row = 1, column = 2)
entry3 = tkinter.Entry(app,width = 2)
entry3.grid(row = 1, column = 3)
entry4 = tkinter.Entry(app,width = 2)
entry4.grid(row = 2, column = 1)
entry5 = tkinter.Entry(app,width = 2)
entry5.grid(row = 2, column = 2)
entry6 = tkinter.Entry(app,width = 2)
entry6.grid(row = 2, column = 3)
entry7 = tkinter.Entry(app,width = 2)
entry7.grid(row = 3, column = 1)
entry8 = tkinter.Entry(app,width = 2)
entry8.grid(row = 3, column = 2)
entry9 = tkinter.Entry(app,width = 2)
entry9.grid(row = 3, column = 3)
entry = [entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9]
entrynew = []

def entree():
    for elem in entry:
        x = elem.get()
        entrynew.append(x)                
    answer1 = "".join(entrynew[0:3])
    answer2 = "".join(entrynew[3:6])
    answer3 = "".join(entrynew[6:9])
    answer.append(answer1)
    answer.append(answer2)
    answer.append(answer3)
    
    checkregescrossword(lineregex,columregex,answer) 

resultat = tkinter.Label(app, text ="Resultat")
resultat.grid(row = 5 ,column = 0)

"""
hint = tkinter.Button(app, text ="Indice")
hint.grid(row = 5 ,column = 1)
hint = tkinter.Label(app, text ="Indice")
hint.grid(row = 5 ,column = 2)
"""

button_validate = tkinter.Button(app, text = "OK", command = entree)
button_validate.grid(row = 5 , column= 3)

app.mainloop()
