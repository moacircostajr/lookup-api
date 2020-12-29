from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User
from cash.api.serializers import CashSerializer
from cash.models import Cash


class CashViewSet(ModelViewSet):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        username = self.request.user  # fazer a busca pelo token ?
        queryset = User.objects.filter(username__exact=username)
        company = queryset[0].id_company
        return Cash.objects.filter(id_company=company)

    def destroy(self, request):
        return Response(status=status.HTTP_403_FORBIDDEN)
