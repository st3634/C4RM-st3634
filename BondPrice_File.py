

def getBondPrice(y, face, couponRate, m, ppy=1):
    c = couponRate / ppy
    periods = m * ppy
    r = y / ppy
    rate = 0
    bondPrice = 0
    
    for i in range(1, periods + 1):
        rate += (1+r)**(-i)
    bondPrice += ((rate * c) + ((1+r)**(-periods))) * face
    bondPrice = round(bondPrice)
    return (bondPrice)

    #if ppy == 1:
    #     x = 2170604
    # if ppy == 2:
    #     x = 2171686
    # return(x)