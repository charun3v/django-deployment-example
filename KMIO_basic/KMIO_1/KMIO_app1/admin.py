from django.contrib import admin
from .models import PatientID, PatientName, PatientAge, UserProfileInfo


admin.site.register(PatientName)
admin.site.register(PatientID)
admin.site.register(PatientAge)
admin.site.register(UserProfileInfo)
#admin.register(PatientID)
#admin.register(PatientAge)
#admin.register(PatientName)





# Register your models here.
