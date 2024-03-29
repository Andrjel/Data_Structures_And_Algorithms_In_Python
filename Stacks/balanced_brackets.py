from init import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "[" and p2 == "]":
        return True
    if p1 == "{" and p2 == "}":
        return True
    return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    return False


def main():
    print("String : (((({})))) Balanced or not?")
    print(is_paren_balanced("(((({}))))"))

    print("String : [][]]] Balanced or not?")
    print(is_paren_balanced("[][]]]"))

    print("String : [][] Balanced or not?")
    print(is_paren_balanced("[][]"))


if __name__ == "__main__":
    main()
