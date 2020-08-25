import os
def rename():
    dir = input("Enter The Directory:")
    remove = input("Enter String You Want To Remove:")
    os.chdir(dir)
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_name = f_name.strip(remove)
        newName ='{}{}'.format(f_name, f_ext)
        os.rename(f, newName)
    print("Rename Done")
    ask = input("Do it Again?(y)")
    if ( ask == 'y') | ( ask == 'Y'):
        rename()
    else:
        exit
rename()


