from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'orientation_rating')


admin.site.register(Feedback, FeedbackAdmin)
