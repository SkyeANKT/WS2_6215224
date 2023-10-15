from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect, HttpResponse
import json


def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)


def movie_list(request):
    list = [{'id': x.movie_id, 'name': x.movie_name, 'year': str(x.year)}
            for x in Movie.objects.filter(void=0).order_by('-created_time')]
    # qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def movie_detail(request):
    name = request.GET.get('movie_name')
    list = [{
        'id': x.movie_id,
        'name': x.movie_name,
        'year': str(x.year),
        'genre': x.genre,
        'description': str(x.description),
        'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
        'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
    }
        for x in Movie.objects.filter(movie_name=name).filter(void=0).order_by('-created_time')]

    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')