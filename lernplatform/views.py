from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .decorators import instructor_required


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.student = request.user
            question.save()
            return redirect('question_detail', slug=question.slug)
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

@login_required
def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_form = None
    if request.user.is_instructor:
        if request.method == 'POST':
            answer_form = AnswerForm(request.POST, instance=question)
            if answer_form.is_valid():
                question = answer_form.save(commit=False)
                question.answered_by = request.user
                question.save()
                return redirect('question_detail', slug=question.slug)
        else:
            answer_form = AnswerForm(instance=question)
    return render(request, 'question_detail.html', {'question': question, 'answer_form': answer_form})

def question_list(request,):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})


@login_required
def student_courses(request):
    # Fetch progress records associated with the logged-in student
    progress_records = Progress.objects.filter(student=request.user).select_related('course')
    courses = [{'course': record.course, 'completed': record.completed} for record in progress_records]
    
    return render(request, 'student_courses.html', {
        'courses': courses,
    })

@login_required
@instructor_required
def add_course(request):
    if request.user.is_instructor:
        if request.method == 'POST':
            form = AddCourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('course_list')
        else:
            form = AddCourseForm()
        return render(request, 'add_course.html', {'form': form})
    else:
        return HttpResponse('U have not instructor status')
@login_required
@instructor_required
def delete_course(request, title):
    course = Course.object.get(title=title)

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})

@login_required
@instructor_required
def delete_question(request, title):
    question = get_object_or_404(Question, title=title)

    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'delete_question.html', {'question': question})

@login_required
@instructor_required
def edit_course(request, title):
    course = get_object_or_404(Course, title=title)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'edit_course.html', {'form': form, 'course': course})




