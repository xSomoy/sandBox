is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You Are a short male")
elif not(is_male) and is_tall:
    print("You Are a Tall Female")
else:
    print("You are neither not male or tall")
