from django.shortcuts import render, redirect
from .models import recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST": #ek ye tarika hai to get info from frontend to backend

        data = request.POST
        recipe_name = data.get('recipe_name')
        description = data.get('description')
        recipe_image = request.FILES.get('recipe_image')

        recipe.objects.create(
            recipe_name = recipe_name,
            description = description,
            recipe_image = recipe_image
            )
        
        return redirect('/recipes')
    
    queryset = recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search')) #__icontains is used to check that the asked content is present in the data or not

    context = {'recipes' : queryset}

    return render(request, "recipe.html", context)

def update_recipe(request, slug):
    queryset = recipe.objects.get(slug = slug)

    if request.method == "POST":

        data = request.POST
        recipe_name = data.get('recipe_name')
        description = data.get('description')
        recipe_image = request.FILES.get('recipe_image')
       
        queryset.recipe_name= recipe_name
        queryset.description = description

        if recipe_image:
            queryset.recipe_image = recipe_image
        
        queryset.save()
        
        return redirect('/recipes')

    context = {'recipe' : queryset}
    return render(request, 'update_recipe.html', context)


def delete_recipe(request, id):
    queryset = recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Username Invalid')
            return redirect('/login/')

        user = authenticate(username = username, password = password)
        # print(user)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user) #ek baar login karne ke baad baar baar login na karna pade for a particular time period we use login which alots a session to the user
            return redirect('/recipes/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def registration_page(request):

    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        Email_Id = data.get('Email_Id')
        Password = data.get('Password')
        # Confirm_Password = request.POST.get('Confirm_Password')
        
        if User.objects.filter(username = username):
            messages.info(request, 'Username already taken')
            return redirect('/registration')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = Email_Id,
        )
        user.set_password(Password)
        user.save()

        messages.info(request, 'Account created successfully')
        return redirect('/login/')


    return render(request, 'registration.html')
