import math
def normalize(val, mean, sd):
    val_n = (val-mean)/sd
    return val_n

def isinrange(a,b,c):
    if a >= b and a<=c:
        return True
    else:
        return False

def cdf(taste, taste_av, taste_sd):
    taste_n = normalize(taste, taste_av, taste_sd)
    val = int(round(100*(1 + math.erf(taste_n/2**0.5))/2.0))
    return val

def Model_LR(al=0,va=0,sph=0,tsd=0):
    if isinrange(al,7,16) and isinrange(va,0,2) and isinrange(sph,0,2) and isinrange(tsd,0,300):
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
        taste_raw = taste_av + al_c*al_n +va_c*va_n + sph_c*sph_n + tsd_c*tsd_n
        taste = cdf(taste_raw,taste_av,taste_sd)

#alcohol
        recommend_al = r_al1 = r_al2 = ""
        if(al_n<=-1):
            taste_raw = taste_raw + al_c*3/al_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_al = "Your wine's alcohol content is too low. To create a competitive product, we \
                recommend that you increase the alcohol content by at least 3 percentage\
                points. This will make your wine taste better than "
            r_al1 = str(taste_imp)+"% "
            r_al2 = "of wines. "
        elif(al_n<=0):
            taste_raw = taste_raw + al_c*2/al_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_al = "If you increase the alcohol content by 2\
                percentage points, your wine will taste better than "
            r_al1 = str(taste_imp)+"% "
            r_al2 = "of wines. "
        elif(al_n<=1):
            taste_raw = taste_raw + al_c*1.5/al_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_al = "If you increase the alcohol content by 1.5\
                percentage points, your wine will taste better than "
            r_al1 = str(taste_imp)+"% "
            r_al2 = "of wines. "
        elif(al_n<=2):
            taste_raw = taste_raw + al_c*1/al_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_al = "If you increase the alcohol content by 1\
                percentage point, your wine will taste better than "
            r_al1 = str(taste_imp)+"% "
            r_al2 = "of wines. "
        else:
            taste_imp = taste_raw
            recommend_al = "Your wine is sufficiently high in alcohol. Well done!"

#volatile acidity
        recommend_va = r_va1=r_va2=""
        if(va_n>=2):
            taste_raw = taste_raw - va_c*0.6/va_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_va = "The volatile acidity (vinegar) content of your wine is too high.\
                If you decrease it by at least 0.6 g/l, \
                your wine will further achieve a rating better than "
            r_va1 = str(taste_imp)+"% "
            r_va2 = "of wines. "
        elif(va_n>=0):
            taste_raw = taste_raw - va_c*0.4/va_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_va = "If you decrease further the volatile acidity (vinegar) content by\
                0.4 g/l, your wine will achieve a ratting\
                better than "
            r_va1 =  str(taste_imp)+ "% "
            r_va2 =  "of wines. "
        elif(va_n>=-1):
            taste_raw = taste_raw - va_c*0.3/va_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_va = "Your wine will benefit by an additional decrease in volatile acidity\
                (vinegar) by 0.3 g/l.\
                This will make it taste better than "
            r_va1 = str(taste_imp) + "% "
            r_va2 =  "of wines. "
        elif(va_n>=-2):
            taste_raw = taste_raw - va_c*0.15/va_sd
            taste_imp = cdf(taste_raw,taste_av,taste_sd)
            recommend_va = "If you additionally decrease the volatile acidity (vinegar) by 0.15 g/l,\
                 the rating of you wine will be better than "
            r_va1 = str(taste_imp)+"% "
            r_va2 = "of wines. "
        else:
            recommend_va = "Your wine is low in volatile acidity (vinegar). Good job!"
#taste
        if(taste>=85):
            recommend_g = "Congratulations! Your wine has an excellent taste. Your best strategy is to\
                invest in the marketing of your product. "
        elif(taste>=75):
            recommend_g = "Great job! Your wine tastes very good. "
        elif(taste>=60):
            recommend_g = "You are almost there! Your wine tastes better than average. "
        else:
            recommend_g = "Your wine needs work. "
#sulphates
        if sph > 0.35:
            recommend_sph = "The sulfate content of your wine is higher than the legal limit of 0.35 g/l."
        elif sph < 0.1:
            recommend_sph = "You may want to increase the sulfate content up to 0.1 g/l."
        else:
            recommend_sph = "The sulfate content of your wine is acceptable."
#total sulfur dioxide
        if tsd < 110:
            recommend_tsd = "The total sulfur dioxide content of your wine is acceptable."
        else:
            recommend_tsd = "Consult the resources below on how to bring the total sulfur dioxide below 110 mg/l."
        return (taste, recommend_g, recommend_al,r_al1,r_al2, recommend_va,r_va1,r_va2,\
                recommend_sph, recommend_tsd)
    else:
        taste = "??"
        recommend_g = "The taste cannot be determined. Check if your input values are\
                within the required ranges below. Do not enter units or % signs."
        recommend_al = "Alcohol: 7-16%."
        recommend_va = "Volatile acidity: 0-2 g/l."
        recommend_sph = "Sulfates: 0-2 g/l."
        recommend_tsd = "Total sulfur dioxide: 0-300 mg/l."
        r_al1=r_al2= " "
        r_va1=r_va2= " "
        return (taste, recommend_g, recommend_al, r_al1, r_al2, recommend_va, r_va1,r_va2,\
                recommend_sph, recommend_tsd)

