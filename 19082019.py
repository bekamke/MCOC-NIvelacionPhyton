"""
Created on Mon Aug 19 22:58:15 2019

@author: Benjamin Kamke
"""
#Estoy mezclando todos los ejemplos que salieron en el video

a = 1 # Se le asigna el valor a una variable

b = 2 # Se le asigna el valor a una variable

c = 5 # Se le asigna el valor a una variable

d = 4 # Se le asigna el valor a una variable

e = 7 # Se le asigna el valor a una variable

f = 7 # Se le asigna el valor a una variable

#1. En este caso veremos como funciona el IF

if a < b: # Se asigna la variable IF para poner una condición

    print "a es menor que b" #Si es que la condicion del IF se cumple se va a imprimir lo que sale siguiente al print

elif a == b: #ELIF es una variable para poner otra condicion por si no cumple la del IF
    
    print "a es igual a b" #Si es que se cumple la condicion se va a imprimir lo que sale siguiente al print

    
else: # Se asigna la variable ELSE para poner una "condicion" si es que la del IF o ELIF no se cumplen

    print "b es mayor que a" #Si es que no se cumple IF y ELIF, se cumplira la condicion del ELSE y se va a imprimir lo que sale siguiente al print
 
#2. En este caso veremos como funciona el ELSE
 
if c < d:  #Si es que la condicion del IF se cumple se va a imprimir lo que sale siguiente al print
    
    print "c es menor que d" #Si es que la condicion del IF se cumple se va a imprimir lo que sale siguiente al print
    
elif c == d: #ELIF es una variable para poner otra condicion por si no cumple la del IF
    
    print "c es igual a d" #Si es que se cumple la condicion se va a imprimir lo que sale siguiente al print    
    
else: # Se asigna la variable ELSE para poner una "condicion" si es que la del IF o ELIF no se cumplen
    
    print" d es mayor que c" #Si es que no se cumple IF y ELIF, se cumplira la condicion del ELSE y se va a imprimir lo que sale siguiente al print
    
#3. En este caso veremos como funciona el ELIF
    
if e < f:  #Si es que la condicion del IF se cumple se va a imprimir lo que sale siguiente al print
    
    print "e es menor que f" #Si es que la condicion del IF se cumple se va a imprimir lo que sale siguiente al print
    
elif e == f: #ELIF es una variable para poner otra condicion por si no cumple la del IF
    
    print "e es igual a f" #Si es que se cumple la condicion se va a imprimir lo que sale siguiente al print 
    
else: # Se asigna la variable ELSE para poner una "condicion" si es que la del IF o ELIF no se cumplen
    
    print" e es mayor que f" #Si es que no se cumple IF y ELIF, se cumplira la condicion del ELSE y se va a imprimir lo que sale siguiente al print
    