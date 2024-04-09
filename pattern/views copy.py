from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pattern, Comment
from .forms import PatternForm, CommentForm
from django.forms import ModelForm


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


def pattern_details(request, slug):
    queryset = Pattern.objects.filter(status=1)
    pattern = get_object_or_404(queryset, slug=slug)
    comments = pattern.comments.all().order_by("-created_on")
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
    else:
        comment_form = CommentForm()

    return render(
        request,
        'pattern/pattern_details.html',
        {
            "pattern": pattern,
            "comments": comments,
            "comment_form": comment_form
        },
    )


def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        queryset = Pattern.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))


def comment_delete(request, slug, comment_id):
    queryset = Pattern.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))
