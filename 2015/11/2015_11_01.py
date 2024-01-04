# Advent of Code 2015, 11: Corporate Policy. Part 1
# https://adventofcode.com/2015/day/11


def increment_password(password) -> str:
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == "z":
            password[i] = "a"
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return password


def password_is_ok(password) -> bool:
    if "i" in password or "o" in password or "l" in password:
        return False
    # ...
    return


def main():
    solution = ""

    input = open("./2015/10/2015_11.txt", "r", encoding="utf-8").readline().strip()


    return f"The new password is {solution}."


if __name__ == "__main__":
    print(main())
