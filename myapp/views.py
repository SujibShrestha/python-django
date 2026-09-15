from django.shortcuts import render

# Create your views here.
def all_app(request):
    return render(request, 'myapp/all.html', {'name': 'all_app'})