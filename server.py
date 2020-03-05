from flask import Flask, render_template, url_for, escape, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<string:subpath>')
def show_subpath(subpath):
    return render_template(f'{subpath}')

def write_to_file(data):
    with open('database.txt', 'a') as file:
            for a,b in data.items():
                file.write(a + ': ' + b + '\n')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a') as file:
            w = csv.writer(file, delimiter=',')
            w.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # print(dir(request))
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong'
    