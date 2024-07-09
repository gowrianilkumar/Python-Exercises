def print_number_pattern(row_count):
    for i in range(1, row_count + 1):
        for j in range(row_count + 1 - i):
            print(i, end=' ')
        print()


row_count = 5
print_number_pattern(row_count)
