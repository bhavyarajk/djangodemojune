from students.models import Student
from rest_framework import serializers
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):

          class Meta:
              model=Student
              fields=['name','age','place','id']

class UserSerializer(serializers.ModelSerializer):
    #password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password','first_name','last_name','email']

    def create(self,validated_data): #after validation validated_data ie deserialized data is sent to create() function
        user=User.objects.create_user(username=validated_data['username'],
                                      password=validated_data['password'],
                                      email=validated_data['email'],
                                      first_name=validated_data['first_name'],
                                      last_name=validated_data['last_name'])
        return user



