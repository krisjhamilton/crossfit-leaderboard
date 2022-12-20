# from flask import appcontext_popped
from flask import Flask, request, render_template
import sqlite3

conn = sqlite3.connect('database.db')
# print "Opened database successfully";

conn.execute('CREATE TABLE athletes (name TEXT, age TEXT, division TEXT)')
# print "Table created successfully";
conn.close()

app = Flask(__name__)

@app.route('/enternew')
def new_student():
    return render_template('athlete.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            age = request.form['age']
            division = request.form['division']
            
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO athletes (name,age,division) VALUES (?,?,?)",(nm,age,division) )
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from athletes")
    
    rows = cur.fetchall(); 
    return render_template("list.html",rows = rows)





@app.route('/')
def hello():
    return ("Hello")

# @app.route('/form_submission', methods=['POST'])
# def form_submission():
#     form_name = request.form['input_name']
#     form_workout = request.form['input_workout']
#     form_score = request.form['input_score']
#     # process form_input and return a response
#     return 'Form input received: {} - {} - {}'.format(form_name,form_workout,form_score)

# @app.route('/form')
# def form():
#     return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)