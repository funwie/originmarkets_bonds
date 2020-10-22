from rest_framework import status
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer


from applications.bond.mapper import get_mapped_legal_entity
from applications.bond.models import Bond, LegalEntity
from utils import web_client


class LegalEntitySerializer(ModelSerializer):

    class Meta:
        model = LegalEntity
        fields = ['lei', 'legal_name', 'legal_address', 'legal_jurisdiction', 'status', 'created']


class BondSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    legal_entity = LegalEntitySerializer(read_only=True)

    class Meta:
        model = Bond
        fields = ['isin', 'size', 'currency', 'maturity', 'lei', 'legal_name', 'owner', 'created', 'legal_entity']
        read_only_fields = ['legal_name']

    def create(self, validated_data):
        if 'lei' in validated_data:
            legal_entity = self.get_legal_entity(validated_data['lei'])
            if legal_entity:
                validated_data['legal_entity'] = legal_entity
                validated_data['legal_name'] = legal_entity.legal_name
        bond = Bond.objects.create(**validated_data)
        return bond

    def get_legal_entity(self, pk):
        try:
            return LegalEntity.objects.get(pk=pk)
        except LegalEntity.DoesNotExist:
            url = f'https://leilookup.gleif.org/api/v2/leirecords?lei={pk}'
            response = web_client.get_json(url)
            if response.status_code == status.HTTP_200_OK:
                mapped_legal_entity = get_mapped_legal_entity(response.data)
                return LegalEntity.objects.create(**mapped_legal_entity)
        return None


