from rest_framework import generics
from myapp.models import Dog, Breed
from myapp.serializers import DogSerializer, BreedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ApiRoot(APIView):
    def get(self,request, format=None):
        return Response({
            'Intro': "Welcome to the Dog API!",
            'Creator': "Nourin",
            'dogs': reverse('dog-list', request=request, format=format),
            'breeds': reverse('breed-list', request=request, format=format)
        })

class AllBreed(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class SingleBreed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class AllDog(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class SingleDog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer