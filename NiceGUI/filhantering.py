konversation = []
i = 0
print("pick document")
document = input()
print("what person do you want to hear?")
name = input()
f = open(document), "r"
for x in f:
  print(x)
  i = x.count(name + ":", 0, 1)
  konversation.append(i)
f.close

f = open("en_sida", "a")
for y in konversation:
  f.write(y)

f.write()
f.close()