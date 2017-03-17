def validate_list_of_numeric_arg(arg_list, command_length, num_boxes):
    if len(arg_list) != command_length:
        raise Exception

    for elem in arg_list:
        validate_numeric_arg(elem, num_boxes)


def validate_numeric_arg(num, num_possible):
    try:
        num = int(num)
    except:
        raise Exception

    if num <= 0:
        raise Exception

    if num_possible != None and num > num_possible:
        raise Exception
