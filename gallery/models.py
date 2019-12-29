from django.db import models

# Create your models here.

# 创建模板
class Gallery(models.Model):
	description = models.FileField(default='作品描述', max_length=100)
	title = models.CharField(default='作品标题', max_length=50)
	image = models.ImageField(default='default.jpg', upload_to='images/')
		