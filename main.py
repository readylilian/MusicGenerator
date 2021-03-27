# This is a sample Python script.
'''import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'hi, ' + name


def main():
    # var = input("hello")
    # print_hi(var)
    # hiSutay()
    find_file()


def hi_sutay():
    long_string = "fajksdhfjkaslkfjaslkjsflkajsflkasjflkjaslkfjaskljflkasjflkassflasjflkajlkasjlkdjalkdaslsdlasd"
    short_string = long_string[7:13]
    print(short_string[::-1])
    yeet = 'yea'

    if yeet == 'yea':
        print('of course')


def find_file():
    files = os.listdir()
    for pos_file in files:
        if '.txt' in pos_file:
            txt_file = open(pos_file, 'r')
            count = 0
            for line in txt_file:
                count += 1
                print(f'{count}: {line.strip()}')
            return 'hi'


CMDs = dict()
CMDs[1] = find_file()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    print_hi('PyCharm')
'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
