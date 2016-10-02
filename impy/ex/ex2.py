while True:
    try:
        a = int(raw_input("workhour: "))
        if a <= 40:
            print a*3
        else:
            print 40*3+(a-40)*4.5

        break
    except ValueError:
        print 'numbers only'

