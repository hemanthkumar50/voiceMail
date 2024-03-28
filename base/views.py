from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

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
def vr(request):
    return render(request, 'vr.html')
