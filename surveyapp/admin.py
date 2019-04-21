from django.contrib import admin

# Register your models here.
from . models import SurveyModel

class SurveyModelAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ('name','vote_count', 'content_id')

admin.site.register(SurveyModel, SurveyModelAdmin)