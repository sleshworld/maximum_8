class Item:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        return self.value / other.value
    
class Item2:
    def __init__(self, value):
        self.value = value


item1 = Item(5)
item2 = Item2(6)

print(item1+item2)
print(item1/item2)
print(item1*item2)
print(item1-item2)