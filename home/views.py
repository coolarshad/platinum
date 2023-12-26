# views.py in your Django app

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Replace these with your actual email addresses
        sender_email = email
        recipient_email = ''

        try:
            send_mail(
                subject,
                email_content,
                sender_email,
                [recipient_email],
                fail_silently=False,
            )
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        # Handle other HTTP methods if needed
        return HttpResponse(status=405)  # Method not allowed
