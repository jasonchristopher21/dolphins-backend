from django.contrib import admin

from api.models import (
    Client,
    Results,
    ClientInsight
)

# Register your models here.
admin.site.register(Client)
admin.site.register(Results)
admin.site.register(ClientInsight)