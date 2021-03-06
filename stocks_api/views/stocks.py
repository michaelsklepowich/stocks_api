from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
        
    def list(self, request):
            return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request):
        return Response(json={'message': 'Listing one of the records'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request):
            return Response(json={'message': 'Deleted the record'}, status=204)
