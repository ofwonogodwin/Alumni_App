from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)#Activity title
    description = models.TextField()#detailed description
    date = models.DateField()#date of the activity
    image = models.ImageField(upload_to='activities/',blank=True, null=True)
    created_at = models.DateField(auto_now_add=True) #auto timestamp

    def __str__(self):
        return self.title #display title in django admin