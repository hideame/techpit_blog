from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.CharField(verbose_name="カテゴリ名", max_length=100, unique=True)
    category_image = models.ImageField(verbose_name="カテゴリ画像", upload_to="images/")


class Blog(models.Model):
    class Meta:
        db_table = "blog"

    title = models.CharField(verbose_name="タイトル", max_length=100)
    content = models.TextField(verbose_name="内容")
    postdate = models.DateField(verbose_name="投稿日", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="カテゴリ")
