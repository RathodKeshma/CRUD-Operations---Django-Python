from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import BlogUser
from .serializers import BlogUserSerializer
from .BlogUser import BlogUserForm

def home(request):
    return render(request, 'Blog_posts/home.html')



class BlogUserView(APIView):
    def get(self, request):
        print(request.data)
        return Response("Query successsfully")



    def createUser(request, id=0):
        if request.method == "GET":
            if id==0: # for create
                form = BlogUserForm()
            else: # for update
                user= BlogUser.objects.get(pk=id)
                form = BlogUserForm(instance=user)
            return render(request, 'Blog_posts/post_form.html', {'form': form})
        else:
            if id==0:
                form = BlogUserForm(request.POST)
            else: # for update
                user = BlogUser.objects.get(pk=id)
                form = BlogUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
            return redirect('/list')

    def deleteUser(request, id):
        user = BlogUser.objects.get(pk=id)
        user.delete()
        return redirect('/list')

    def listUser(request):
        #queryset = BlogUser.objects.all()
        #context = {}
        #context['user_list'] = queryset

        context = {'user_list': BlogUser.objects.all()}
        return render(request, 'Blog_posts/post_list.html', context)

    def updateUser(request, pk):
        queryset = get_object_or_404(BlogUser, pk=pk)
        serializer = BlogUserSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return redirect('listUser')
        return render(request, 'Blog_posts/post_form.html', {'form': serializer})
