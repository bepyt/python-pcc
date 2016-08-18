pizza = {
    'crust': 'thick',
    'toppings': ['mush','extra cheese'],
    }

print(pizza)
print('your pizza ' + pizza['crust'] + ' with :')
for top in pizza['toppings']:
    print("\t" + top)