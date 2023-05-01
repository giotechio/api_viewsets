from django.db import models

# Create your models here.

class Posting(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey("auth.User", related_name="postings", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title