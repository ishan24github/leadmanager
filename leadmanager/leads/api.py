from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset  , allow to make CRUD api

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()  # queryset attribute , that exact name
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
