from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView
from .models import *

def ListContactView(request):
    context = {}
    objs = list(Contact.objects.all())
    context['contacts'] = objs

    return render(request,'address_book/contact_name.html', context)


def Contact_add(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    contact = Contact()
    contact.first_name = first_name
    contact.last_name = last_name
    contact.email = email
    contact.save()

    return redirect('contact-list')

def Contact_delete(request, id):
    ob = Contact.objects.get(id=id)
    ob.delete()
    return redirect('contact-list')

def Contact_edit(request, id):
    if request=='GET':
        ob = Contact.objects.get(id=id)
        context = {}
        context['ob'] = ob
        return render(request, 'address_book/contact_edit.html', context)
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        ob = Contact.objects.get(id=id)
        ob.first_name = first_name
        ob.last_name = last_name
        ob.email = email

        ob.save()
        return redirect('contact-list')
