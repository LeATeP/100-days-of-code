
name1 = input("Write your name: ")
name2 = input("Write your love name: ")
name_total = name1.lower() + name2.lower()


t = name_total.count("t")
r = name_total.count("r")
u = name_total.count("u")
e = name_total.count("e")

true = t + r + u + e

l = name_total.count("l")
o = name_total.count("o")
v = name_total.count("v")

love = l + o + v + e

total_score = int(str(true) + str(love))

print(total_score)
