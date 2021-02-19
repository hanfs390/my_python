def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0:
        print 'Need a unsigned int'
        exit(0)
    elif n in [1]:
        print '{}'.format(n)
    while n not in[1]:
        for index in xrange(2, n + 1):
            if n % index == 0:
                n /= index
                if n == 1:
                    print index
                else:
                    print '{} *'.format(index),
                break
reduceNum(90)
reduceNum(900)
reduceNum(1)
