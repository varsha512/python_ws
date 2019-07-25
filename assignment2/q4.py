name=input("enter your name:")
lst=['a','e','i','o','u']
print(list(filter(lambda x:x in lst,name)),len(list(filter(lambda x:x in lst,name))))