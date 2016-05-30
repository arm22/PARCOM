from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models import signals

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

class Comment(models.Model):
  study = models.ForeignKey('feed.Study', related_name='comments')
  author = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.text

class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  age = models.IntegerField(null=True)
  occupation = models.CharField(max_length=200)
  about = models.TextField()
  GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA', 'Not Applicable')
  )
  sex = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
  interests = TaggableManager()

  def __str__(self):
    return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

signals.post_save.connect(create_user_profile, sender=User)