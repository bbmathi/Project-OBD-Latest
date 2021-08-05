import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from django.shortcuts import render
import boto3

def reads3(request):
    s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                        aws_secret_access_key='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',
                        region_name='us-east-1'
                        )

    obj = s3.Object('ec2-obd2-bucket', '866039048578802/Data/866039048578802_rpm.txt')
    key = obj.key
    body = obj.get()['Body'].read()
    my_json = body.decode('utf8').replace("'", '"')
    #print('fileName :', key, 'filecontent:', my_json,body)
    RPM=my_json[8:14]
    #print(RPM)
    sender_email = "mathisiqsess@gmail.com"
    receiver_email = "mathivanan.b@siqsess.com"
    password = "Siqsess@Mathi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "RPM Alert"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    """
    html = """\
    <html>
      <body>
        <p>RPM crossed the Limit,<br>
           <a href="https://siqsess.com/#/home">Siqsess</a> <br>
           OBD Projects.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    if float(RPM)>450.0:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
        )
    return render(request, 'mail.html',context={"RPM":RPMx  })