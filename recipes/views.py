from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html', context={'home': 'home',})

def recipe(request, id):
    return render(request, 'pages/recipe_view.html', context={'id': id,})
