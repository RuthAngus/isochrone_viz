from iso_age import iso_age
from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc-age', methods=["POST"])
def calc_age():
    teff = request.form["teff"]
    logg = request.form["logg"]
    feh = request.form["feh"]
    # age = calc_age(request.form["teff"])
    return "{0}, {1}, {2}".format(teff, logg, feh)

# @app.route('/calc_age.py', methods=['POST'])
# def index():
#     print(request.form['projectFilepath'])
#     test = request.form['projectFilepath']
#     # age_text = calc_age()
#     age_text = test
#     return render_template('index.html', age_text=age_text)


# @app.route('/calc_age.py', methods=['POST'])
# def index():
#     print("I got it!")
#     print(request.form['projectFilepath'])
#     return render_template('index.html')


# @app.route('/image/<figname>')
# def image("trilegal_period_hist-80.pdf"):
#     return make_plot(figname)

if __name__ == '__main__':
    app.run(debug=True)
