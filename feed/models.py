from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Study(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  abstract = models.TextField()
  inclusions = TaggableManager()
  start_date = models.DateField()
  end_date = models.DateField()
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title