from django.contrib.auth.models import User, Group
from library_module.models import *
from rest_framework import viewsets
from library_module.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow to be viewed or edite
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow groups to be viewed or edite
    """    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow  to be viewed or edite
    """
    queryset = Genre.objects.all().order_by('-name')
    serializer_class = GenreSerializer
    
class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow  to be viewed or edite
    """
    queryset = Language.objects.all().order_by('-name')
    serializer_class = LanguageSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow  to be viewed or edite
    """
    queryset = Book.objects.all().order_by('-title')
    serializer_class = BookSerializer
    
class BookInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow  to be viewed or edite
    """
    queryset = BookInstance.objects.all().order_by('-status')
    serializer_class = BookInstanceSerializer
    
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow  to be viewed or edite
    """
    queryset = Author.objects.all().order_by('-first_name')
    serializer_class = AuthorSerializer
