def bin2dec():
    output_decimal = 0
    while True:
        input_string_bin = input('Enter binary number:')
        is_valid_input = True

        # print(f"first: {is_valid_input}")
        for s in input_string_bin:
            if s != '0' and s != '1':
                is_valid_input = False

        # print(f"second: {is_valid_input}")
        if not is_valid_input:
            # print("Enter a valid binary number")
            continue

        break

    for place in range(0, len(input_string_bin)):
        power = len(input_string_bin) - place - 1
        output_decimal += int(input_string_bin[place]) * pow(2, power)
    return output_decimal


print(bin2dec())






