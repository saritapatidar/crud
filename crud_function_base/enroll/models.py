from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.pk: 
            super().save(*args, **kwargs)
        else:
            original_user = user.objects.get(pk=self.pk)
            self.email = original_user.email
            super().save(*args, **kwargs)



