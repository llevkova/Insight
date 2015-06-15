import math
def normalize(val, mean, sd):
    val_n = (val-mean)/sd
    return val_n

def Model_LR(al=0,va=0,sph=0,tsd=0):
    al_av = 10.42298
    al_sd = 1.065668
    al_n = normalize(al, al_av, al_sd)
    va_n = (va - 0.5278205)/0.1790597
    sph_n =(sph - 0.6581488)/0.169507
    tsd_n =(tsd - 46.46779)/32.89532

    taste = round(5.63602 + 0.31470*al_n -0.21461*va_n + 0.12071*sph_n - 0.07353*tsd_n,1)
    return taste

def cdf(taste):
    taste_n = normalize(taste, 5.636023, 0.8075694)
    val = int(round(100*(1 + math.erf(taste_n/2**0.5))/2.0))
    return val
