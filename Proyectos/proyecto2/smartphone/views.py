from django.shortcuts import render, redirect
from smartphone.models import Manufacturers
from smartphone.forms import SmartphoneForm

# Create your views here.
def list_smartphone(request):
    manufacturers = Manufacturers.objects.all()

    context = {
        'manufacturers': manufacturers

    }

    return render(request, template_name='smartphone/list_manufacturers.html', context=context)

def create_smartphone(request):
    if request.method == "POST": # Es cuando quiero subir el template completado. Guardar en la base de datos lo que vamos a crear.
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_smartphone)
    
    form = SmartphoneForm()
    context = {
        "form": form
    }
    return render(request, template_name='smartphone/register_smartphone.html', context=context)