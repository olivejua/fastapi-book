def doh():
    yield "Homer: D'oh!"
    yield "Lisa: A deer!",
    yield "Merge: A female deer!"

for line in doh():
    print(line)
