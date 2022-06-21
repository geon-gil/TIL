from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET'])
def profile(request, username):
    User_model = get_user_model()
    user = get_object_or_404(User_model, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def signout(request):
    if request.user.is_authenticated:
        User_model = get_user_model()
        user = get_object_or_404(User_model, pk=request.user.pk)
        user.delete()
        data = {
            'message': f'{user.username}님 회원탈퇴 되었습니다.'
        }
        return Response(data)