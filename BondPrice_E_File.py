

def getBondPrice_E(face, couponRate, yc):
    pv = 0
    
    for i in range(1, len(yc) + 1):
        pv += 1 / ((1 + yc[i - 1]) ** i)
    
    bondPriceE = (pv * couponRate + 1 / ((1 + yc[-1]) ** len(yc))) * face
    bondPriceE = round(bondPriceE)
    return (bondPriceE)
    #return(2098949)
