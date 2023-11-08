from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    print("index関数を使ってTOP画面を表示します！")
    return render(request, "blog/index.html")


class IndexView(TemplateView):
    template_name = "blog/index.html"
    # print("index関数を使ってTOP画面を表示します！")

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("index関数を使ってTOP画面を表示します！")
        return self.render_to_response(context)
