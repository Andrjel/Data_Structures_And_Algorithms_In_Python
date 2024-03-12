from init import Stack


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    while dec_num != 0:
        s.push(dec_num % 2)
        dec_num //= 2
    result_bin_number = ""
    while not s.is_empty():
        result_bin_number += str(s.pop())
    return result_bin_number


def main():
    print(convert_int_to_bin(242))


if __name__ == "__main__":
    main()
