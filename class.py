'''class mother():
    def __init__(self, b1, b2 ,b3):
        self.b1 = b1
        self.b2 = b2 
        self.b3 = b3 
    def __str__(self):
        return '{} {} {}'.format(self.b1, self.b2, self.b3)


class Baby(mother):
    def __init__(self, b0,b1, b2 ,b3 ):
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2 
        self.b3 = b3
    def __str__(self):
        return '{} {}'.format(self.b0, super().__str__())

class superbaby(Baby):
    def __init__(self, b0,b1, b2 ,b3,b4):
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2 
        self.b3 = b3
        self.b4 = b4
    def __str__(self):
        return '{} {}'.format(self.b4, super().__str__())

x = Baby('min', ' wasin' , 'wirakit', 'natdanai' ,)
m = superbaby('min', ' wasin' , 'wirakit', 'natdanai' ,'tanapat')
print(x)
print(m)'''

'''class Car():     
    """A simple attempt to model a car."""          
    def __init__(self, make, model, year):         
        """Initialize car attributes."""         
        self.make = make         
        self.model = model         
        self.year = year 
 
        
               
        self.fuel_capacity = 15       
        self.fuel_level = 0
 
    def fill_tank(self):         
        """Fill gas tank to capacity."""         
        self.fuel_level = self.fuel_capacity         
        print("Fuel tank is full.")              
    
    def drive(self):         
        """Simulate driving."""         
        print("The car is moving.")
    
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity: 
            self.fuel_level = new_level 
        else:
            print("The tank can't hold that much!")


me = Car('a','b','c')

y = me.update_fuel_level(6)
print(y)'''

'''class Battery():
    def __init__(self, size=70):         
        """Initialize battery attributes."""         
        # Capacity in kWh, charge level in %.         
        self.size = size         
        self.charge_level = 0 
 
    def get_range(self):         
        """Return the battery's range."""         
        if self.size == 70:             
            return 240         
        elif self.size == 85:             
            return 270

s1 = Battery()
print(s1.charge_level)'''

a = []
for _ in range(500):
    x = 'car' , 'ford' , '2016'
    a.append(x) 

print(a)












        











