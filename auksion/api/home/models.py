from django.db import models
from ..base.models import Basemodel
from ..accounts.models import Usermodel
from django.core.validators import FileExtensionValidator
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel, Basemodel):
    name = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return self.name



class Productmodel(Basemodel):
    user = models.ForeignKey(Usermodel, on_delete=models.CASCADE, related_name='user_product', blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user/products/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])
    discription = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product', blank=True)
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
class Certificatemodel(Basemodel):
    user = models.ForeignKey(Usermodel, on_delete=models.CASCADE, related_name='user_certificate', blank=True)
    product = models.ForeignKey(Productmodel, on_delete=models.CASCADE, related_name='product_certificate', blank=True)
    code = models.BinaryField()
    
    def __str__(self) -> str:
        return self.uuid