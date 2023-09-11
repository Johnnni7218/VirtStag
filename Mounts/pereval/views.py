from .serializers import *
from rest_framework import viewsets


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializers_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializers_class = LevelSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializers_class = PhotoSerializer


class MountViewSet(viewsets.ModelViewSet):
    queryset = Mount.objects.all()
    serializers_class = MountSerializer


