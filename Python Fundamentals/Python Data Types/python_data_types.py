# x = 5
# print(type(x))

# x = {"name" : "Name", "age" : 26}
# name = x["name"]
# age = x["age"]
# print(name)
# print(age)

# print("Setting the Data Type");
x = "Hello World"; print(type(x));
x = 20; print(type(x));
x = 26.5; print(type(x));
x = ["apple", "banana", "cherry"]; print(type(x)); # list
x = ("apple", "banana", "cherry"); print(type(x)); # tuple
x = range(6); print(type(x));
x = {"name" : "John", "age" : 36}; print(type(x)); # dict
x = {"apple", "banana", "cherry"}; print(type(x)); # set
x = frozenset({"apple", "banana", "cherry"}); print(type(x));
x = True; print(type(x));
x = b"Hello"; print(type(x));
x = bytearray(5); print(type(x));
x = memoryview(bytes(5)); print(type(x));
x = None; print(type(x));

print("\n");

# print("Setting the Specific Data Type");
x = str("Hello World"); print(type(x));
x = int(20); print(type(x));
x = float(20.5); print(type(x));
x = complex(1j); print(type(x));
x = list(("apple", "banana", "cherry")); print(type(x));
x = tuple(("apple", "banana", "cherry")); print(type(x));
x = range(6); print(type(x));
x = dict(name="John", age=36); print(type(x));
x = set(("apple", "banana", "cherry")); print(type(x));
x = frozenset(("apple", "banana", "cherry")); print(type(x));
x = bool(5); print(type(x));
x = bytes(5); print(type(x));
x = bytearray(5); print(type(x));
x = memoryview(bytes(5)); print(type(x));