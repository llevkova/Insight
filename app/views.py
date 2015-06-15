from flask import render_template, request
from app import app
from LR_Model import Model_LR, cdf


@app.route('/input')
def wine_input():
  return render_template("input.html")

@app.route('/output')
def wine_output():
    al = float(request.args.get('AL'))
    va = float(request.args.get('VA'))
    sph = float(request.args.get('SPH'))
    tsd = float(request.args.get('TSD'))

    taste = Model_LR(al,va,sph,tsd)
    CDF = cdf(taste)
    return render_template("output.html", taste=taste, CDF = CDF)
