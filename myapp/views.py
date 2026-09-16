from django.shortcuts import render
from .models import appVariety
from django.shortcuts import get_object_or_404
# Create your views here.
def all_app(request):
    apps = appVariety.objects.all()
    return render(request, 'myapp/all.html', {'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(appVariety, pk=app_id)
    return render(request, 'myapp/detail.html', {'app': app})