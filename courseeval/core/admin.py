from django.contrib import admin
from courseeval.core.models import Courses, Person, Questions, Survey_Answers

admin.site.register(Courses)
admin.site.register(Person)
admin.site.register(Questions)
admin.site.register(Survey_Answers)