#to import every models in models directory
from movieSearch.models import *

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')

    #method used to show the object when instanciated
    def __str__(self):
        return '{}'.format(self.user.username)

    #notation needed to use the method bellow. 'post_save' tells post methods to create user.
    #'sender=User' tells which Model class is being called by post
    @receiver(post_save, sender=User)
    #method responsable to automatically create user profile
    def create_user_profile(sender, instance, created, **kwargs):
        #try block is used here to avoid superuser (which has no profile yet) to break the app
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    #Saves automatically any profile's change made in profile's view 
    def save_user_profile(sender, instance, **kwargs):
        #try block is used here to avoid superuser (which has no profile yet) to break the app
        try:
            instance.profile.save()
        except:
            pass
