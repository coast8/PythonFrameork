from django.contrib import admin
from yawdadmin import admin_site
from lib.tagging.models import Tag, TaggedItem
from lib.tagging.forms import TagAdminForm

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

admin_site.register(TaggedItem)
admin_site.register(Tag, TagAdmin)




