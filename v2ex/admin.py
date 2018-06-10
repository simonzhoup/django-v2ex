from django.contrib import admin

from v2ex.models import Topic, Category, Tag, UserProfile

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(UserProfile)