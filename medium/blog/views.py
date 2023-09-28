from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
# from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from .models import Blog, Comment
<<<<<<< HEAD:blog/views.py
from .forms import EmailPostForm, CommentForm, SearchForm, TopicForm
=======
from .forms import EmailPostForm, CommentForm, SearchForm
>>>>>>> d32a961ec6d747a0d677f67036b53b44970dcf36:medium/blog/views.py

# Create your views here.
# class BlogListView(ListView):
def blog_list(request, tag_slug=None):
    
    object_list = Blog.published.all()
    tag = None
   

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    # context_object_name = 'blogs'
    # template_name = 'blog/list.html'
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = Paginator.page(paginator.num_pages)



    context = {
        'page': page,
        'blogs': blogs,
        'tag': tag
    }
    return render(request, 'blog/list.html', context)
def blog_detail(request, year, month, day, blog):
    blog = get_object_or_404(Blog, slug=blog, status='published', publish__year=year, publish__month=month, publish__day=day)

    # list of active comments
    comments = blog.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # POST a commnet
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to database just yet
            new_comment = comment_form.save(commit=False)
            # assign new comment to blog
            new_comment.post = blog
            # save to database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    # list posts with similar tags
    post_tag_id = blog.tags.values_list('id', flat=True)
    similar_posts = Blog.published.filter(tags__in=post_tag_id).exclude(id=blog.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    context = {'blog': blog, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form, 'similar_posts':similar_posts}
    return render(request, 'blog/details.html', context)
@login_required
def new_blog(request):
    """Add a new blog"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        
    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)
# post notification

@login_required
def post_share(request, post_id):
    # retrieve post by id
    post = get_object_or_404(Blog, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # SUBMIT FORM
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read \ {post.title}"
            message = f"Read {post.title} at {post_url}\n\n \\ {cd['name']} \ comments: {cd['comments']}"
            send_mail(subject, message, 'dennismurage97@gmail.com', [cd['to']])
            sent = True
            # .....send mail
    else:
        form = EmailPostForm()
    context = {'post': post, 'form': form, 'sent': sent}
    return render(request, 'blog/share.html', context)

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Blog.published.annotate(search=SearchVector('title', 'body')).filter(search=query)
    context = {
        'form': form,
        'query': query,
        'results': results,
    }

    return render(request, 'blog/search.html', context)