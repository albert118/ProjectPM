""" The attribute list models.
	Models for skills, hobbys, languages, etc.. added below.
	
	IDEA: Every user has unique skills, add them to their porfolio! 
	TODO: include options for porfolio plugins to further extend this idea.
	
	Importable as: AttributeLists
	
	Author: Albert Ferguson"""

from __future__ import unicode_literals
from django.db import models
import os
import inspect
from django.conf import settings 
""" use django.conf import rather than, django.contrib.auth.models import User 
	see: https://stackoverflow.com/questions/19976115/whats-the-difference-between-from-django-conf-import-settings-and-import-set """
from django.utils.encoding import python_2_unicode_compatible

class attList(models.Model):
	res_file_dir = settings.STATIC_ROOT 

	class Meta:
		abstract = True

@python_2_unicode_compatible    
class Skills(attList):
	""" Model describing the user's skills as a many-to-one relation to a skill table. """
	# TODO: Add validation as in tmp/attributes but for database
	skill = models.CharField(max_length=50, null=True)
	validated = models.BooleanField(default=False)
	desc = models.CharField(max_length=100, null=True, blank=True)
	class Meta:
		db_table = "skills"
		ordering = ('skill',)

	def __str__(self):
		return self.skill

@python_2_unicode_compatible
class Education(attList): 
	""" Model describing the user's education history as a many-to-one relation"""
	edu = models.CharField(max_length=25, null=True, blank=False) 
	startDate = models.DateField(null=True, blank=False)
	endDate = models.DateField(null=True, blank=False) 
	qualification = models.CharField(max_length=100, null=True, blank=False)

	class Meta:
		db_table = "eduhist"
		verbose_name = "Education"
		
	def __str__(self):
		return self.edu

@python_2_unicode_compatible
class Languages(attList):
	"""The applicant's known languages. """
	language = models.CharField(max_length=15, null=True)
	iso_code = models.CharField(max_length=2, null=True)

	BEGINNER = "Beginner"
	INTERMEDIATE = "Intermediate"
	ADVANCED = "Advanced"
	PROFICIENCY_CHOICES = (
		(BEGINNER, "Beginner"), 
		(INTERMEDIATE, "Intermediate"), 
		(ADVANCED, "Advanced"),
		)
	proficiency = models.CharField(max_length=12,choices=PROFICIENCY_CHOICES,default=BEGINNER,blank=False) 

	class Meta:
		db_table = "languages"
		ordering = ("language",)

	def __str__(self):
		return self.language

	def getLangs(self):
		from django.core import serializers
		import json
		""" Read the lang data from a res file & update the database. """
		counter = 0

		try:
			# res file in same (development) directory
			data = open("Languages.txt", "r")
			langs_dict = json.loads(data)
			
			for lang in langs_dict:
				_lang = Languages.objects.create(
					pk=counter, language=lang['name'], iso_code=str(lang)
					)
				counter += 1
		except IOError:
			print("Language resource file not found!")
		"""else:
		# res file in production directory
		path = "res_file_dir/res/Languages.txt"
		data = open(path, "r")
		langs_dict = json.loads(data)
		
		foreach lang in langs_dict:
			_lang = Languages.objects.create(
				pk=counter, language=lang['name'], iso_code=str(lang)
				)
			counter += 1"""


@python_2_unicode_compatible
class WorkHist(attList):
	"""The applicant's work experience/history. TODO: Add questionaire results..."""
	business = models.CharField(max_length=120)
	review = models.CharField(max_length=500, default="", blank=True)
	rating = models.IntegerField(default=0)
	term_start = models.DateField(null=True, blank=False)
	term_end = models.DateField(null=True, blank=False)

	class Meta:
		db_table = "workhist"
		ordering = ("business",)

	def __str__(self):
		return "Employment at: %s" %(self.business)
