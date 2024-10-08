from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import HomeNew
from .forms import AddPostForm, ContactForm
from .tasks import send_form

# Create your views here.

class HomePage(ListView):
    model = HomeNew
    template_name = 'main/index.html'
    context_object_name = 'news'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'main/addpost.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            return super(CreateView, self).dispatch(request, *args, **kwargs)

        


# def index(request):
#     return render(request, 'main/index.html')


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_data = ''.join(['From:\n', form.cleaned_data['mail'], '\n\nText:\n', form.cleaned_data['text']])
            send_form.delay(send_data)
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'main/about.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')

# def help(request):
#     return render(request, 'main/help.html') # Template was removed