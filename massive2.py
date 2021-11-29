#          0      1       2       3      4
cars = ['honda','bmw','ferari','kamaz','opel']
print(cars)
for x in cars:
    print(x.upper())
for x in range (1,6):
    print(x)

my_list = list(range(0,10))
print(my_list)
print("=========================================")
for x in my_list:
    x = x*3
    print(x)

my_list.sort(reverse=True)
print(my_list)

print("Max number is:" + str(max(my_list)))
print("Min number is:" + str(min(my_list)))
print("Sum list is:" + str(sum(my_list)))
#==================================================
print("=========================================")
mycars = cars [1:4]
print(mycars)

