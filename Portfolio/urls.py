from django.urls import path, include
from .views import SkillParcourView

urlpatterns = [
    path('', SkillParcourView.as_view(), name='parcours'),
]
