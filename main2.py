from turtle import*
import math
from tkinter import*



#HIGH LEVEL


up()
goto(-100,00)
down()

color("red")
c=1
a=90
d=300
while c<= 20:
   width(5)
   forward(d)
   left(a)
   c+=1
   
   
   if c>10:
       
       color("purple")
       
       up()
       goto(50,150)
       down()
       width(20)
       forward(150)
       left(45)
       
up()
goto(50,150)   
down() 
color("orange")
e=1
while e<=15:
       forward(5)  
       goto(50,150)
       left(2)
       forward(5)
       e+=1
       from tkinter import messagebox
reset()
#        
#        
#   # ETOILE
def etoile():
   a=1
   b=1

   while a<=5:
       width(5) 
       color("black")   
       left(70)    
       forward(350)
       right(145)
       forward(350)
       right(150)
       forward(350)
       right(135)
       forward(300)
       right(143)
       forward(380)
       a+=1
       
       if a==6:
           up()
           goto(-300,-500)
           down()
           write("1) Nomme le composé suivant.")
           up()
           goto(-300,-450)
           down()
           write("Exercice")
           up()
           goto(0,0)
           
       
         
etoile()   
reset()
#    
up()  
goto(-16,10) 
color("orange") 

down()
e=1 
while e<2:
       width(20)
       right(45)
       forward(6)
       goto(-16,10)
       e+=1
reset()

#MON NOM
#lettre A
width(20)

color("purple")
left(70)
forward(170)
right(135)
forward(170)
up()
goto(20,80)
down()
left(65)
forward(80)
#lettre k
color("orange")
up()
goto(150,150)
down()
left(270)
forward(150)

up()
goto(150,75)
down()
left(135)
forward(100)
up()
goto(150,75)
down()
right(90)
forward(100)
#lettre L
color("blue")
up()
goto(300,150)
down()
right(45)
forward(150)
right(270)
forward(120)
#lettre E
color("red")
up()
goto(450,150)
down()
right(90)
forward(150)
right(270)
forward(120)
up()
goto(450,75)
down()
left(0)
forward(120)
up()
goto(450,150)
down()
right(0)
forward(120)
reset()

n=1
width(20)
color("blue")


while n<=5:
   up()
   goto(500,-150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   n+=1
   
   
   

   

m=1
width(20)
color("gold")


while m<=5:
   up()
   goto(250,-150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   m+=1
   
   
   

l=1
width(20)
color("red")


while l<=5:
   up()
   goto(0,-150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   l+=1
   
   

p=1
width(20)
color("green")


while p<=5:
   up()
   goto(-250,-150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   p+=1
   
   

q=1
width(20)
color("purple")


while q<=5:
   up()
   goto(-500,-150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   q+=1
   
   
   

i=1
width(20)
color("indigo")


while i<=5:
   up()
   goto(-500,150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   i+=1
   
   

j=1
width(20)
color("orange")


while j<=5:
   up()
   goto(-250,150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   j+=1
   
   

k=1
width(20)
color("yellow")


while k<=5:
   up()
   goto(0,150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   k+=1
   
     

h=1
width(20)
color("pink")


while h<=5:
   up()
   goto(250,150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   h+=1               
   
   
   

     

q=1
width(20)
color("brown")


while q<=5:
   up()
   goto(500,150)
   down()
   left(180)
   forward(200)
   left(90)
   forward(50)
   left(90)
   forward(200)
   left(90)
   forward(50)
   q+=1     
reset()         
   
        
             

width("black")


forward(1)
right(90)
width("black")
forward(100)
right(90)
forward(320)
right(90)
forward(100)
right(90)
forward(320)
reset()

