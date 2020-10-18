from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView

from applications.bond.models import Bond, LegalEntity
from applications.bond.serializers import BondSerializer, LegalEntitySerializer
from applications.bond.permissions import IsOwnerReadOnly


class BondViewSet(ListCreateAPIView):
    """
       Return a list of all the Bonds that belong to
       the authenticated user, with optional filtering.

       Returns all Bonds for Admin Users

       Create Bond instance or instances
    """
    serializer_class = BondSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isin', 'lei', 'legal_name']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Bond.objects.all()
        return Bond.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BondDetail(RetrieveAPIView):
    """
    Retrieve a bond instance.
    """
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = [IsOwnerReadOnly]


class LegalEntityViewSet(ListCreateAPIView):
    """
       Return a list of all the Legal Entities that belong to
       the authenticated user, with optional filtering.

       Create Legal Entity instance or instances
    """
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['legal_name', 'legal_jurisdiction', 'status']


class LegalEntityDetail(APIView):
    """
    Retrieve a Legal Entity instance.
    """

    def get_object(self, pk):
        try:
            return LegalEntity.objects.get(pk=pk)
        except LegalEntity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        legal_entity = self.get_object(pk)
        serializer = LegalEntitySerializer(legal_entity)
        return Response(serializer.data)


# Move to api root app
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'bonds': reverse('bond-list', request=request, format=format),
        'legal_entities': reverse('legal_entity-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })
