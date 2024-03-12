from init import Stack


def reverse_string(input_string):
    s = Stack()
    reversed_string = ""
    for char in input_string:
        s.push(char)
    while not s.is_empty():
        reversed_string += s.pop()
    return reversed_string


def main():
    input_str = "!evitacudE ot emocleW"
    print(reverse_string(input_str))


if __name__ == "__main__":
    main()
