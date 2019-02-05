""" The extended profile/applicant skills.
    
    IDEA: Every user has unique skills, add them to their porfolio! TODO: include options for
	porfolio plugin to further extend this.
    
    Importable as: skills.py
    
    Author: Albert Ferguson"""

from django.db import models
import os
import inspect
from profilemodel import Profile

class Skills(models.Model):
    """"Add skill and validated fields to db. """
    skill = models.CharField(max_length=200, blank=True)
    validated = models.BooleanField()
    profile = models.ForeignKey(Profile, related_name="skills")

    class Meta:
        db_table = "skills"

    def __str__(self):
        return self.skill
    # TODO: Add validation as in tmp/attributes but for database
