from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json
from .forms import MyprofileForm

# Create your views here.

def is_json(mydata):
    try:
        json.loads(mydata)
        valid = True
    except Exception as e:
        valid = False
    return valid


@method_decorator(csrf_exempt, name='dispatch')
class myProfile(View):

    def get(self, request):
        return HttpResponse(json.dumps({"message": "good to go"}), content_type="application/json")

    def post(self, request):
        my_data = request.body
        if not is_json(my_data):
            return HttpResponse(json.dumps({"message":"unformatted json"}), status=403)
        my_data = json.loads(my_data)
        form = MyprofileForm(my_data)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({"message": "resource Created successful"}))
        if form.errors:
            print(form.errors)
            return HttpResponse(json.dumps({"message": "unformatted json"}), status=400)
