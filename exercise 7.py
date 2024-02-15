def even_odd(no):
    return no/2

ans = even_odd(int(input("no: ")))

if ans%2 == 0:
    print("even")
elif ans != 0:
    print("odd")
