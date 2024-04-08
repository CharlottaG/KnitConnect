from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .models import User
from .forms import ProfileForm


class ProfilesList(generic.ListView):
    queryset = User.objects.filter()
    template_name = "user/profiles_list.html"
    #paginate_by = 6

def add_profile(request):
    if request.method == "POST":
        print(request.POST)
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.created_by = request.user
            profile.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Congratulations! Your profile has been added.'
            )
            return redirect('user_profile', slug=profile.slug)
    else:
        profile_form = ProfileForm()

    return render(
        request,
        "profiles/add_profile.html",
        {
            "profile_form": profile_form
        },
    )


def user_profile(request, slug):
    profile = get_object_or_404(User, slug=slug)
    return render(request, 'user_profile.html', {'user': user})

