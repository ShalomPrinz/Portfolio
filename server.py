from flask import Flask, render_template, request, redirect
import csv

# use this to email from the contact page when I want to
# import importlib

# moduleName = 'emailing.py'
# importlib.import_module(moduleName)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def home_page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = ["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'Something went wrong. Try again!'
