from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod' # development environment

if ENV == 'dev':
    app.debug = True
    # putting development database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Gaurav123@localhost/lexus'
else:
    app.debug = False 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jpozangmelgrtj:1b0db3280f8b3833cdccf05e83f36b49858c71a44ea379d4748bb6e6698dcbde@ec2-34-224-226-38.compute-1.amazonaws.com:5432/dbf0isje5pbdj2'  

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Database Object(used to query the database)
db = SQLAlchemy(app)

# create feedback class
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

# Route to index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to submit
@app.route('/submit', methods = ['POST'])
def submit():
    # Request is a post request from Form
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        #print(customer, dealer, rating, comments)
        if customer == ' 'or dealer == ' ':
            return render_template('index.html', message='Please enter required fields')

        # Check customer is already in database or not if not then add
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data) # add the data
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        # else render to index page    
        return render_template('index.html', message='You have already submitted')     


if __name__ == '__main__':
    app.run()