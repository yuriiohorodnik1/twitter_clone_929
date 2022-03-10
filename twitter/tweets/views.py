from django.http import HttpResponse

from .models import Tag, Tweet


def get_all_twits(request):
    tweets = Tweet.objects.all()
    return HttpResponse(tweets[1].text)
