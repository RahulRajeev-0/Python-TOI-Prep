# use decorator to prevent zero divsion error 


def dec(func):
    def wrapper(a, b):
        if b == 0 :
            return "not posible "
        func(a, b)
    return wrapper

@dec
def div(a, b):
    return a / b

print(div(1,0))