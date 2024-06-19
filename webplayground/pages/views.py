from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse 


# Create your views here.

class PagesListView(ListView):
    
    model = Page

class PageDetailView(DetailView):
    
    model = Page

class PageCreate(CreateView):
    model = Page 
    fields = ["title", 'content', 'order']
    
    def get_success_url(self):
        return reverse('pages:pages')