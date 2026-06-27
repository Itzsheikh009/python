#Map,reduce and filter  Function
#---------------------Find area of a circle using map function

# import math
# def area(r):
#     return math.pi*(r**2)

# radii = [1,2,3,4,5]
# areas = []
# for r in radii:                         (Withour using map function) --- (FUNCTIONS,ITERABLE)
#     a = area(r)
#     areas.append(a)
# print(areas)

#by using map function
# import math
# def area(r):
#     return math.pi*(r**2)

# r=[1,2,3,4,5]
# areas=map(area,r)
# print(list (areas))

#---------------------Filter function  (FUNCTION,DATA)
import statistics
data=[1,12,13,4,55,61,77,8,9]
avg=statistics.mean(data)
print(avg)

filtered_data=filter(lambda x: x > avg, data)
print(list(filtered_data))

