# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:43:45 2020

@author: Micheal
"""


from tkinter import *
import math
import webbrowser
from numpy import *
window=Tk()
window.title("planet information")
window.geometry('1000x1000')
class planets(object):
    def __init__(self,name, mass, distance_from_sun,diameter,website):
        self.name=name
        self.mass=mass
        self.PDS=distance_from_sun
        self.diameter=diameter
        self.website=website
var1=StringVar() #declaring global string variable
var2=StringVar() #declaring global string variable
var3=DoubleVar() #declaring global integer variable
var4=StringVar() #declaring global string variable
var5=StringVar() #declaring global integer variable
var6=DoubleVar() #declaring global integer variable
var6.set(1496*math.pow(10,8))
var7=StringVar() #declaring global string variable
#declaring global string variable to store url
#displaying planet details 
def displaydetails(t):
    o=globals()['var1']
    p=globals()['var2']
    q=globals()['var3']
    r=globals()['var4']
    u=globals()['var7']
    o.set(t.name)
    p.set(t.mass)
    q.set(t.PDS)
    r.set(t.diameter)
    u.set(t.website) 
#all planets
Mercury=planets("Mercury",3.3022*math.pow(10,23),0.39,4879.4,"https://en.wikipedia.org/wiki/Mercury_(planet)")
Venus=planets("Venus",4.8685*math.pow(10,24),0.732,12104,"https://en.wikipedia.org/wiki/Venus_(planet)")
Earth=planets("Earth",5.9736*math.pow(10,24),1,12756,"https://en.wikipedia.org/wiki/Earth_(planet)")
Mars=planets("Mars",6.4185*math.pow(10,23),1.524,6779,"https://en.wikipedia.org/wiki/Mars_(planet)")        
Jupiter=planets("Jupiter",1.8986*math.pow(10,27),5.203,142800,"https://en.wikipedia.org/wiki/Jupiter_(planet)")
Saturn=planets("Saturn",5.6846*math.pow(10,26),9.539,120660,"https://en.wikipedia.org/wiki/Saturn_(planet)")
Uranus=planets("Uranus",8.6810*math.pow(10,25),19.18,51118,"https://en.wikipedia.org/wiki/Uranus_(planet)")
Neptune=planets("Neptune",10.243*math.pow(10,25),30.06,49528,"https://en.wikipedia.org/wiki/Neptune_(planet)")

planetlist=array([Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune])
#button for planet calculations
b1=Button(window,text="Mercury",width=20,height=1,bg="yellow",command=lambda: displaydetails(Mercury)).place(x=30,y=60)
b2=Button(window,text="Venus",width=20,height=1,bg="yellow",command=lambda: displaydetails(Venus)).place(x=30,y=90)
b3=Button(window,text="Earth",width=20,height=1,bg="yellow",command=lambda: displaydetails(Earth)).place(x=30,y=120)
b4=Button(window,text="Mars",width=20,height=1,bg="yellow",command=lambda: displaydetails(Mars)).place(x=30,y=150)
b5=Button(window,text="Jupiter",width=20,height=1,bg="yellow",command=lambda: displaydetails(Jupiter)).place(x=30,y=180)
b6=Button(window,text="Saturn",width=20,height=1,bg="yellow",command=lambda: displaydetails(Saturn)).place(x=30,y=210)
b7=Button(window,text="Uranus",width=20,height=1,bg="yellow",command=lambda: displaydetails(Uranus)).place(x=30, y=240)
b8=Button(window,text="Neptune",width=20,height=1,bg="yellow",command=lambda: displaydetails(Neptune)).place(x=30,y=270)

#displaying details on the window
l1=Label(window,text="Planet Name: ",width=30,height=1).place(x=200,y=30)
l2=Label(window,text="Planet Mass: ",width=30,height=1).place(x=200,y=60)
l3=Label(window,text="Planet's distance from sun: ",width=30,height=1).place(x=200,y=90)
l4=Label(window,text="Planet diameter: ",width=30,height=1).place(x=200,y=120)
diplayplanetdetails=Label(window,text="Planet Details are given below",width=40,height=1).place(x=250,y=0)
l5=Label(window,textvariable=var1,width=20,height=1).place(x=400,y=30)
l6=Label(window,textvariable=var2,width=24,height=1).place(x=400,y=60)
l7=Label(window,textvariable=var3,width=20,height=1).place(x=400,y=90)
l8=Label(window,textvariable=var4,width=20,height=1).place(x=400,y=120)

#converting au to km
def AU_to_KM():
    m=globals()['var5']
    m.set(var3.get()*var6.get())

lAU=Label(window,text="If you want to convert AU to km click submit or to browse site click browse ",width=65,height=1).place(x=300,y=180)
bsubmit=Button(window,text="SUBMIT",bg="yellow",width=10,height=1,command=AU_to_KM).place(x=600,y=210)
lKM=Label(window,textvariable=var5 ,width=20,height=1).place(x=300,y=210)
#label to display sites
lsites=Label(window,textvariable=var7,width=40,height=1).place(x=300, y=240)
browse=Button(window,text="BROWSE",bg="yellow", width=10, height=1,command=lambda:webbrowser.open(var7.get())).place(x=600,y=240)
#to create checkbuttons to display distances between the planets
ldistanceinfo=Label(window, text="to find the distance between any two planets tick the planets",width=60,height=1).place(x=600,y=0)
#intvar declarations for each checkbox
varc1=IntVar()
varc2=IntVar()
varc3=IntVar()
varc4=IntVar()
varc5=IntVar()
varc6=IntVar()
varc7=IntVar()
varc8=IntVar()
varc9 = IntVar()
planet1=StringVar()
planet2=StringVar()
intermediatedistance=StringVar()
#function for displaying distance between two
def display_intermediate_distance():
    x=varc1.get()
    y=varc2.get()
    z=varc3.get()
    a=varc4.get()
    b=varc5.get()
    c=varc6.get()
    d=varc7.get()
    e=varc8.get()
    distance = 0
    variablelist=[x,y,z,a,b,c,d,e]
    if variablelist.count(1) != 2:
        varc9.set(0.0)
        return
    else:
        for i in range(len(variablelist)):
            if variablelist[i] == 1:
                distance = planetlist[i].PDS - distance
    varc9.set(distance)

c1=Checkbutton(window, text="Mercury", bg="cyan",width=10,height=1,variable=varc1).place(x=800,y=30)
c2=Checkbutton(window, text="Venus", bg="cyan",width=10,height=1,variable=varc2).place(x=800,y=60)
c3=Checkbutton(window, text="Earth", bg="cyan",width=10,height=1,variable=varc3).place(x=800,y=90)
c4=Checkbutton(window, text="Mars", bg="cyan",width=10,height=1,variable=varc4).place(x=800,y=120)
c5=Checkbutton(window, text="Jupiter", bg="cyan",width=10,height=1,variable=varc5).place(x=800,y=150)
c6=Checkbutton(window, text="Saturn", bg="cyan",width=10,height=1,variable=varc6).place(x=800,y=180)
c7=Checkbutton(window, text="Uranus", bg="cyan",width=10,height=1,variable=varc7).place(x=800,y=210)
c8=Checkbutton(window, text="Neptune", bg="cyan",width=10,height=1,variable=varc8).place(x=800,y=240)
bcalcdist=Button(text="DISTANCE", bg="yellow",width=10, height=1, command= display_intermediate_distance).place(x=800, y=270)
bcalcdist_label = Label(window,textvariable=varc9,width=20,height=1).place(x=800, y=300)

window.mainloop()