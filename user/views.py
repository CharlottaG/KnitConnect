from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .models import User
from .forms import ProfileForm


class ProfilesList(generic.ListView):
    queryset = User.objects.filter()
    template_name = "user/profiles_list.html"
    #paginate_by = 6

@login_required
def add_profile(request):
    if request.user.is_authenticated:
        # Check if the user already has a profile
        if hasattr(request.user, 'profile'):
            # User already has a profile, redirect them there
            return reverse('user_profile', username=request.user.profile.username)
        
        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save() 
                messages.add_message(
                    request, messages.SUCCESS,
                    'Congratulations! Your profile has been added.'
                )
                return redirect('user_profile', username=profile.username)
        else:
            profile_form = ProfileForm()

        return render(
            request,
            "user/add_profile.html",
            {
                "profile_form": profile_form
            },
        )

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user/profile_details.html', {'user': user})

