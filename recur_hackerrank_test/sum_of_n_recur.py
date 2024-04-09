def sum_of_n(st, ed):
    if st >= ed:
        return st
    print("\n", st)
    return st + sum_of_n(st+1, ed)


start = int(input("Enter the starting point : "))
end = int(input("Enter the ending point : "))

print(sum_of_n(start, end))
