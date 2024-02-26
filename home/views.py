# views.py in your Django app

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        password = "[~9K[]X~PFZ+"
        email_content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Replace these with your actual email addresses
        sender_email = 'operations@platinum-my.com'
        recipient_email = ['operations@platinum-my.com']

        try:
            # send_mail(
            #     subject,
            #     email_content,
            #     'developer@noticevalley.com',
            #     ['developer@noticevalley.com'],
            #     fail_silently=False,
            # )
            send_email(subject, email_content, sender_email, recipient_email, password)
            
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        # Handle other HTTP methods if needed
        return HttpResponse(status=405)  # Method not allowed




# subject = "Email Subject"
# body = "This is the body of the text message"
# sender = "developer@noticevalley.com"
# recipients = ["coolarshad96@gmail.com", "developer@noticevalley.com"]
# password = "Coolarshad1@"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('sxb1plzcpnl487536.prod.sxb1.secureserver.net', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


# send_email(subject, body, sender, recipients, password)