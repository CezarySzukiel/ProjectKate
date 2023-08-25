"""
URL configuration for Katemath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from exercises_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'exercises', views.ExercisesViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'sections', views.SectionsViewSet)
router.register(r'subsections', views.SubsectionsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('list/', views.ExercisesListView.as_view(), name='exercises_list'),
    path('exercise_details/<int:pk>', views.ExerciseDetailsView.as_view(), name='exercise_details'),
    path('exercise_details/<int:pk>/summary', views.SubmitView.as_view(), name='exercise_submit'),
    # path('create/', views.ExercisesCreateView.as_view(), name='exercises_create'),
]
