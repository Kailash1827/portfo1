import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# print(__name__)       #main

@app.route('/')
def my_home():
    return render_template('index.html')


#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/blog')
# def blog():
#     return 'Winners Never Quit'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # writer(data)
            writer_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Did not saved to database'
    else:
        return 'something went wrong'


def writer(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')


def writer_csv(data):
    with open('database2.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
