from django.urls import path
from .views import CourseListView, CourseDetailView, TeacherDetailView, student_create, SignupView, CustomLoginView

urlpatterns = [
    path('schedule/main/', CourseListView.as_view(), name='main'),
    path('schedule/course_details/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('schedule/teacher_details/<int:pk>', TeacherDetailView.as_view(), name='teacher-detail'),
    path('schedule/add_course/', student_create, name='student-create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
