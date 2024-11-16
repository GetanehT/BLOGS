from rest_framework.response import Response
from rest_framework.views import APIView
from .models import profile
from .serializers import profileSerializer

class ProfileList(APIView):
    def get(self, request, *args, **kwargs):
        profiles = profile.objects.all()
        serializer = profileSerializer(profiles, many=True)  # Corrected reference to 'profileSerializer'
        return Response(serializer.data)
