from django.views import generic
from django.views.generic import edit
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from posts.mixins import SpecialGroupRequiredMixin
# Create your views here.


class HomeView(generic.ListView):
    '''
    List approved posts
    '''
    model = Post
    template_name = 'posts/home_page.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status=1)
    

#Create item by user // only authorized users.
class PostCreateView(LoginRequiredMixin, edit.CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['name', 'price', 'category', 'image']
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
 
    
class PostView(generic.DetailView):
    model = Post
    template_name = 'posts/post.html'


class PanelListPostsView(SpecialGroupRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/panel_management/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status=2).order_by('created')

  
class PanelHistoryPostsView(SpecialGroupRequiredMixin, generic.ListView):
      model = Post
      template_name = 'posts/panel_management/history.html'
      

class PanelEditPostView(SpecialGroupRequiredMixin, edit.UpdateView):
    model = Post
    template_name = 'posts/panel_management/pending.html'
    fields = ['status']
    success_url = reverse_lazy('posts:panel_pendings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(slug=self.object.slug)
        return context


class UserPendingPostsView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/user/pending_posts.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status=2).order_by('created')


class UserPostsView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'posts/user/posts.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status=1)


class UserEditPostView(LoginRequiredMixin, edit.UpdateView):
    model = Post
    template_name = 'posts/user/edit_post.html'
    fields = ['name', 'price', 'category', 'image']
    success_url = reverse_lazy('posts:user_pending_items')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = 2
        obj.save()
        return super().form_valid(form)
    