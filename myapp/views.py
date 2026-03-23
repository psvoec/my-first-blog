from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    posts = post.objects.filter(published_date_lte=time-zone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'posts':posts})