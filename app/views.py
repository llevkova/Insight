from flask import render_template, request
from app import app
from LR_Model import Model_LR

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/input')
def wine_input():
  return render_template("input.html")

@app.route('/output')
def wine_output():
    al = request.args.get('AL')
    va = request.args.get('VA')
    sph = request.args.get('SPH')
    tsd = request.args.get('TSD')
    if is_number(al):
        al=float(al)
    else: al= -1
    if is_number(va):
        va=float(va)
    else: va= -1
    if is_number(sph):
        sph=float(sph)
    else: sph= -1
    if is_number(tsd):
        tsd=float(tsd)
    else: tsd= -1


    taste, r_g,r_al1,r_al2,r_al3,r_va1,r_va2,r_va3, r_sph, r_tsd  = Model_LR(al,va,sph,tsd)
    return render_template("output.html", taste = taste, r_g=r_g, r_al1=\
            r_al1,r_al2=r_al2,r_al3=r_al3, r_va1=r_va1,r_va2=r_va2,r_va3=r_va3, r_sph=r_sph, r_tsd=r_tsd)
