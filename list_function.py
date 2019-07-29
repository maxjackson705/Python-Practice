li = [10, 20, 30]
l = [5, 8, 9, 12.10]

print(li)

li.append(70)
print(li)

li.insert(2, 25)
print(li)

li.extend(l)
print(l)

new_li = list.copy(li)
print(new_li)

cnt = li.count(10)
print("No. of 10s: ", cnt)

print("Index of '9': ", li.index(9))

li.pop(4)
print(li)

li.remove(10)
print(li)

li.reverse()
print(li)

li.sort()
print(li)
