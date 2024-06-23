from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def feedback():
    return render_template('feedback.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/reg')
def reg():
    return render_template('Resignation.html')
@app.route('/Product')
def Product():
    return render_template('Product.html')
@app.route('/admindashboard')
def admindashboard():
    return render_template('admindashboard.html')
@app.route('/payment')
def Payment():
    return render_template('payment.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
@app.route('/web')
def web():
    return render_template('web.html')
@app.route('/Adminlogin')
def Adminlogin():
    return render_template('Admin_login.html')
app.run(debug=True)