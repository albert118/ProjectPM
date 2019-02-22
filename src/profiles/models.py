""" Python implemenation of BaseProfile. BaseProfile extends auth_user, Business allows
	internall tracking of associated businesses.
	Based on original JavaApp development and adapted for webuse with MySQL.
	Importable as: models.py
	
	Author: Albert Ferguson"""

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings

class BaseProfile(models.Model):
	# note: the relation must be to the base user defined here!
	# not to the abstract model defined in usermodels.py, otherwise and E300, E307 error will arrise!!
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
		)
	slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
	birth = models.DateField(null=True)
	picture = models.ImageField(
		"Profile picture", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
		)
	bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
	email_verified = models.BooleanField("Email verified", default=False)

	class Meta:
		abstract = True

@python_2_unicode_compatible
class Profile(BaseProfile):
	""" This is the publicly accessible Profile model. Forms access this. """
	def __str__(self):
		return "{}'s profile".format(self.user)

@python_2_unicode_compatible
class Business(models.Model):
	"""For internal use, allows business to be added to our db so we can keep track of stat's."""
	name = models.CharField("Business Name", max_length=80, primary_key=True)
	phone = models.CharField("Business Phone", max_length=10, null=True)
	mobile = models.CharField("Optional Contact Mobile", max_length=10, null=True, blank=True)
	cont_name = models.CharField(max_length=50, null=True, blank=True)
	picture = models.ImageField(
		"Profile picture", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
	)
	is_active = models.BooleanField()
	date_joined = models.DateField(editable=False)
	edited_at = models.DateField()
	bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return "{}".format(self.name)

	class Meta:
		db_table = "businesses"

class Address(models.Model):
	"""Address model. """
	street = models.CharField(max_length=50, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	suburb = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=10, blank=True, null=True)
	street_number = models.IntegerField(blank=True, null=True)
	unit_number = models.IntegerField(blank=True, null=True)
	postcode = models.IntegerField(blank=True, null=True)
	business = models.ForeignKey(
		Business, on_delete=models.CASCADE, related_name="Addresses"
		)
	
	class Meta:
		db_table = "addresses"
