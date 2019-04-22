from .models import Conference, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConfForm, CommentForm

def listing(request):
    confs = Conference.objects.all()
    return render(request, 'conf/listing.html', {'confs': confs})

def conf_detail(request, pk):
    conf = get_object_or_404(Conference, pk=pk)
    comments = Comment.objects.filter(conf = conf)
    # if request.method == "POST":
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         comm = comment_form.save(commit=False)
    #         comm.user = request.user
    #         comm.conf = conf
    #         comm.save()
    # else:
    #     comment_form = CommentForm()
    return render(request, "conf/conf_detail.html", {"conf": conf,  'comments':comments})

def add_comment(request, pk):
    conf = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.conf = conf
            comment.user = request.user
            comment.save()

            return redirect(conf_detail, pk=conf.pk)
    else:
        form = CommentForm()
    return render(request, 'conf/add_comment.html', {'form': form})

def conf_new(request):
    if request.method == "POST":
        form = ConfForm(request.POST)
        if form.is_valid():
            conf = form.save(commit=False)
            conf.author = request.user
            conf.published_date = timezone.now()
            conf.save()
            return redirect('conf_detail', pk=conf.pk)
    else:
        form = ConfForm()
    return render(request, 'conf/conf_edit.html', {'form': form})

def conf_edit(request, pk):
    conf = get_object_or_404(Conference, pk=pk)
    if request.method == "POST":
        form = ConfForm(request.POST, instance=conf)
        if form.is_valid():
            conf = form.save(commit=False)
            conf.save()
            return redirect('conf_detail', pk=conf.pk)
    else:
        form = ConfForm(instance=conf)
    return render(request, 'conf/conf_edit.html', {'form': form})

def logout(request):
    logout(request)