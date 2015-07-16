#from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import rpy2.robjects as ro
import pandas.rpy.common as com
import math

def normalize(val, mean, sd):
    val_n = (val-mean)/sd
    return val_n

def cdf(taste, taste_av, taste_sd):
    taste_n = normalize(taste, taste_av, taste_sd)
    val = int(round(100*(1 + math.erf(taste_n/2**0.5))/2.0))
    return val

def Model_RF(al,va,sph,tsd):
    ro.r('load("RF.rda")')
    d = {'alcohol':al,'sulphates':sph,'total.sulfur.dioxide':tsd,'volatile.acidity':va}
    dataf = pd.DataFrame(data=d, index=['1'])
    rdf = com.convert_to_r_dataframe(dataf)
    ro.globalenv['mydata'] = rdf
    ro.r('library(randomForest)')
    p={}
    p=str(ro.r('predict(reg,newdata=mydata,type="class")'))
    taste_raw=p.split()
    return int(taste_raw[1])

def rec(al,va,sph,tsd):
    al_av = 10.42298
    al_sd = 1.065668
    al_n = normalize(al, al_av, al_sd)
    al_c = 0.31470;

    va_av = 0.5278205
    va_sd = 0.179059
    va_n =  normalize(va, va_av, va_sd)
    va_c = -0.21461

    sph_av = 0.6581488
    sph_sd = 0.169507
    sph_n = normalize(sph,sph_av,sph_sd)
    sph_c = 0.12071

    tsd_av = 46.46779
    tsd_sd = 32.89532
    tsd_n = normalize(tsd,tsd_av,tsd_sd)
    tsd_c = -0.07353

    taste_av = 5.636023
    taste_sd = 0.8075694
    taste_raw = Model_RF(al_n, va_n, sph_n, tsd_n)
    taste = cdf(taste_raw,taste_av,taste_sd)

    recommend = "A"
    return (taste, recommend)

if __name__=="__main__":
    print(rec(15,0.8,0.3,0))

'''
#alcohol
    if(al_n<=-al_sd):
        taste_raw = Model_RF(al_n+3/al_sd, va_n, sph_n, tsd_n)
        taste_imp = cdf(taste_raw,taste_av,taste_sd)
        recommend = "Your alcohol content is too low. To create a competitive product, we \
                recommend that you increase the alcohol content by at least 3 percentage\
                points. This will bring the rating of your wine to "
        recommend = recommend + str(taste_imp)+". "
    elif(al_n<=0):
        taste_raw = Model_RF(al_n+2/al_sd, va_n, sph_n, tsd_n)
        taste_imp = cdf(taste_raw,taste_av,taste_sd)
        recommend = recommend + "If you increase the alcohol content by 2\
                percentage points, your wine will taste like "
        recommend = recommend + str(taste_imp)+". "
    elif(al_n<=al_sd):
        taste_raw =  Model_RF(al_n+1.5/al_sd, va_n, sph_n, tsd_n)
        taste_imp = cdf(taste_raw,taste_av,taste_sd)
        recommend = recommend + "If you increase the alcohol content by 1.5\
                percentage points, your wine will taste like "
        recommend = recommend + str(taste_imp)+". "
    elif(al_n<=2*al_sd):
        taste_raw = Model_RF(al_n+1/as_sd, va_n, sph_n, tsd_n)
        taste_imp = cdf(taste_raw,taste_av,taste_sd)
        recommend = recommend + "If you increase the alcohol content by 1\
                percentage point, your wine will taste like "
        recommend = recommend + str(taste_imp)+". "
    else: taste_imp = taste_raw



    if(taste>=90):
        recommend = "Great job! Your wine has excellent taste. Your best strategy is to\
                invest in the marketing of your product. " + recommend
    elif(taste>=80):
        recommend = "Well done! Your wine tastes very good. " + recommend
    elif(taste>=60):
        recommend = "You are almost there! Your wine tastes better than average. " + recommend
    else:
        recommend = "Your wine needs work. " + recommend

    return (taste, recommend)
'''


