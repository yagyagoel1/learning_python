import math 
def circle_stats(radius):
    area = math.pi*radius **2
    circumference = 2*math.pi*radius
    area = round(area,2)
    circumference = round(circumference,2)
    
    return area, circumference
print(circle_stats(5))