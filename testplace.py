'''def min (cat , dog ):
    while cat:
        unmin = cat.pop()
        print('hello' + unmin)
        dog.append(unmin)

cat = ['a','b','c']
dog = []

min (cat,dog)

print('cat: ' , cat)
print('dog:' , dog)'''


'''def mu (B):
    for b in B:
        msg = 'HelloandHowareYou! ' +  b +': Yaa.. Im good '
        print(msg)

x = ['q', 'a']
mu(x)



def greet_users(names):     
    """Print a simple greeting to everyone."""     
    for name in names:         
        msg = "Hello, " + name + "!"         
        print(msg) 
 
usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames) '''

'''def make_pizza(size, *toppings):     
    """Make a pizza."""     
    print("\nMaking a " + size + " pizza.")     
    print("Toppings:")     
    for topping in toppings:         
        print("- " + topping) 
 
#Make three pizzas with different toppings.  
make_pizza('small', 'pepperoni') 
make_pizza('large', 'bacon bits', 'pineapple') 
make_pizza('medium', 'mushrooms', 'peppers','onions', 'extra cheese')'''


def list_user (fname , lname , *info):
    print('first name: ' + fname + 'lastname: '  + lname )
    for inf in info:
        print(inf)

list_user('sittisak', 'rodpraya', 'heigh = 170cm.', 'weight = 58' )




