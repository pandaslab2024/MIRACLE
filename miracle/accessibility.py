def calculate_accessibility(access_list, start, length):
    return sum(access_list[start:start+length]) / length