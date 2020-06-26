from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. %d" % angka)

def number(request, number):
    return HttpResponse("This is number request page. %d" % number)

def example0(request):
    return HttpResponse("This is example output 0.")

def example1(request):
    return HttpResponse("This is example output 1.")

def example2(request):
    return HttpResponse("This is example output 2.")

def template(request):
	tulisan0 = "This is template-driven page."
	tulisan1 = "This is template-driven title."
	daftar = {
		"example0",
		"example1",
		"example2",
	}

	template = "custom_app/detail.html"
	context = {
		'tulisan0': tulisan0,
		'tulisan1': tulisan1,
		'daftar': daftar,
	}

	return render(request, template, context)