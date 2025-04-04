from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class CustomUser(AbstractBaseUser):
    username=models.CharField(max_length=20,blank=False,null=True)
    email=models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    last_login=None

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['email','username']

    def __str__(self):
        return self.phone_number  












# class profilemodel(models.Model):
#     image=models.ImageField(upload_to="profilepics")
#     bio=models.CharField(max_length=300)
#     followers=models.ManyToManyField(User,related_name='followers',blank=True)
#     following=models.ManyToManyField(User,blank=True)
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")

# class Post(models.Model):
#     post = models.ImageField(upload_to="posts")
#     profileuser = models.ForeignKey(profilemodel,related_name="profile",on_delete=models.CASCADE)
#     likes = models.ManyToManyField(User,related_name="likes",blank=True,null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  