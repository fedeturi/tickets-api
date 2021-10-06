from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer
import requests
from pprint import pprint
import json
from random import randrange, choice
import random_word


class ApiConstants():

    def __init__(self):
        """
        Constants belonging to SpaceX Public Trello Board:
        https://trello.com/b/Vxv7dECV/space-x
        """
        self.API_KEY = 'f01a5dd3b4b4cfb10c9893039f5e4f26'
        self.API_TOKEN = '5f62066bda0b8e999f3928f9d7fee45dc18009d207b75417eb81ac8d9c058d83'
        self.BOARD_ID = '615cdf992792ff64b2a8f3c3'
        self.TODO_LIST_ID = '615ce6867fd14f52ab38e4fb'


class NewTicket(APIView):

    def post(self, request):

        ticket_type = request.POST.get('type')

        if ticket_type == 'issue':
            response = self.load_issue_ticket(request.POST)
        elif ticket_type == 'bug':
            response = self.load_bug_ticket(request.POST)
        elif ticket_type == 'task':
            response = self.load_task_ticket(request.POST)
        else:
            response = None

        return Response(response if response else None)

    def load_bug_ticket(self, request_params):
        """
        Create a new BUG Card using POST endpoint of Trello API

        :param request_params: HTTP Request Parameters Dict
        :type request_params: Dic
        :returns: HTTP Response
        :rtype: Http Response
        """

        constants = ApiConstants()

        # Get a list of all available members to assign this task
        URL = f'https://api.trello.com/1/boards/{constants.BOARD_ID}/members'
        query = {
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
        }

        response = requests.request(
            "GET",
            URL,
            params=query
        )

        members = response.json()

        assigned_member = choice(members).get('id')

        # Get a list fo all available labels in this board, and use BUG label
        URL = f'https://api.trello.com/1/boards/{constants.BOARD_ID}/labels'
        query = {
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
        }

        response = requests.request(
            "GET",
            URL,
            params=query
        )

        labels = response.json()

        BUG_TAG_ID = next(item for item in labels if item["name"] == "Bug").get('id')

        # Create BUG Card
        r = random_word.RandomWords()
        word = r.get_random_word()
        number = randrange(0, 10001)

        title = f'bug-{word}-{number}'
        description = request_params.get('description')

        URL = f'https://api.trello.com/1/cards'
        query = {
            'name': title,
            'desc': description,
            'pos': 'bottom',
            'idList': constants.TODO_LIST_ID,
            'idMembers': assigned_member,
            'idLabels': BUG_TAG_ID,
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
            }

        response = requests.request(
           "POST",
           URL,
           params=query
        )

        return response.json()

    def load_task_ticket(self, request_params):
        """
        Create a new TASK Card using POST endpoint of Trello API

        :param request_params: HTTP Request Parameters Dict
        :type request_params: Dic
        :returns: HTTP Response
        :rtype: Http Response
        """

        constants = ApiConstants()

        # Get a list fo all available labels in this board, and use BUG label
        URL = f'https://api.trello.com/1/boards/{constants.BOARD_ID}/labels'
        query = {
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
        }

        response = requests.request(
            "GET",
            URL,
            params=query
        )
        labels = response.json()

        MAINTENANCE_TAG_ID = next(item for item in labels if item["name"] == "Maintenance").get('id')
        RESEARCH_TAG_ID = next(item for item in labels if item["name"] == "Research").get('id')
        TEST_TAG_ID = next(item for item in labels if item["name"] == "Test").get('id')

        tags = {
            'Maintenance': MAINTENANCE_TAG_ID,
            'Research': RESEARCH_TAG_ID,
            'Test': TEST_TAG_ID
        }

        URL = f'https://api.trello.com/1/cards'
        title = request_params.get('title')
        category = request_params.get('category')
        tag = tags.get(category)

        query = {
            'name': title,
            'pos': 'bottom',
            'idList': constants.TODO_LIST_ID,
            'idLabels': tag,
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
        }

        response = requests.request(
            "POST",
            URL,
            params=query
        )

        return response.json()

    def load_issue_ticket(self, request_params):
        """
        Create a new ISSUE Card using POST endpoint of Trello API

        :param request_params: HTTP Request Parameters Dict
        :type request_params: Dic
        :returns: HTTP Response
        :rtype: Http Response
        """

        constants = ApiConstants()

        title = request_params.get('title')
        description = request_params.get('description')

        URL = f'https://api.trello.com/1/cards'
        query = {
            'name': title,
            'desc': description,
            'pos': 'bottom',
            'idList': constants.TODO_LIST_ID,
            'key': constants.API_KEY,
            'token': constants.API_TOKEN
            }

        response = requests.request(
           "POST",
           URL,
           params=query
        )

        return response.json()
