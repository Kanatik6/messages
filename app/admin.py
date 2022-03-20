from django.contrib import admin
from app.models import (Message,AboutUs,HomePage, Comments,
                        OurServices, QuickProjectStart)

admin.site.register(Message)
admin.site.register(AboutUs)
admin.site.register(HomePage)
admin.site.register(Comments)
admin.site.register(OurServices)
admin.site.register(QuickProjectStart)
