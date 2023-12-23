from django.contrib import admin
from .models import Task

admin.site.site_header = "Todo App"
admin.site.index_title = "TODO"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'user', 'title_length')
    list_per_page = 10
    actions = ['complete_task', 'uncomplete_task']

    @admin.display(description="title length: ")
    def title_length(self, task: Task):
        return f"length: {len(task.title)}"
    
    @admin.action(description="Mark selected tasks as completed")
    def complete_task(self, request, queryset):
        queryset.update(completed=True)

    @admin.action(description="Mark selected tasks as uncompleted")
    def uncomplete_task(self, request, queryset):
        queryset.update(completed=False)