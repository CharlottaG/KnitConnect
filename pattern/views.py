from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Pattern, Comment, Like
from .forms import CommentForm, PatternForm
from django.forms import ModelForm
from django.utils.text import slugify


class PatternList(generic.ListView):
    model = Pattern
    template_name = "pattern/patterns.html"
    paginate_by = 6

def my_page(request):
    return render(request, 'pattern/my_page.html')


#@login_required
def pattern_details(request, slug):
    pattern = get_object_or_404(Pattern, slug=slug)
    comments = Comment.objects.filter(pattern=pattern).order_by("-created_on")

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.pattern = pattern
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )
    
    comment_form = CommentForm()

    # Count the number of likes for the pattern
    like_count = pattern.likes.count()

    return render(
        request,
        'pattern/pattern_details.html',
        {
            "pattern": pattern,
            "comments": comments,
            "comment_form": comment_form,
            "like_count": like_count, 
        },
    )


@login_required
def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        post = get_object_or_404(Pattern, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Pattern, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))


@login_required
def add_pattern(request):
    if request.method == "POST":
        pattern_form = PatternForm(request.POST, request.FILES)
        if pattern_form.is_valid():
            pattern = pattern_form.save(commit=False)
            pattern.created_by = request.user
            pattern.slug = slugify(pattern.pattern_name)
            pattern.save()
            messages.success(request, 'Your pattern was added successfully!')
            return redirect('patterns')
        
    else:
        # Form is invalid; display error messages
        messages.error(request, 'Please correct the errors in the form.')
        pattern_form = PatternForm()
    
    return render(request, "pattern/add_pattern.html", {'pattern_form': pattern_form})


@login_required
def like_pattern(request, slug):
    pattern = get_object_or_404(Pattern, slug=slug)
    like, created = Like.objects.get_or_create(user=request.user, pattern=pattern)

    if created:
        messages.success(request, "You've liked this pattern.")
    else:
        messages.error(request, "You've already liked this pattern.")
    
        return redirect('pattern_details', slug=slug)