def count_by_extension(paths):
    totals = {}
    for line in paths:
        line = line.split('.')
        if len(line) < 2:
            key = ''
        else:
            key = line[-1].lower()
        totals[key] = totals.get(key, 0) + 1
    return totals
