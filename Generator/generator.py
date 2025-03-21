def generator():
    for i in range(10):
        yield i

for i in generator():
    print(i)
