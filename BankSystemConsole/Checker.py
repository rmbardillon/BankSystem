def pin_validator(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        except ValueError:
            print("Numbers only!")
    return answer


def float_validator(prompt):
    while True:
        try:
            answer = float(input(prompt))
            break
        except ValueError:
            print("Numbers only!")
    return answer
