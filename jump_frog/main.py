# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def frog_jump(step, i=1):
    """" Find number way frog can jump with given N steps and frog can jump either1step or 2 step at a time """
    height = step - i
    if height > 0:
        return frog_jump(step, i + 1) + frog_jump(step, i + 2)
    else:
        if not height:
            return 1
        else:
            return 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Jump Frog, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    step = 5
    ret = frog_jump(step)

    print("No. of ways frog can reach to top:", ret)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Algo ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
