from django.core.cache import cache
from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from ideas.models import Idea

import json

def json_response(data):
    """
    **Overview**
        Return a json response

    **Parameters**
        data

    """
    json_converted = json.dumps(data)

    response = HttpResponse(json_converted, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'

    return response

def create_idea(idea):
    """
    **Overview**
        Return an idea dict

    **Parameters**
        idea

    """
    return {
        'id': idea.id,
        'created_date': str(idea.created_date),
        'updated_date': str(idea.updated_date),
        'title': idea.title,
        'body': idea.body,
    }

def create_ideas(ideas):
    """
    **Overview**
        Return a list of ideas

    **Parameters**
        ideas

    """
    ideas_list = []

    for idea in ideas:
        ideas_list.append(create_idea(idea))

    return ideas_list
