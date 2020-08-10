def lazy_range(upto):
    index = 0
    while index < upto:
        yield index
        index = index + 1
lazy_range(1000)