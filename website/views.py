from django.shortcuts import render
from django.http import HttpResponse
from website.models import StickyNotes
# Create your views here.

def home(request):
    return render(request,'index.html', {})

def highlights(request):
    highlights= StickyNotes.objects.all()
    context={
        'highlights': highlights
    }
    return render(request, 'index.html', context)