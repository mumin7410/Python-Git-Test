users = ['a','c','f','b']
users.sort()
print(users)

'''numbers = list(range(1, 1000001))
print(numbers)'''

for user in users:
 print("Welcome, " + user + "!")
print("Welcome, we're glad to see you all!")

dimensions = (800, 600)
print(dimensions)
dimensions = (1200, 900)
print(dimensions)

dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
for dog in dogs:
 print("Hello " + dog + "!")
print("I love these dogs!")
print("\nThese were my first two dogs:")
old_dogs = dogs[:2]
for old_dog in old_dogs:
 print(old_dog)
del dogs[0]
dogs.remove('peso')
print(dogs)