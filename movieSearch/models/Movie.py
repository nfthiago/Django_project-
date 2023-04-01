from movieSearch.models import *

class Movie(models.Model):
    name = models.CharField(null=False, max_length=100)
    genre = models.OneToOneField(Genre, blank=True, related_name='genre', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)