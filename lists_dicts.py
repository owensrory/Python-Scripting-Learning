# Tuples
point = (2.0, 3.0)
point_3d = point + (4.0,)
print(point_3d)
x, y, z = point_3d
print(x)
print(y)
print(z)
print("My name is: %s %s" % ("Rory", "Owens"))

# Dictionaries
ages = {'Rory': 20, 'Sophie': 19, 'Sofie': 23}
print(ages)
print(ages['Rory'])
ages['Susan'] = 52
print(ages)
del ages['Rory']
print(ages)
ages.pop('Sofie')
print(ages)
print(ages.keys())
print(ages.values())
weights = dict(Rory=79, Sophie=50, Sofie=60)
print(weights)
colours = dict([('Rory', 'green'),('Sophie', 'pink'), ('Sofie', 'yellow')])
print(colours)

