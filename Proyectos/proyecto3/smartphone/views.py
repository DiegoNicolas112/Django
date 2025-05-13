from django.shortcuts import render, redirect
from smartphone.models import Manufacturers
from smartphone.forms import SmartphoneForm, CompanyForm
from django import forms
import requests


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

def create_companies(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            companies = form.cleaned_data['companies']
            response = requests.get(f'https://fakerapi.it/api/v1/companies?_quantity={companies}')
            print(response.json())  # o lo que necesites hacer con los datos
            if response.status_code == 200:
                data = response.json()['data']
                for company in data:
                    company = Manufacturers(
                        name=company['name'],
                        country_origin=company['country'],
                        date_of_fundation=company['contact']['birthday'],
                        website=company['website'],
                    )
                    company.full_clean()
                    company.save()
            return redirect('list_manufacturers')  # o alguna otra vista
    else:
        form = CompanyForm()

    context = {'form': form}
    return render(request, 'smartphone/create_companies.html', context)