from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .models import Post, Tag, Category, Comment, Rating_Star


def blog_list(request):
    posts = Post.objects.all().order_by('-date_posted')


    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, id=pk)

    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('blog:post_detail', pk, slug)



@login_required
def dislike_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return redirect('blog:post_detail', pk, slug)
