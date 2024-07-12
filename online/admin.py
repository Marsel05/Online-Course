from .models import *
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Module)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Certificate)
admin.site.register(Grade)
admin.site.register(Enrollment)
admin.site.register(Lesson)


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ("name",'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }