from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Job


class JobSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'