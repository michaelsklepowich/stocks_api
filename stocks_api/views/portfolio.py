from ..models.schemas import PortfolioSchema, StockSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.view import view_config
from pyramid.response import Response
from ..models import Portfolio, stock
import requests
import json

from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):
        """ class based view for our portfolio model,
            class methods not formatted currently and only return basic json and response statuses
        """

        def list(self, request):
            return Response(json={'message': 'list of all portfolios:'}, status=200)

        def create(self, request):
            return Response(json={'message': 'created new portfolio'}, status=201)

        def destroy(self, request, id):
            return Response(json={'message': 'portfolio successfully destroyed'}, status=204)


class StocksAPIView(APIViewSet):

    def list(self, request):
        return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request):
        return Response(json={'message': 'Listing one of the records'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request):
        return Response(json={'message': 'Deleted the record'}, status=204)


class CompanyAPIView(APIViewSet):
    """ this class based view is for the company model which inherits from pyramid's APIViewSet and which currently does nothing
    """

    def retrieve(self, request, id=None):
        """ this retrieve method will return a single company based on the id parameter
        """
        return Response(json={'message': f'successfully retrieved comapny: {id}'}, status=200)
