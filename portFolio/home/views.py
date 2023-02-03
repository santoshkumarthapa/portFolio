from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class myProfile(View):

    def get(self, request):
        return HttpResponse({"message":"good to go"}, content_type="html/json")