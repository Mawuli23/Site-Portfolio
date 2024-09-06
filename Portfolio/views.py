from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skill, Parcour
# Create your views here.


class SkillParcourView(TemplateView):
    template_name = "Portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['parcours'] = Parcour.objects.all().order_by('-created_at')
        return context
