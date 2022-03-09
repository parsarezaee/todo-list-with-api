from django.contrib import admin
from .models import TodoModel


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(TodoModel, TodoAdmin)