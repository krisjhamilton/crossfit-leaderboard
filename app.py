from flask import appcontext_popped
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return ("Hello")

@app.route('/form_submission', methods=['POST'])
def form_submission():
    form_name = request.form['input_name']
    form_workout = request.form['input_workout']
    form_score = request.form['input_score']
    # process form_input and return a response
    return 'Form input received: {}'.format(form_name,form_workout,form_score)

@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()