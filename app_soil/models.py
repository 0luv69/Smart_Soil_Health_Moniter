from django.db import models
from django.contrib.auth.models import User


class All_soil(models.Model):
    soil_image= models.ImageField(upload_to="images/soil_image", null=True, blank=False)
    soil_name = models.CharField( max_length=100) 
    soil_discription= models.TextField(null=True )

    
# Create your models here.
class Test_soil(models.Model): 
    usersd = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    soil_image= models.ImageField(upload_to="images/user_soil_image", blank=False)
    soil_discription= models.TextField(null=True )
    soil_location= models.CharField(max_length=100)
    soil_name_col = models.CharField( max_length=100)
    date_added= models.DateTimeField(auto_now_add=True)





   






