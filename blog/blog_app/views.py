from django.shortcuts import render, redirect
from .models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogView(ListView):
    model = Blog
    template_name = 'home.html'


def home_page(request):
    object_list = Blog.objects.all()
    ctx = {
        "object_list": object_list
    }
    return render(request, 'home.html', ctx)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'


def post_detail(request, pk):
    object = Blog.objects.get(id=pk)
    ctx = {
        'object': object
    }
    return render(request, 'post_detail.html', ctx)


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'create_post.html'
    fields = "__all__"


# def create_post(request):
#     model = Blog()
#     if request.POST:
#         model = Blog(
#             title=request.POST.get('title'),
#             author_id=request.POST.get('author_id'),
#             body=request.POST.get('body'),
#         )
#         model.save()
#         return redirect('home_page')
#     ctx = {
#         'model': model,
#     }
#     return render(request, 'create_post.html', ctx)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = '__all__'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home_page')