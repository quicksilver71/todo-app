def parse(user_input):
    parts = user_input.split(',')
    lower_bound = int(parts[0])
    upper_bound = int(parts[1])
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}
