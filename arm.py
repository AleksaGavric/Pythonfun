def arm0():
    count = 0
    for j in range(0, 10):
        e = 10000 * j
        for i in range(0, 10):
            d = 1000 * i
            for x in range(0, 10):
                a = 100 * x
                for y in range(0, 10):
                    b = 10 * y
                    for z in range(0, 10):
                        c = z
                        aps = a + b + c + d + e
                        n = 3
                        bes = x ** n + y ** n + z ** n + i ** n + j ** n
                        if bes == aps and aps != 0 and aps != 1:
                            print("Armstrong number:", bes)
                            count += 1

    print()
    print(count, "Armstrong numbers under 1000!")
arm0()
