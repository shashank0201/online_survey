from __future__ import unicode_literals


from django.db import models

# Create your models here.
class SurveyModel(models.Model):
	""" Define the table for survey content """

	name=models.CharField(max_length = 255, blank=False, null=False)
	content_id = models.CharField(primary_key=True, max_length = 255, blank = False, null = False)
	vote_count=models.IntegerField(default='0', editable=False, blank=False, null=False)
	year=models.IntegerField(blank=False, null=False)

	def __str__(self):
		return self.name