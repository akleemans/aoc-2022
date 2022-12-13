import datetime
import timeit

if __name__ == '__main__':
    today = datetime.datetime.now()
    for d in range(1, today.day + 1):
        p = 'day' + str(d).zfill(2)
        t = timeit.timeit('import ' + p + '; ' + p + '.main()', number=1)
        print(p, ':', round(t, 3), 's')
