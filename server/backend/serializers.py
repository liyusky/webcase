from rest_framework import serializers
from backend.models import *

class AmountDetailListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        detailMap = {}
        detailList = []
        for data in validated_data:
            detailMap[data['kind']] = data

        for detail in instance:
            if detail is not None:
                detailList.append(self.child.update(detail, detailMap[detail.kind]))

        return detailList

class AmountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountDetail
        fields = ('kind', 'amount', 'year')
        list_serializer_class = AmountDetailListSerializer

    def create(self, validated_data):
        detail = AmountDetail.objects.create(**validated_data)
        return detail

class AmountTotalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmountTotal
        fields = ('kind', 'amount', 'year')

    def create(self, validated_data):
        total = AmountTotal.objects.create(**validated_data)
        return total
