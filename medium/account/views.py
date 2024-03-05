from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return redirect('blog:blog_list')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def favourite_list(request):
    new = Blog.published.filter(favourites= request.user)
    context = {'new': new}
    return render(request, 'registration/bookmarks.html', context)
@login_required
def favourite_add(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, id=id)
        if request.user.is_authenticated:
        
            if post.favourites.filter(id=request.user.id).exists():
                post.favourites.remove(request.user)
                
                post.save()
            else:
        
                post.favourites.add(request.user)
            

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('/')

