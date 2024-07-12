from .models import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class AssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'