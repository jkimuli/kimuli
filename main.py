from flask import Flask,render_template,redirect,request
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

SENDGRID_KEY = config('SENDGRID')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email',methods=['POST'])
def send_email():
    
    # Construct the email that we want to be sent

    message = Mail(
        from_email= request.form['email'],
        to_emails='jkimuli@gmail.com',
        subject= 'Greetings from ' + request.form['name'],
        html_content= request.form['message']
    )

    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message) # send the email          
    
    return redirect('/')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
