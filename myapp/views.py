from django.shortcuts import render
from .models import appVariety, Store
from django.shortcuts import get_object_or_404
from .forms import AppVarietyForm

# Create your views here.
def all_app(request):
    apps = appVariety.objects.all()
    return render(request, 'myapp/all.html', {'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(appVariety, pk=app_id)
    return render(request, 'myapp/detail.html', {'app': app})

def stores(request):
    stores = None
    if request.method == 'POST':
        form = AppVarietyForm(request.POST)
        if form.is_valid():
            app_variety = form.cleaned_data['app_variety']
            stores = Store.objects.filter(app_varieties = app_variety)
    else:
        form = AppVarietyForm()

    return render(request, 'myapp/stores.html', {'stores': stores, 'form': form} )  
