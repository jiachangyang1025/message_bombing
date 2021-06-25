import time

from pynput.keyboard import Key, Controller

def input(content):
    keyboard = Controller()
    keyboard.type(content)
    keyboard.press(Key.enter)


def main(number, content):
    time.sleep(5)
    print("start bombing...")
    for i in range(number):
        input(content)
        time.sleep(0.5)


main(10, "还钱还钱还钱！！！")

