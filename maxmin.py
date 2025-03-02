

def high_and_low(arraystr):
    # split input by commas
    try:
        numbers = [int(n) for n in arraystr.replace('[', '').replace(']', '').split(
            ",")]
    except:
        raise Exception("Incorrect input")
    highlow = [numbers[0], numbers[0]]
    # run through array and record highest and lowest numbers
    for number in numbers:
        if number < highlow[0]:
            highlow[0] = number
        elif number > highlow[1]:
            highlow[1] = number
    return highlow


print(high_and_low(input("Please input a list of numbers: ")))
