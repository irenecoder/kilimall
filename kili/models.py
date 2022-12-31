from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kili:product_list_by_category',args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,blank=True)
    available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kili:product_detail', args=[self.id,self.slug])

