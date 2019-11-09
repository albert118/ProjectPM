""" Python implemenation of the user profile/resume class for BetterResume app.
    
    IDEA: Implement a database model for the applicant's profile. 
	This model file includes the education & languages related models.
	Importable as: profilemodel.py
    
    Author: Albert Ferguson"""

from django.db import models
from django.contrib.auth.models import User 
# note: the relation must be to the base user defined here!
# not to the abstract model defined in usermodels.py, otherwise and E300, E307 error will arrise!!

class Profile(models.Model):
	"""The user's profile/resume. Contains a one-to-many relationship to languages & education. """
	bio = models.CharField(max_length=500, blank=True)
	created_at = models.DateField(editable=False)
	edited_at = models.DateField() # Do not use the auto_add_now, buggy feature...see super override below: save
	#user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="Profile")
	
	def __str__(self):
		return self.User.first_name + " " + self.User.last_name

	def save(self, *args, **kwargs):
		"""Circumvent the auto_add arguments. On save, update time-stamps."""
		from django.utils import timezone
		if not self.id:
			created_at = timezone.now()
		edited_at = timezone.now()

	class Meta:
		db_table = "profiles"

class Education(models.Model): 
	"""Definition of the education history model. """
	edu = models.CharField(max_length=25, null=True, blank=False)
	startDate = models.DateField(null=True, blank=False)
	endDate = models.DateField(null=True, blank=False)
	profile = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name="EducationHistory")

	class Meta:
		db_table = "education_history"
    
	def __str__(self):
		"""Return the current education location. """
		return self.edu

class Languages(models.Model):
	"""The applicant's known languages. """
	language = models.CharField(max_length=15, null=True, blank=True)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="Languages")

	class Meta:
		db_table = "languages"

	def __str__(self):
		return self.language

class WorkHist(models.Model):
	"""The applicant's work experience/history. TODO: Add questionaire results..."""
	business = models.CharField(max_length=120)
	review = models.CharField(max_length=500, null=False, blank=True)
	rating = models.IntegerField()
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="WorkHistory")

	class Meta:
		db_table = "work_history"

	def __str__(self):
		return self.language
