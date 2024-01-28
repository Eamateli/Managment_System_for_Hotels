from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField
from django.utils.translation import gettext_lazy as _ 



GENDER = (
    ("Woman","Woman"),
    ("Man","Man"),
    ("Other","Other"),
    ("Prefer not to answer","Prefer not to answer"),
)

IDENTITY_TYPE = (
    ("ID","ID"),
    ("Drivers' License","Drivers' License"),
    ("Passport","Passport"),

)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

class User(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='userauth_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='userauth_user_permissions')
    username = models.CharField(max_length=500, unique=True)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Other")
    
    otp = models.CharField(max_length=100, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyzw1234567890")
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="None")
    
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state  = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=600, null=True, blank=True)
    
    identity_type = models.CharField(max_length=200, choices=IDENTITY_TYPE, null=True, blank=True)
    identity_image = models.FileField(upload_to=user_directory_path, default="id.jpg", null=True, blank=True)
    
    facebook = models.URLField( null=True, blank=True)
    instagram = models.URLField( null=True, blank=True)
    twitter = models.URLField( null=True, blank=True)
    linkedin = models.URLField( null=True, blank=True)
    website = models.URLField( null=True, blank=True)
    other = models.URLField( null=True, blank=True)
    
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    
    date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        if self.full_name:
            return f"{self.full_name}"
        else:
            return f"{self.user.username}"
        

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwags):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

    
