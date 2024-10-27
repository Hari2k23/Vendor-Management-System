from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title