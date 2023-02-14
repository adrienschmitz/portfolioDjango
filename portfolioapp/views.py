from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def portfolio(request):
	template_name = "portfolio.html"
	if request.method == 'POST':
		form = ContactForm(request.POST)
   
	form = ContactForm()
	return render(request, "portfolio.html", {'form':form})
