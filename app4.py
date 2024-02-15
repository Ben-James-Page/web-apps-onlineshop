from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "top secret password, keep private!"

products = [
    { "name": "Strip Weathers", "price": "£43.00", "description": "\"The Legend\"", "image": "/static/StripWeathers.png", "link": "/prod/0" },
    { "name": "Chic Hicks", "price": "£86.00", "description": "\"The Runner Up\"", "image": "/static/ChickHicks.png", "link": "/prod/1" }, 
    { "name": "Lightning Mcqueen", "price": "£95.00", "description": "\"The Rookie\"", "image": "/static/LightningMcqueen.png", "link": "/prod/2" },
]

class OpinionForm(FlaskForm):
    opinion = StringField('Your Feedback: ',validators = [DataRequired(), Length(min=0,max=100)]) #makes you input something, makes max characters 100
    submit = SubmitField('Submit')
    
class AddToBasketForm(FlaskForm):
    quantity = StringField('Quantity: ', validators = [DataRequired()])
    addToBasket = SubmitField('Add to Basket')

@app.route('/')
def galleryPage():
    return render_template('index.html',products = products)

@app.route('/prod/<int:prodId>',methods=['GET', 'POST'])
def singleProductPage(prodId):
    form = OpinionForm()
    form2 = AddToBasketForm()
    
    if form.validate_on_submit():
        return render_template('SingleProdOpinion.html', product = products[prodId], opinion = form.opinion.data)
    elif form2.validate_on_submit():
        return render_template('basket.html', product = products[prodId], quantity = form2.quantity.data)
    else:
        return render_template('SingleProd.html', product = products[prodId], form2 = form2, form = form)
    
    #HEYHEY
    

if __name__ == '__main__':
    app.run(debug=True) 
    
