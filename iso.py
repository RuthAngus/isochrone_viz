from iso_age import iso_age
from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc-age', methods=["POST"])
def calc_age():
    teff = float(request.form["teff"])
    logg = float(request.form["logg"])
    feh = float(request.form["feh"])
    age = iso_age(teff, logg, feh)
    return "Age = {0} Myr".format(age)

# @app.route('/image/<figname>')
# def image("trilegal_period_hist-80.pdf"):
#     return make_plot(figname)

if __name__ == '__main__':
    app.run(debug=True)
