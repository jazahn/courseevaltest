from django.db import models

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    YES = "Y"
    NO = "N"
    YESNO = (
        (YES, "yes"),
        (NO, "no")
    )
    TERM_CHOICES = (
        (1, "fall"),
        (2, "spring"),
        (3, "summer")
    )
    acad_year = models.IntegerField(max_length=4)
    term = models.IntegerField(max_length=1, choices=TERM_CHOICES)
    eval_course = models.CharField(max_length=1, choices=YESNO)
    eval_start = models.DateField()
    eval_end = models.DateField()
    publish_responses = models.CharField(max_length=1, choices=YESNO)
    class Meta:
        verbose_name_plural = "Courses"
    

# why does your person table have a course ID -- poorly named table
# is it an mtm or do we get the data from ldap?
# also, this should not be singular when other tables are plural
class Person(models.Model):
    COURSE_ROLE_CHOICES = (
        ("Instructor", "Instructor"),
        ("TF", "TF"),
        ("Student", "Student")
    )
    course = models.ForeignKey(Courses)
    hu_id = models.CharField(max_length=8)
    course_role = models.CharField(max_length=32, choices=COURSE_ROLE_CHOICES)
    title = models.CharField(max_length=64, blank=True)
    class Meta:
       verbose_name_plural = "People"

    
class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=64)
    text = models.CharField(max_length=1024)
    class Meta:
       verbose_name_plural = "Questions"

class Survey_Answers(models.Model):
    course = models.ForeignKey(Courses)
    question = models.ForeignKey(Questions)
    target_id = models.CharField(max_length=8)
    respondent_id = models.CharField(max_length=8)
    # TODO: make this a clob so if people ever ask for rich text we can fit it
    # assuming Oracle, max max_length is 4000
    response = models.CharField(max_length=1024)
    class Meta:
       verbose_name_plural = "Survey_Answers"
    
    