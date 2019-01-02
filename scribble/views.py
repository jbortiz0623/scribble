from django.shortcuts import render
from .models import Comment, Post
from django.http import HttpResponse
from .forms import PostForm,CommentForm
# Create your views here.

# def index(request):
#     return HttpResponse(request, 'scribble/base.html')

#index
def post_list(request):
    post = Post.objects.all()
    return render(request, 'scribble/post_list.html',{'posts':post})
#index
def comment_list(request):
    comment = Comment.objects.all()
    return render(request, 'scribble/comment_list.html',{'comments',comment})

def post_detail(request, id):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post':post})

def comment_detail(request, id):
    comment = Comment.objects.get(id=pk)
    return render(request, 'scribble/comment_detail.html', {'comment':comment})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = post.save(commit = False)
            post.save()
        return HttpResponse('/')
    else :
        return render(request,'scribble/create.html',{'form':PostForm})

def comment_create(request):
    form = CommentForm(request.POST)
    if form.is_valid:
        comment = form.save(commit = False)
        comment.save()
    return HttpResponseRedirect('/')

# def post_edit(request, pk):
#     post =

# def post_edit(request, pk):
#     post = Post.objects.get(pk=pk)
#         if request.method == 'POST':
#             form = PostForm(request.POST)

    