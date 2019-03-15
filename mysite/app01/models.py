from django.db import models

# Create your models here.
class Product(models.Model):
    #id,默认创建
    Asin = models.CharField(max_length=64)
    Total_reviews = models.CharField(max_length=64)
    Total_score = models.CharField(max_length=64)

class Detail(models.Model):
    Asin_detail = models.CharField(max_length=64)
    Total_reviews_detail = models.CharField(max_length=64)
    Total_score_detail = models.CharField(max_length=64)
    Asin_tag = models.CharField(max_length=500)
    Reviewer = models.CharField(max_length=200)
    Stars = models.CharField(max_length=64)
    Title = models.CharField(max_length=500)
    Date_str = models.CharField(max_length=64,default='2019-2-19')
    Review_content = models.CharField(max_length=5000)
    #AsinFK=models.ForeignKey(to="Product")
