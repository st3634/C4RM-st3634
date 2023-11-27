

def getBondPrice_Z(face, couponRate, times, yc):
    pv = 0
    
    for i in range(1, len(times) + 1):
        pv += 1 / ((1 + yc[i - 1]) ** times[i-1])
    
    bondPriceZ = (pv * couponRate + 1 / ((1 + yc[-1]) ** times[-1])) * face
    bondPriceZ = round(bondPriceZ)
    return (bondPriceZ)
    #return(1996533)