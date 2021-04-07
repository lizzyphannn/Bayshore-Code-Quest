is_dog = False
is_pretty = False

if is_dog and is_pretty:
    print("It is a pretty dog.")
elif is_dog and not(is_pretty):
    print("It is not a pretty dog.")
elif not(is_dog) and is_pretty:
    print("It is not a dog but it is pretty.")
else:
    print("It is not a pretty creature.")