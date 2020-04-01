from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    name = request.form['name']
    email = request.form['email']
    question = request.form['question']
    with open('uploads/questions.csv','a') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow([name,email,question])
    return redirect('/view')

def read_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(row) for row in reader]

@app.route('/view')
def testing():
    csv_data = read_csv('uploads/questions.csv')
    headers = csv_data[0].keys()
    return render_template('view.html', csv_data=csv_data, headers=headers)

@app.route('/easter')
def easter():
  return render_template('easter.html')

app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  app.run(debug=True)