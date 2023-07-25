from flask import Flask, render_template , jsonify

app = Flask(__name__)
JOBS =[
  {
    'id' : 1,
    'title':'Data Analyst',
    'location' : 'Bengaluru',
    'salary': '1,00,000'
  },
  {
    'id' : 2,
    'title':'Data Scientist',
    
    'salary': '1,50,000'
  },
   {
    'id' : 3,
    'title':'Frontend Developer',
    'location' : 'Bengaluru',
    'salary': '1,60,000'
  },
   {
    'id' : 4,
    'title':'Backend Developer',
    'location' : 'Bengaluru',
    'salary': '1,80,000'
  }
]



@app.route("/")
def home():
  return render_template('home.html' , jobs = JOBS)
@app.route("/")
def joblist():
  return jsonify(JOBS)

                          


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
