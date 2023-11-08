from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.CharField(verbose_name="カテゴリ名", max_length=100, unique=True)
    category_image = models.ImageField(verbose_name="カテゴリ画像", upload_to="images/")
