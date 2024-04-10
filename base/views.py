from django.shortcuts import render

from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
    
def home(request):
    return render(request, 'inbox.html')

def compose(request):
    

    return render(request, 'compose.html')

def doc(request):
    return render(request, 'doc.html')

def dupe(request):
    return render(request, 'dupe.html')

def sent_preview(request):
    return render(request, 'sent-preview.html')

def sent(request):
    return render(request, 'sent.html')

def view(request):
    return render(request, 'view.html')

def voice(request):
    return render(request, 'voice.html')




