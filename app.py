from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test_template():
    
    context = {
        'first':'Yeehaaa'
    }

    return render_template('test/index.html', context=context)


@app.route('/game/<int:score>')
def game(score):
   return render_template('test/int.html', score = score)



# flask run --reload