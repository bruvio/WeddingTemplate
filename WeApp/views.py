from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RSVP_FORM, Comments_Forms
from .models import RSVP as rsvp , Comments , Excurisons as Exc,Hotels as hote             
# Create your views here.


def Travel(request):
    Data_hotels = hote.objects.all()
    Data_excursion = Exc.objects.all()
    context = {
     "Data_hotels": Data_hotels,
     "Data_excursion": Data_excursion,
   }
    return render(request, "Travel.html", context)

def WeApp(request):
    
    return render(request, "homeW.html")



def RSVP(request):
    Data_comments = rsvp.objects.all()
    form = RSVP_FORM()  # Move this line outside the if block
    
    if request.method == 'POST':
        name = request.POST['name']
        attend = request.POST['attend']
        phone = request.POST['phone']
        print(name,attend,phone)
        obj = rsvp()
        obj.name = name
        obj.attend = attend
        obj.phone = phone
        obj.save()
        form = RSVP_FORM(request.POST)
        return redirect('RSVP')
    else:
        form = RSVP_FORM()
    
    return render(request, "RSVP.html", {
        "form": form,
    })   

def FAQ(request):
    Data_question = Comments.objects.all()
    form = Comments_Forms()  # Move this line outside the if block
    
    if request.method == 'POST':
        name = request.POST['name']
        question = request.POST['question']
        print(name,question)
        obj = Comments()
        obj.name = name
        obj.question = question
        obj.save()
        form = Comments_Forms(request.POST)
        return redirect('FAQ')
    else:
        form = Comments_Forms()
    
    return render(request, "FAQ.html", {
        "form": form,
        "Data_question": Data_question
    })     
               
def itenary(request):
    image_url = '/static/images/itenary1.jpg'
    image_url2 = '/static/images/clouds.png'
    image_url3 = '/static/images/plane.png'
    image_url4 = '/static/images/Chapel.png'

    context={
     'image_url':image_url,
     'image_url2':image_url2,
     'image_url3':image_url3,
     'image_url4':image_url4,

    }
    return render(request, "itenary.html",context)
             
               
