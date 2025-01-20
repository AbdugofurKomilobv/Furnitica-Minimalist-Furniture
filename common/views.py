from django.shortcuts import render

def home_page_view(requests):
    return render(requests,template_name='index.html')
