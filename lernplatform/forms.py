from django import forms
from .models import Course, Question, User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_student', 'is_instructor']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'materials']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','student', 'text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['answer']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
