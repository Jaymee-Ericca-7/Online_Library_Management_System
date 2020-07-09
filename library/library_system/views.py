from django.shortcuts import render
from django.http import HttpResponse

books = [
    {
        'title': 'The Lost Stars',
        'author': 'Jaymes Eric',
        'publisher': 'villacruz inc',
        'year_of_pub': '2019',
        'ISBN': 'BN154',
        'status': 'available',
        'reviews' : 'very awesome book'
    },
    {
        'title': 'The Found Stars',
        'author': 'Jaymes Eric',
        'publisher': 'villacruz inc',
        'year_of_pub': '2010',
        'ISBN': 'BN143',
        'status': 'available',
        'reviews' : 'very awesome book'
    },
    {
        'title': 'The Missing Stars',
        'author': 'Jaymes Eric',
        'publisher': 'villacruz inc',
        'year_of_pub': '2001',
        'ISBN': 'BN133',
        'status': 'available',
        'reviews' : 'very awesome book'
    }
]

def home(request):
    context = {
        'books': books
    }
    return render(request, 'library_system/home.html', context)

def about(request):
    return render(request, 'library_system/about.html')

def profile(request):
    return render(request, 'library_system/home.html')
