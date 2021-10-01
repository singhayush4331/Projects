# 1.

def fun(*args):
    for arg in args:
        print(arg)


# fun("Welcome", "to", "Geeks", "for", "Geeks")

# 2.

def yo(first, *args):
    print("My name is :", first)
    for arg in args:
        print("My Friend name is :", arg)


# yo("Ayush", "Srivardhan", "Rishu", "Adii", "Vatsal")

# 3.

def my_fun(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# my_fun(car="BMW", seats=4, owner="Ayush")

# 4.

def yes(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print(f"My {key} is", ":", value)


# yes("Hi", Name="Ayush", Age=16)

