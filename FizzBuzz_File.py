

def FizzBuzz(start, finish):
    outlist = []
    for i in range(start,finish+1):
        if i % 3 == 0 and i % 5 == 0:
            i = "fizzbuzz"
        elif i % 3 == 0:
            i = "fizz"
        elif i % 5 == 0:
            i = "buzz"
        outlist.append(i)
    return(outlist)

    #v = ['buzz', 41, 'fizz', 43, 44, 'fizzbuzz']
    #return(v)