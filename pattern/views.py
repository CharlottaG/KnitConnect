from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pattern
from .forms import PatternForm


# Create your views here.

class PatternList(generic.ListView):
    model = Pattern
    template_name = "pattern/patterns.html"
    #paginate_by = 6

def add_pattern(request):
    if request.method == "POST":
        pattern_form = PatternForm(request.POST, request.FILES)
        if pattern_form.is_valid():
            pattern = pattern_form.save(commit=False)
            pattern.created_by = request.user
            pattern.save()
            pattern_form = PatternForm()
            messages.success(request, 'Your pattern was added successfully!')
            return redirect('patterns')
    else:
        pattern_form = PatternForm()
    
    return render(request, "pattern/add_pattern.html", {'pattern_form': pattern_form})
