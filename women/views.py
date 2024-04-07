from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.
class WomenAPIView(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer