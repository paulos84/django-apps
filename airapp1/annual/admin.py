from django.contrib import admin
from .models import AnnualMean
from import_export.admin import ImportExportModelAdmin
from .models import AnnualMean, DailyMean


@admin.register(AnnualMean)
class AnnualMeanAdmin(ImportExportModelAdmin):
    pass

@admin.register(DailyMean)
class DailyMeanAdmin(ImportExportModelAdmin):
    pass
