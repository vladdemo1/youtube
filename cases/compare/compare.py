"""Compare objects in Python like 'is' or == """


immutable = ('This tuple immutable', 100,)
repeat = ('This tuple immutable', 100,)

print(f'Id first object in memory : {id(immutable)}')
print(f'Id second object in memory: {id(repeat)}')

print(immutable == repeat, immutable is repeat)
