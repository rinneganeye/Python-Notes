# <------------------------------------Dictionary------------------------------------>
# Dictionary stores data in key value pair format. The value can be duplicate but the key should always be unique.
dictionary = {
    "name": "Amey",
    "age": 21,
    "disabled": False,
}

print(dictionary)

# <------------------------------------Accessing Dictionary element------------------------------------>

# SYNTAX: dictionary["key" ]
print(dictionary["age"])

# <------------------------------------Dictionary Methods------------------------------------>

print(dictionary.keys())  # Prints dictionary keys in array format

print(dictionary.values())  # Prints dictionary values in array format

print(dictionary.get("name"))  # This will print the value with specified key
# NOTE: The difference between dictionary["key"] and dictionary.get() method is that,
# if we pass invalid key to dictionary.get() method, it will return 'none' while dictionary["key"] will throw error

dictionary.pop("age")  # This will remove element from dictionary

dictionary.clear()  # Clears the dictionary

dictionary.popitem()  # This will remove the last element from dictionary

dictionary.update(
    {"last": "Shinde"}
)  # This will add the new element to the end of the dictionary


# <------------------------------------Nested Dictionary------------------------------------>
nestedDictionary = {"profile": {"name": "Isha", "age": 21}}


# <------------------------------------Accessing Nested Dictionary------------------------------------>
# SYNTAX: dictionary['key1']['key2']

print(nestedDictionary["profile"]["name"])
