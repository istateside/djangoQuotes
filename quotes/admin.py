from django.contrib import admin

# Register your models here.
from .models import Quote, Source, Author

admin.site.register(Quote)
admin.site.register(Source)
admin.site.register(Author)