from django.shortcuts import render #use to return html file directly
from django.http import HttpResponse


# Create your views here.

def home(request): 
    # return  HttpResponse("<h1>This is a home page</h1>") # this is not a good practice as sometimes html,css can be heavy

    people = [
        {'name' : 'Ansh maheshwari' , 'age' : 20},
        {'name' : 'charchit Aggarwal' , 'age' : 13},
        {'name' : 'ri ma' , 'age' : 26},

    ]



    return render(request , "index.html", context = {'people' : people, 'page' : 'Home'})




def about(request):
    context = {'page' : 'About'}
    return render(request , "about.html")


def contact(request):
    context = {'page' : 'Contact'}
    return render(request , "contact.html")