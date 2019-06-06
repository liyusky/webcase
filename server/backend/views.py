import random

from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.response_content import ResponseContent
from backend.serializers import AmountDetailSerializer, AmountTotalSerializer
from backend.models import AmountDetail, AmountTotal


CurrentYear = 1900
yearMark = 0
CurrentMonthAmountList = None
GoodsKind = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

class AmountDetailView(APIView):
    def get(self, request, *args, **kwargs):
        response = ResponseContent(code=200, description=10001)
        state = status.HTTP_200_OK

        global CurrentYear
        global CurrentMonthAmountList
        global GoodsKind

        detailDataList = []
        for kind in GoodsKind:
            detailDataList.append({
                'kind': kind,
                'amount': random.randint(0, 3000),
                'year': CurrentYear
            })

        response.data = detailDataList
        CurrentMonthAmountList = detailDataList
        CurrentYear += 1

        try:
            details = AmountDetail.objects.all()
            serializer = None
            if AmountDetail.objects.count() > 0:
                serializer = AmountDetailSerializer(details, data=detailDataList, many=True)
            else:
                serializer = AmountDetailSerializer(data=detailDataList, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                response.refresh(code=500, description=12002, error=serializer.errors)
                state = status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            response.refresh(code=500, description=12001, error=e.__str__())
            state = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response.content(), status=state)


class AmountTotalView(APIView):

    def get(self, request, *args, **kwargs):
        response = ResponseContent(code=200, description=10002)
        state = status.HTTP_200_OK

        try:
            total = AmountTotal.objects.order_by('-year')[:100]
            serializer = AmountTotalSerializer(total, many=True)
            response.data = serializer.data
        except Exception as e:
            response.refresh(code=500, description=12003, error=e.__str__())
            state = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response.content(), status=state)


    def post(self, request, *args, **kwargs):
        response = ResponseContent(code=200, description=10003)
        state = status.HTTP_200_OK

        global CurrentYear
        global yearMark
        global CurrentMonthAmountList

        if not AmountTotal.objects.filter(year=CurrentYear).exists() and (yearMark != CurrentYear):
            yearMark = CurrentYear
            serializer = AmountTotalSerializer(data=CurrentMonthAmountList, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                response.refresh(code=500, description=12004, error=serializer.errors)
                state = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            response.description = 10004

        return Response(response.content(), status=state)
