""" Python implemenation of the user profile/resume class for BetterResume app.
	
	IDEA: Implement a database model for the applicant's CV. 
	This model file includes the custom attribute lists (skills, hobbys, languages, etc..).
	
	Importable as: profilemodel
	
	Author: Albert Ferguson"""
from __future__ import unicode_literals
from django.db import models
from django.conf import settings 
"""
use django.conf import rather than, django.contrib.auth.models import User 
see: https://stackoverflow.com/questions/19976115/whats-the-difference-between-from-django-conf-import-settings-and-import-set 
"""
from django.utils.encoding import python_2_unicode_compatible
from .AttributeLists import Skills, Education, Languages, WorkHist

class BaseCV(models.Model):
	"""The user's profile/resume. Contains a one-to-many relationship to languages & education. """
	
	# add any direct attributes of this table below
	bio = models.CharField("What's your goal?", max_length=500, blank=True, null=True)
	created_at = models.DateField(null=True, blank=False)
	# Do not use the auto_add_now, buggy feature...see super override below: save
	edited_at = models.DateField(null=True, blank=False) 

	# add any external table references below
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
		)
	
	class Meta:
		db_table = "Base_CV"

@python_2_unicode_compatible	
class CV(BaseCV):

	skill = models.ForeignKey(Skills, related_name="CV", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Skill")
	wrkhist = models.ForeignKey(WorkHist, related_name="CV", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Work Experience")
	eduhist = models.ForeignKey(Education, related_name="CV", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Education")
	langs = models.ForeignKey(Languages, related_name="CV", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Languages")

	def __str__(self):
		return "%s's CV." % (self.user.name)

	class Meta:
		db_table = "profiles"
