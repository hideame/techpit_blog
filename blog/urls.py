from django.urls import path

from .views import index, IndexView

urlpatterns = [
    path("index", index, name="index"),
    path("index_class", IndexView.as_view(), name="index_class"),
]
