from django.contrib import admin
from . models import Task, Solution , Mark
# Register your models here.


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at' , 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # list_editable = ('is_published',)
    list_filter = ('id',)


@admin.register(Solution)
class Solution(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id',)
    search_fields = ('id',)
#
#
@admin.register(Mark)
class Mark(admin.ModelAdmin):
    list_display = ('id', 'solution', 'mark', 'comment')
    list_display_links = ('mark', )
    search_fields = ('mark',)
