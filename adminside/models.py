from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"

class Items(models.Model):
    name = models.CharField(max_length=50)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"

class ItemImage(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = "Item Image"