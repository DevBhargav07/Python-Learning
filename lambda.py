from functools import reduce

#we will learn about fucntions in python 
a = [1,2,3,4,5,6,7]

mapValue = list(map(lambda x: x ** 2, a))

mapOveriding = list(map(lambda x: x%2 == 0, a))
print(f'map overiding is {mapOveriding}')

filterValue = list(filter(lambda x: x %2 != 0 , a))
#filter is to apply on all the elements inside an iterator you provided and to perform some tasks

print(mapValue)
print(filterValue)


keyvalues = [
    {"else": "if",
    "if": "else-if bhai bolthe public"}
]
try:
    keyvalues = [(1,'a',True), (2,'c', False), (3,'b',True)]
    keyS = sorted(keyvalues, key=lambda x: x[1])
    print(keyS)
except IndexError:
    print('An Index error occured here!')


#now we will use reduce from functools - this does is compressing or reducing the number of working times a function
#finding the sum of a list without using the default sum functions
sumofvalues = reduce(lambda crnt, x: crnt + x, a)
print(sumofvalues)
print(sum(a))


#finding the max_value in list without and with using the max function
maxofvalues = reduce(lambda crnt, nxt: crnt if crnt > nxt else nxt, a)
print(maxofvalues)
print(max(a))


#finding the min_value in list without and with using the min function
minofvalues = reduce(lambda crnt, nxt: crnt if crnt < nxt else nxt, a)
print(minofvalues)
print(min(a))




listofTuples = [('RD44', None), ('RF_44', None), ('RD44', None), ('RF_44', None), ('RF_44', None), ('RD44', None), ('RD44', None), ('RF_44', None), ('RD44', None), ('RD44', None), ('RD44', None), ('RD44', None), ('RF_44', None), ('RD44', None), ('RD44', None), ('RF_44', None), ('RF_44', None), ('RF_44', None), ('RD44', None), ('RF_44', None)]

seperated1 = list(map(lambda x: x[0], listofTuples))
seperated2 = list(map(lambda x: x[1], listofTuples))
print(seperated1)
print(seperated2)
