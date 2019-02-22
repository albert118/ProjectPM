from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

from .models.AttributeLists import Skills, Education, Languages, WorkHist
from .models.profilemodel import CV


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
	list_display = ("skill", "validated", "desc")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	pass

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
	list_display = ("language", "iso_code")

@admin.register(WorkHist)
class WorkHistAdmin(admin.ModelAdmin):
	pass

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
	list_display = ("__str__", "created_at")
	fieldsets = (
		(None, {
			'description' : ("Admin editing page for the Better Resume app.",),
			'fields' : ('user', ('eduhist', 'langs','skill', 'wrkhist'),  'bio')
		}),
		('Advanced Options', {
			'classes' : ('collapse',),
			'fields' : ('created_at', 'edited_at',)
		}),
		)
