

def check_str_length(value, permitted_length):
    value_length = len(value)
    if value_length > 0 and value_length <= permitted_length:
        return True
    else:
        return False
        