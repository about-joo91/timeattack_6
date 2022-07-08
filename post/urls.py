from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView, UserApplyJobPostView

urlpatterns = [
    path('', SkillView.as_view()),

    path('job', JobView.as_view()),

    path('apply', UserApplyJobPostView.as_view())
]
