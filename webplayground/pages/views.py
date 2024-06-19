from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect


# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin permitira que te valides como usuario para realizar las operacion CRUD
    """ 
    def dispatch(self, request,*args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login')) 
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class PagesListView(ListView):
    
    model = Page

class PageDetailView(DetailView):
    
    model = Page

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page 
    fields = ["title", 'content', 'order']
    success_url = reverse_lazy('pages:pages')
    
    
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    fields = ["title", 'content', 'order']
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
    
class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")