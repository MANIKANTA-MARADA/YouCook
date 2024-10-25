from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, RecipeForm
from .models import Recipe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

@login_required
def app(request):
    return render(request, 'app.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def base(request):
    return render(request, 'base.html')

def recipe_list(request):
    query = request.GET.get('q', '')
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes, 'query': query})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

from django.shortcuts import render, redirect
from .forms import RecipeForm  # Adjust this import based on your actual form location

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'form.html', {'form': form})


@csrf_exempt  # Note: Use with caution and ensure CSRF protection in production
def rate_recipe(request, recipe_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = data.get('rating')

        # Update the recipe rating
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe.rating = rating  # Here you might want to implement logic for averaging ratings if needed
            recipe.save()
            return JsonResponse({'status': 'success'})
        except Recipe.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Recipe not found.'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def contactlogic(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        subject = 'Thank You for ur valuable Feedback'
        send_mail(
            subject,
            comment,
            'praveenluru@gmail.com',  # Update with your sender email
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Thank you for giving Feedback </center></h1>")
    else:
        HttpResponse("<h1>error</h1>")