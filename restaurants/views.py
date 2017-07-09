import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation
# Create your views here.
# function based view
# def home(request):
	
# 	html_='''<!DOCTYPE html>
# 	<html lang='en'>
# 	<head>
# 	</head>
# 	<body>
# 	<h1>Django</h1>
# 	<p>This is Django coming through</p>
# 	</body>
# 	</html>
# 	'''
# 	return HttpResponse(html_)



# def home(request):
# 	context = {
# 	}
# 	return render(request, 'home.html', context)

# def contact(request):
# 	context = {
# 	}
# 	return render(request, 'contact.html', context)

# def about(request):
# 	context = {
# 	}
# 	return render(request, 'about.html', context)

# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		print(kwargs)
# 		context = {}
# 		return render(request, 'contact.html', context)

# class HomeView(TemplateView):
# 	template_name = 'home.html'
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		num = None
# 		some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
# 		condition = True
# 		if condition:
# 			num = random.randint(0, 1000000)
# 		context = {
# 			'num': num,
# 			'some_list': some_list
# 		}
# 		return context

def restaurants_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, template_name, context)