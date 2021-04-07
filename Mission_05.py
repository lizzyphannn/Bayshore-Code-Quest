is_female = True
is_athlete = False

if is_athlete and is_female:
    print("You are a female and an athlete")
elif is_athlete and not(is_female):
    print("You are an athlete but not a female")
elif not(is_athlete) and is_female:
    print("You are a female but not an athlete")
else:
    print("You are not a female nor an athlete")