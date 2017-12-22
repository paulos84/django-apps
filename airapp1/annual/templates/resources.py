from import_export import resources
from .models import AnnualMean

class PersonResource(resources.ModelResource):
    class Meta:
        model = AnnualMean