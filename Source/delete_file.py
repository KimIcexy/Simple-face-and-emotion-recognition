"""Kết hợp với ứng dụng Delete Duplicate Image để xóa các file trùng lặp bằng cách nhập filepath"""

import os


def wait_for_input():
    inputs = []
    while True:
        user_input = input("Nhập path (nhấn Enter để kết thúc): ")
        if user_input == "":
            break
        inputs.append(user_input)

    return inputs


def remove(inputs):
    for file in inputs:
        try:
            os.remove(file)
        except:
            print('can not remove ' + file)


def main():
    remove(wait_for_input())


if __name__ == "__main__":
    main()
