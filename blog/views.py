from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .models import Blog, Category


def index(request):
    print("index関数を使ってTOP画面を表示します！")
    return render(request, "blog/index.html")


class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("index関数を使ってTOP画面を表示します！")
        return self.render_to_response(context)


class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context
