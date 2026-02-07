from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin

from django.contrib.auth import login, logout, authenticate

from .models import Post, Category
from .forms import ProfileForm, UserForm, CommentForm

class IndexView(TemplateView):
    template_name = 'index.html'


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('account'))
    
    return render(request,'login.html')

def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class UserAccount(TemplateView):
    template_name = 'account.html'

def UserSignup(request):
    user_profile = ProfileForm
    user_form = UserForm

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            user_profile.instance.user = user
            user_profile.save()

            return HttpResponseRedirect(reverse('login'))
    
    return render(request, 'signup.html', context={'user_form' : UserForm, 'profile' : ProfileForm})

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['post_category', 'post_img', 'post_name', 'post_alt', 'post_description']
    template_name = 'app/createpost.html'
    success_url = reverse_lazy('app:create-post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'app/createcategory.html'
    success_url = reverse_lazy('app:create-category')

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['post_category', 'post_img', 'post_name', 'post_alt', 'post_description']
    template_name = 'app/createpost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'app/confirm_delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('app:list-posts')

class DetailPost(FormMixin, DetailView):
    model = Post
    template_name = 'app/detailpost.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request):
        self.object = self.get_object() 
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object 
            comment.user = request.user  
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('app:detail-post', kwargs={'pk': self.object.pk})

class ListPost(ListView):
    model = Post
    template_name = 'app/listpost.html'
    context_object_name = 'posts'
    paginate_by = 12

# Create your views here.
