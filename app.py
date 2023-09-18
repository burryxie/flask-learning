# import os

# for file in os.listdir():
#   if file.startswith('.'):
#     print(file)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'ID': 1,
    'Title': 'Data Engineering',
    'Location': 'Shenzhen,China',
    'Salary': 'RMB 20000'
}, {
    'ID': 2,
    'Title': 'Data Architect',
    'Location': 'Shenzhen,China',
    'Salary': 'RMB 30000'
}, {
    'ID': 3,
    'Title': 'Data Scientist',
    'Location': 'Hongkong,China',
    'Salary': 'RMB 40000'
}]


@app.route('/')
def home_page():
  # return "Hello World"
  return render_template("home.html"
                         , jobs=JOBS
                         , company_name="Hello")

@app.route('/api/jobs')
def get_all_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
