clubsaturday = {'1':'mumin', '2':'fousee', '3':'deng', '4':'sin' ,'5':'kit' ,'6':'vee'}
print(clubsaturday)
for x, y in clubsaturday.items() :
    print(x + ':' + y)


# Start with an empty list.

# Make a new user, and add them to the list.
new_user = {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 }

# Make another new user, and add them as well.
new_user = {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 }

# Show all information about each user.

for k, v in new_user.items():
    print(k + ": " + v)
    
