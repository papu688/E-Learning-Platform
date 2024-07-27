from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    def clean(self):
        if self.is_student and self.is_instructor:
            raise ValidationError('User cannot be both student and instructor.')

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    materials = models.TextField()

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class Question(models.Model):
    title = models.CharField(max_length=100)
    student = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    answer = models.TextField(blank=True)
    answered_by = models.ForeignKey(User, related_name='answered_questions', null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)
