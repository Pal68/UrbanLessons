first=int(input("Ведите первое число:"))
second=int(input("Ведите второе число:"))
third=int(input("Ведите третье число:"))
print(first)
print(second)
print(third)
if first==second and second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)
