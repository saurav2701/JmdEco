from django.db import models

# Create your models here.
class Products(models.Model):  
    sn = models.IntegerField(default= 0)
    name = models.CharField(max_length= 25 ) 
    price = models.IntegerField(default=0  )   
    image = models.ImageField(upload_to = 'product/'  ) 
    category  = models.CharField(max_length= 25  )

    def __str__(self):
        return str(self.image)
