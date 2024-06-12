#Desarrollar una función que permita convertir un número romano en un número decimal.




#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado,  
# pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#c. Utilizar un vector para representar la mochila.


mochi=["comunicador","botella de agua","galletitas","sable de luz","pañuelitos","desodorante"]
def usar_la_fuerza(mochila):
    i=0
    if i>=len(mochila):
            return ("ya no hay objetos en la mochila, el sable no esta")
    elif mochila[i]=="sable de luz":
        return ("encontre el sable")
    
    else:
        return usar_la_fuerza(mochila(i+1))
    
        
print (usar_la_fuerza(mochi))
    