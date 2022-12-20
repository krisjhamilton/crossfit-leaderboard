from flask import appcontext_popped
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return ("Hello")

@app.route('/form_submission', methods=['POST'])
def form_submission():
    form_input = request.form['input_name']
    # process form_input and return a response
    return 'Form input received: {}'.format(form_input)

@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()