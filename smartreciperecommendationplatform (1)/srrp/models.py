from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.TextField()
    instructions = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    prep_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

