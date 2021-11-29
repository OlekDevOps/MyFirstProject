
age = 155
if   (age <=4):
    print("You are too little")
elif (age > 4) and (age < 12):
    print("You are young")
elif (age >=12) and (age <= 19):
    print("You are teanager")
else:
    print("You are old")
print("end==============================")


sity = ['Debica', 'kiev', 'Gdansk', 'odessa', 'lvov', 'Lodz', 'rovno', 'Piotrkow', 'lugansk', 'frankovsk', 'Dzialoszin']
polandsity = ['Gdansk', 'Lodz', 'Debica', 'Piotrkow', 'Dzialoszin']
for xxx in sity:
    if xxx in polandsity:
        print("Polskie miasto " + xxx)
    else:
        print("Ukrainskie miasto " + xxx.title())
