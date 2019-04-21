from __future__ import division
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Sum

from . models import SurveyModel

class SurveyView(TemplateView):

	def save_in_database(self, request, *args, **kwargs):

		movie_content_id=request.POST.getlist('movie')
	  	for id in movie_content_id:
	  		result=SurveyModel.objects.get(content_id=id)
	  		vote_count = int(result.vote_count)
		  	result.vote_count=vote_count+1
		  	result.save()
		  	return self.redirect_trendPage(request)

	def redirect_trendPage(self, request, *args, **kwargs):
		
		template_name="trendPage.html"
		total_vote = SurveyModel.objects.aggregate(Sum('vote_count'))
		total_vote = total_vote['vote_count__sum']
		get_survey_result = SurveyModel.objects.all()
		report=[]

		for each_movie in get_survey_result:
			movieDetails={}
			movieDetails['name'] = each_movie.name
			movieDetails['vote_count'] = each_movie.vote_count
			movieDetails['year'] = each_movie.year
			vote_percentage = float((each_movie.vote_count*100)/total_vote)
			movieDetails['vote_percentage'] = round(vote_percentage,3)
			report.append(movieDetails)

   		return render(request, template_name, {"movieDetails":report})

	def get(self, request, *args, **kwargs):

		#check availability of cookies
		if 'firstvisit' in request.COOKIES:
			return self.redirect_trendPage(request)

		else:
			template_name="home.html"
			movieDetails=SurveyModel.objects.all()
			response=render(request,template_name,{"movieDetails":movieDetails})
			response.set_cookie('firstvisit', 'yes')
			#for testing the cookie, uncomment the below line
			# it will delete the cookie. so when you visit the url it will leads you to the home page
			# not to the trendpage.html
			#response.delete_cookie('firstvisit', 'yes')
			return response


	def post(self, request, *args, **kwargs):
		return self.save_in_database(request)


	