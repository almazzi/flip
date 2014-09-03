from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from .forms import ProductForm


def create(request):
    if request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin/')
    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_product.html' ,args)
# Create your views here.
