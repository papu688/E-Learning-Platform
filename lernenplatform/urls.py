
from django.contrib import admin
from django.urls import path
from lernplatform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('course_list/', views.course_list,name='course_list'),
    path('add/questions/', views.add_question,name='add_question'),
    path('questions/<slug:slug>/', views.question_detail, name='question_detail'),
    path('question_list',views.question_list, name='question_list'),
    path('student/courses/', views.student_courses, name='student_courses'),
    path('add/course', views.add_course, name='add_course'),
    path('question/delete/<str:title>/', views.delete_course, name='delete_course'),
    path('course/delete/<str:title>/', views.delete_question, name='delete_question'),
    path('course/edit/<str:title>/', views.edit_course, name='edit_course'),
    




]
