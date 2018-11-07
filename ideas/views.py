# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from .utils.core import json_response
from .utils.core import create_idea, create_ideas
from .models import Idea

import json

def ideas(request):
    """
    /ideas

    **Overview**
        Return a list of ideas

    **Model**
        An instance of :model:`ideas.Idea`.

    **Template**
        json

    """
    ideas = Idea.objects.order_by('created_date')

    return json_response(create_ideas(ideas))

def idea_new(request):
    """
    /ideas/new

    **Overview**
        Return a dict of the idea

    **Model**
        An instance of :model:`ideas.Idea`.

    **Template**
        json

    """
    idea = Idea()
    idea.save()

    return json_response(create_idea(idea))

@csrf_exempt
def idea_delete(request):
    """
    /ideas/delete

    **Overview**
        Delete an idea by id

    **Model**
        An instance of :model:`ideas.Idea`.

    **Template**
        json

    """
    if request.method == 'DELETE':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']
            idea = Idea.objects.get(id=id)
            idea.delete()
        except KeyError:
            return HttpResponseServerError()
        else:
            return HttpResponseNotFound()

@csrf_exempt
def idea_update(request):
    """
    /idea/update

    **Overview**
        Update an idea by id

    **Model**
        An instance of :model:`ideas.Idea`.

    **Template**
        json

    """
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']
            idea = Idea.objects.get(id=id)
            idea.title = json_data['title']
            idea.body = json_data['body']
            idea.save()

            return json_response(create_idea(idea))
        except KeyError:
            return HttpResponseServerError()
        else:
            return HttpResponseNotFound()

