from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy

from schedule.forms import SearchForm, StudentForm
from schedule.models import Course, Teacher


class CourseListView(generic.ListView):
    model = Course
    template_name = 'schedule/main.html'

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            return Course.objects.filter(title__icontains=q)

        # Reset and show all
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['num_courses'] = context['course_list'].count()
        return context


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'schedule/course_details.html'


class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = 'schedule/teacher_details.html'


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(student)
            return redirect('student-create')

    form = StudentForm()
    return render(request, 'schedule/add_course.html', {'form': form})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'signup.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')
    template_name = 'login.html'
