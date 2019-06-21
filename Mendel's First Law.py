from scipy.special import comb

def dominateProb(k, m, n):
    totalPop = k + m + n
    totalgenes = comb(totalPop, 2)
    domgenes = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    domprob = domgenes/totalgenes
    print(domprob)

dominateProb(19, 23 ,17)
