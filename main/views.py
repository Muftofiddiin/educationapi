from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.generics import CreateAPIView , ListCreateAPIView , UpdateAPIView


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



@api_view(['GET'])
def get_banner_view(request):
    banner = Banner.objects.last()
    serialized_data = BannerSerializer(banner).data
    return Response(serialized_data)

@api_view(['GET'])
def get_about_view(request):
    about = About.objects.all()
    serialized_data = AboutSerializer(about , many= True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_univs_view(request):
    univs = Universities.objects.all().order_by('-id')
    serialized_data = UniversitiesSerializer(univs , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_facs_view(request):
    facs = Faculties.objects.all().order_by('-id')
    serialized_data = FacultiesSerializer(facs , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_student_view(request):
    student = Student.objects.all()
    serialized_data = StudentSerializer(student , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_comms_view(request):
    comms = Comments.objects.all()
    serialized_data = CommentsSerializer(comms , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_unidetails_view(request):
    unidetails = Uni_Details.objects.all()
    serialized_data = UniDetailsSerializer(unidetails , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_profile_view(request):
    profile = Profile.objects.all()
    serialized_data = ProfileSerializer(profile , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_punivs_view(request):
    punivs = P_Universities.objects.all()
    serialized_data = PUniversitiesSerializer(punivs , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_assistent_view(request):
    assistent = Assistent.objects.all()
    serialized_data = AssistentSerializer(assistent , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_econtract_view(request):
    econtr = Econtract.objects.all()
    serialized_data = EcontractSerializer(econtr , many= True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_statistics_view(request):
    statistics = Statistics.objects.all()
    serialized_data = StatisticsSerializer(statistics , many= True).data
    return Response(serialized_data)



def search(request):
    query = request.GET.get('q', '')
    universities = Universities.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(rating__icontains=query) | Q(cost__icontains=query))
    return render(request , {'universities': universities})

@api_view(['GET'])
def get_univcab_view(request):
    univcab = UnivCab.objects.all()
    serialized_data = UnivCabSerializer(univcab , many= True).data
    return Response(serialized_data)


