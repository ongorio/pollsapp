from django.contrib import admin

from polls import models


# Register your models here.
admin.site.register([
    models.Poll,
    models.Option,
    models.Response
])