from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50) 
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note title: {self.title} body: {self.body}"
    