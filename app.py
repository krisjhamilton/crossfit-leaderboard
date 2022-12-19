import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('leaderboard.db')

@app.route('/')
def leaderboard():
  # Get the list of athletes from the database
  athletes = get_athletes_from_database(conn)
  # Get the list of workouts from the database
  workouts = get_workouts_from_database(conn)
  return render_template('leaderboard.html', athletes=athletes, workouts=workouts)

@app.route('/add_athlete', methods=['POST'])
def add_athlete():
  # Get the form data from the request
  name = request.form['name']
  age = request.form['age']
  # Add the athlete to the database
  add_athlete_to_database(conn, name, age)
  return redirect('/')

@app.route('/add_score', methods=['POST'])
def add_score():
  # Get the form data from the request
  athlete_id = request.form['athlete_id']
  workout_id = request.form['workout_id']
  score = request.form['score']
  # Add the score to the database
  add_score_to_database(conn, athlete_id, workout_id, score)
  return redirect('/')


def get_athletes_from_database(conn):
  cur = conn.cursor()
  cur.execute('SELECT * FROM athletes')
  return cur.fetchall()

def add_athlete_to_database(conn, name, age):
  cur = conn.cursor()
  cur.execute('INSERT INTO athletes (name, age) VALUES (?, ?)', (name, age))
  conn.commit()

def get_workouts_from_database(conn):
  cur = conn.cursor()
  cur.execute('SELECT * FROM workouts')
  return cur.fetchall()

def add_score_to_database(conn, athlete_id, workout_id, score):
  cur = conn.cursor()
  cur.execute('INSERT INTO scores (athlete_id, workout_id, score) VALUES (?, ?, ?)', (athlete_id, workout_id, score))
  conn.commit()


@app.route('/create_database')
def create_database():
  # Create the athletes table
  conn.execute('''CREATE TABLE athletes (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL
                );''')
  # Create the workouts table
  conn.execute('''CREATE TABLE workouts (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL
                );''')
  # Create the scores table
  conn.execute('''CREATE TABLE scores (
                  id INTEGER PRIMARY KEY,
                  athlete_id INTEGER NOT NULL,
                  workout_id INTEGER NOT NULL,
                  score INTEGER NOT NULL,
                  FOREIGN KEY (athlete_id) REFERENCES athletes(id),
                  FOREIGN KEY (workout_id) REFERENCES workouts(id)
                );''')
  conn.commit()
  return 'Database created successfully!'

if __name__ == '__main__':
  app.run()
