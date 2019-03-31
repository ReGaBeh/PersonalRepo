import personmod as pm

p1 = pm.Adult("Jerry", 34, "M")
print(p1.name, "is_alive =", bool(p1.status()))
p1.birth("James", "M")
p1.kill()
print(p1.name, "is_alive =", bool(p1.status()))

p2 = pm.Child("Bob", 4, "M")
print(p2.name)
p2.graduate()
print(p2.name, p2.age, p2.gender)

p3 = pm.Adult("Rachel", 27, "F")
print(p3.name, p3.age, p3.title)
p3.employ()
print(p3.name, "is", p3.job)

p4 = p3.birth("Zoe", "F")

p5 = pm.Child("Jaco", 18, "M")
p5.graduate()
print(p5.title)
p5.all_data()

p6 = pm.Adult("Chloe", 22, "F")
p6.marriage(p3)
print(p6.name, "is married to", p6.mpartner.name)
print(p3.name, "is married to ", p3.mpartner.name)
print(p6.married, p3.married)

p3.marriage(p1)
p3.divorce(p6)
print(p3.married, p3.mpartner)
print(p6.married, p6.mpartner)
