# nonlocal allows us to modify a parent variable or resuse a parent variable without creating a new one

def outer():
    x = "local var"

    def inner():
        nonlocal x
        x = 'inner var'
        print("inner: ", x)
    inner()
    print("outer: ", x)


print(outer())
