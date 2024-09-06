from django.contrib import admin
from .models import Skill, Parcour
# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Parcour)
class ParcourAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
