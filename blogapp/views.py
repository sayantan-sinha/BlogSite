from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, PostForm
from django.contrib import messages
from .models import Post


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'blogapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'blogapp/register.html', context=context)

@login_required
def dashboard(request):
    public_posts = Post.objects.filter(
        user=request.user,
        is_public=True,
    ).order_by('-date_posted')

    private_posts = Post.objects.filter(
        user=request.user,
        is_public=False,
    ).order_by('-date_posted')

    context = {
        'public_posts': public_posts,
        'private_posts': private_posts,
        'welcome': "Welcome to your dashboard"
    }

    return render(request, "blogapp/dashboard.html", context=context)


@login_required
def compose(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if (form.is_valid()):
            cd = form.cleaned_data
            if (cd.get('image')):
                image = request.FILES['image']
            else:
                image = ''

            post = Post(user=request.user,
                        title=cd.get('title'),
                        description=cd.get('description'),
                        image=image,
                        is_public=cd['is_public']
                        )
            post.save()
            return redirect(reverse('blogapp:dashboard'))

    else:
        form = PostForm()

    context = {
        "write": "Write an Article",
        'form': form
    }

    return render(request, "blogapp/compose.html", context=context)

def search_users(request):
    if(request.method == 'POST'):
        user = request.POST.get('search_for')
        user = User.objects.filter(username = user)
        if(user.exists()):
            user = user[0]
            public_posts = Post.objects.filter(
                        user = user,
                        is_public = True,
                    ).order_by('-date_posted')

            context = {
                'public_posts': public_posts,
                'search_for': user
            }
            return render(request,"blogapp/dashboard.html", context=context)
        else:
            messages.warning(request, 'USER DOES NOT EXISTS')
    return render(request,"blogapp/dashboard.html")
