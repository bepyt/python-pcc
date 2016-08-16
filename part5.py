#--------------------------------
def lprint(items):
    for item in items:
        print(item)
#--------------------------------
def e43():
    vingt = list(range(1,21))
    for entier in vingt:
        print(entier)
#--------------------------------        
def e44():
    million = list(range(1,10**6+1))
    for entier in million:
        print(entier)    
    print(sum(million))
    print(max(million))
    print(min(million))
#-------------------------------- 
def e46():
    odds = list(range(1,21,2))
    for odd in odds:
        print(odd)
#--------------------------------
def e47():
    triple = [3*value for value in range(1,11)]
    lprint(triple)
#--------------------------------
def e48():
    cubes = [value**3 for value in range(1,11)]
    lprint(cubes)
#--------------------------------
def e410():
    million = list(range(1,10**6+1))
    print("The first three items in the list are"+" : "+str(million[:3]))
    print("The  three items in the midle of the list are"+" : "+str(million[43:46]))
    print("The last three items in the the list are"+" : "+str(million[-3:]))
#--------------------------------
def e411():
    pizzas = ['bolo', 'montagnare', 'calzone']
    friends_pizza = pizzas[:]
    pizzas.append('double')
    friends_pizza.append('quiche')
    lprint(friends_pizza)
    lprint(pizzas)
#--------------------------------
def e413():
    foods=('pizza','pates','mozza','truc','machin')
    foods=('pizza','pates','mozza','soupe','lala')
    lprint(foods)
#--------------------------------
e413()
