import NameGenerator
name=NameGenerator

for i in range(10):
    male = name.male()
    female = name.female()
    rand = name.rnd()
    print(male,"*****",female,"******",rand)
