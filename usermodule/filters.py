
import django_filters

from employermodule.models import *


class postjobfilter(django_filters.FilterSet):
    class Meta:

        model = emplor_postjob
        fields= '__all__'
        
        
        
