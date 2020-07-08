import os

isblocked = False

blocktext = '# 127.0.0.1 		www.facebook.com'
unblocktext = '127.0.0.1 		www.facebook.com'


path = os.path.abspath("C:/Windows/System32/drivers/etc/hosts")
# print(path)

with open(path, "a+") as f:
    f.seek(0)
    doc = f.read()
    if 'www.facebook.com' not in doc:
        f.write('\n' + blocktext)
    else:
        if blocktext not in doc:
            isblocked = True


def changeblockstatus():
    global isblocked
    with open(path, "a+") as f:
        f.seek(0)
        lines = f.readlines()
        for c, line in enumerate(lines):
            if 'facebook' in line:
                if isblocked:
                    lines[c] = blocktext
                    isblocked = False
                    print('\nFacebook is now unblocked')
                else:
                    lines[c] = unblocktext
                    isblocked = True
                    print('\nFacebook is now blocked')

    with open(path, "w") as f:
        f.writelines(lines)


print('Welcome to the Facebook disabling tool!')
print()
print()
if isblocked:
    print('Facebook is currently blocked')
else:
    print("Facebook is NOT currently blocked")
print()

while 1 > 0:
    print()
    print("""
    ------Options------
    1. Block/Unblock Facebook (y/n)
    2. Quit
    3. (more features tbd)
    """)
    print()
    choice = input(': ')
    if choice == '1':
        changeblockstatus()
    elif choice == '2':
        input('Press any key to exit:')
        quit()
    else:
        print('invalid input, please choose one of the listed menu options')