
def getBondDuration(y, face, couponRate, m, ppy = 1):
    c = couponRate / ppy
    cf = c * face
    periods = m * ppy
    r = y / ppy
    rate = 0
    pvcf = 0
    bondPrice = 0
    bondDuration = 0
    
    for i in range(1, periods + 1):
        rate += (1+r)**(-i)
        pvcf += (((1+r)**(-i)) * cf) * i
    bondPrice += ((rate * c) + ((1+r) ** (-periods))) * face
    bondDuration += (pvcf + (((1+r) ** (-periods)) * face * periods))/bondPrice
    return(round(bondDuration,2))
    #return(8.51)