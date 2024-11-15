from django.shortcuts import render
from rest_framework.decorators import api_view
# function based api view
from django.http import Http404
from rest_framework import status
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response
# @api_view(['GET','POST'])  #non primary based
# def studentlist(request):
#     if(request.method=="GET"):  #GET Method -READ REQUEST from client
#         s=Student.objects.all()  #Reads all student records
#         stu=StudentSerializer(s,many=True)  #serialization -converts django format into json
#         return Response(stu.data,status=status.HTTP_200_OK) #returns json  response to client
#
#     elif(request.method=="POST"):
#         s=StudentSerializer(data=request.data) #converting request data in json format into django format
#
#         if s.is_valid(): #validating data
#                 s.save()  #saves the data into db table after validation
#                 return Response(s.data,status=status.HTTP_201_CREATED)
#     return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def studentdetail(request,pk):
#     try:
#         s=Student.objects.get(pk=pk) #reads a particular record matching with the value pk
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method=="GET"):
#         stu = StudentSerializer(s)  # serialization -converts django format into json
#         return Response(stu.data, status=status.HTTP_200_OK)  # returns json  response to client
#
#     elif (request.method == "PUT"):
#         s = StudentSerializer(s,data=request.data)  # converting request data in json format into django format
#
#         if s.is_valid():  # validating data
#             s.save()  # saves the data into db table after validation
#             return Response(s.data, status=status.HTTP_201_CREATED)
#     elif(request.method=="DELETE"):
#         s.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# class StudentListView(APIView): #nonprimary key based
#
#     def get(self,request):#if request.method == get it automatically calls get()
#         s = Student.objects.all()  # Reads all student records
#         stu=StudentSerializer(s,many=True)  #serialization -converts django format into json
#         return Response(stu.data,status=status.HTTP_200_OK) #returns json  response to client
#
#     def post(self,request):#if request.method == post it automatically calls post()
#         s = StudentSerializer(data=request.data)  # converting request data in json format into django format
#
#         if s.is_valid(): #validating data
#             s.save()  #saves the data into db table after validation
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import mixins,generics
# class StudentListView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView): #nonprimary key based
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request):
#          return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
# class StudentListView(generics.ListCreateAPIView): #nonprimary key based
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):#primarykey based
#
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
from rest_framework import viewsets
class StudentView(viewsets.ModelViewSet): #get,post,put,delete
      permission_classes=[IsAuthenticated,]
      queryset = Student.objects.all()
      serializer_class = StudentSerializer
#class StudentDetailView(APIView):#primarykey based
#
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(pk=pk) #reads a particular record matching with the value pk
#         except Student.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk):
#          s=self.get_object(pk)
#          stu= StudentSerializer(s)  # serialization -converts django format into json
#
#          return Response(stu.data, status=status.HTTP_200_OK)  # returns json  response to client
#
#     def put(self,request,pk):
#          s = self.get_object(pk)
#          stu = StudentSerializer(s, data=request.data)  # converting request data in json format into django format
#          if stu.is_valid():  # validating data
#                 stu.save()  # saves the data into db table after validation
#                 return Response(stu.data, status=status.HTTP_201_CREATED)
#     def delete(self,request,pk):
#          s = self.get_object(pk)
#          s.delete()
# #          return Response(status=status.HTTP_204_NO_CONTENT)
#
# class StudentDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):#primarykey based
#
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
#     def get(self,request,pk):
#          return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request, pk)
#     def delete(self,request,pk):
#         return self.destroy(request, pk)
from django.db.models import Q
class SearchView(APIView):

      def get(self, request):
            query = request.query_params.get('search')  # query_parameter  --{'search': 'carrot'}
            if query:
                  s= Student.objects.filter(Q(name__icontains=query) | Q(place__icontains=query))
                  stu = StudentSerializer(s, many=True)
            return Response(stu.data, status=status.HTTP_200_OK)

#search by name
class SearchName(APIView):

      def get(self, request):
            query = request.query_params.get('name')  # query_parameter  --{'name': 'Arun'}
            if query:
                  s= Student.objects.filter(name=query)
                  stu = StudentSerializer(s, many=True)
            return Response(stu.data, status=status.HTTP_200_OK)
from django.contrib.auth.models import User
from students.serializers import UserSerializer
class RegisterView(viewsets.ModelViewSet):
      queryset = User.objects.all()
      serializer_class = UserSerializer



class LogoutAPIView(APIView):
      permission_classes=[IsAuthenticated]
      def get(self,request):
            self.request.user.auth_token.delete()
            return Response({'msg':"logout successfully"},status=status.HTTP_200_OK)








