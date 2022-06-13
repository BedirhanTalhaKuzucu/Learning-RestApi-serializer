from dataclasses import field
from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now



# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField()

#     def create(self, validated_dat):
#         return Student.objects.create(**validated_dat)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name',instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'number', 'days_since_joined',]
        # fields= '__all__'

    def validate_number(self, value):
        """
        Check that the blog post is about Django.
        """
        if value  > 1000 :
            raise serializers.ValidationError("number must be below 1000")
        return value
    
    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days


class PathSerializer(serializers.ModelSerializer):

    ogrenci = StudentSerializer(many = True)
    # ogrenci = serializers.StringRelatedField(many = True)
    # ogrenci = serializers.PrimaryKeyRelatedField(many = True,  read_only=True)
    


    
    class Meta:
        model = Path
        fields= '__all__'



