from django.db import models


class News(models.Model):

    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    image = models.URLField()

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return self.title
