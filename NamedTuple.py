# •1. NamedTuple called Employee with fields like name, age, and country. Print each employee's name and country.
# •2. NamedTuple called Point with fields x, y and z representing the coordinate of a point. Access and print the fields.
# •3. Create a dictionary where keys are food names and prices are instances of the Food named tuple.
# •4. a NamedTuple called Student with fields like name, age, and marks (a list of subjects and marks).


from collections import namedtuple as nt
e = nt("Employee",['Name','age','country'])
l = e('Amar',21,'India')
l1 = e('Kamal',26,'US')
# print("Names: ",l.Name,l1.Name)
# print("country: ",l.country,l1.country)

Point = nt("Poing",['x','y','z'])
# print(Point._fields)

food = nt("Food",['Name','Price'])
d = {"Chicken":food(Name='Chicken',Price=180),
      "Edli":food(Name='Edli',Price=75),
        "Dosa":food(Name='Dosa',Price=55)}
print(d.values())
