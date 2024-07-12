from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    last_login_date = models.DateField(null=True, blank=True)

    CHOICES_ROLE = (
        ('Учитель', 'Учитель'),
        ('Ученик', 'Ученик'),
    )
    role = models.CharField(choices=CHOICES_ROLE, max_length=50)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor_id = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    CHOICES_LEVEL = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый')
    )
    level = models.CharField(choices=CHOICES_LEVEL, max_length=100)


class Module(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    video_url = models.FileField(upload_to='video/', null=True, blank=True)
    duration = models.IntegerField(default=0)


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress = models.CharField(max_length=100)


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    submitted = models.DateTimeField(max_length=100)


class Grade(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    grade = models.SmallIntegerField(default=0)
    feedback = models.TextField()


class Certificate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.IntegerField(default=0)
    issued = models.DateTimeField()
    certificate_url = models.URLField(null=True, blank=True, max_length=100)
