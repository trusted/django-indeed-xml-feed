from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from .serializers import JobSerializer
from .models import Job


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # parser_classes = (XMLParser,)
    # renderer_classes = (JSONRenderer, XMLRenderer )
