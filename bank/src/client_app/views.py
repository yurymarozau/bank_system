from client_app.models import Client
from client_app.serializers import (ClientCreateSerializer,
                                    ClientDetailsSerializer,
                                    ClientShortDetailsSerializer,
                                    ClientUpdateSerializer)
from rest_framework import permissions, viewsets
from client_app.permissions import (IsClientManagerAddClient,
                                    IsClientManagerChangeClient,
                                    IsClientManagerDeleteClient,
                                    IsClientManagerViewClient)



class ClientViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new client.
    destroy:
        Delete a client.
    retrieve:
        Get the specified client.
    list:
        Get a list of all clients.
    update:
        Update a client.
    partial_update:
        Update a client.
    '''

    def get_queryset(self):
        querysets_dict = {
            'create': Client.objects.all(),
            'destroy': Client.objects.all(),
            'retrieve': Client.objects.all(),
            'list': Client.objects.all(),
            'update': Client.objects.all(),
            'partial_update': Client.objects.all(),
        }
        queryset = querysets_dict.get(self.action)
        return queryset.distinct()

    def get_serializer_class(self):
        serializers_dict = {
            'create': ClientCreateSerializer,
            'retrieve': ClientDetailsSerializer,
            'list': ClientShortDetailsSerializer,
            'update': ClientUpdateSerializer,
            'partial_update': ClientUpdateSerializer,
        }
        serializer_class = serializers_dict.get(self.action)
        return serializer_class

    def get_permissions(self):
        base_permissions = [permissions.IsAuthenticated, IsClientManagerViewClient]
        permissions_dict = {
            'create': [IsClientManagerAddClient],
            'destroy': [IsClientManagerDeleteClient],
            'retrieve': [],
            'list': [],
            'update': [IsClientManagerChangeClient],
            'partial_update': [IsClientManagerChangeClient],
        }
        base_permissions += permissions_dict.get(self.action, [])
        return [permission() for permission in base_permissions]
