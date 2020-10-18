from django.urls import path
from applications.bond.views import BondViewSet, BondDetail, api_root, LegalEntityViewSet, LegalEntityDetail

urlpatterns = [
        path('bonds/', BondViewSet.as_view(), name='bond-list'),
        path('bonds/<int:pk>/', BondDetail.as_view(), name='bond-detail'),
        path('legal_entities/', LegalEntityViewSet.as_view(), name='legal_entity-list'),
        path('legal_entities/<pk>/', LegalEntityDetail.as_view(), name='legal_entity-details'),
        path('', api_root, name='api-root'),
    ]