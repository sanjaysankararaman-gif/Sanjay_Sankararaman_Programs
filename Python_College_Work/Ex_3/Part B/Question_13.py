def count_occurences(traget_rating, *ratings):
    count = 0
    for i in ratings:
        if i == traget_rating:
            count += 1
        else:
            continue
    return count
