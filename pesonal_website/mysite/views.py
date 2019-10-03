from django.shortcuts import render

def Home(request):
    return render(request, 'mysite/home.html')
def DataSceience(request):
    return render(request, 'mysite/ads.html')
def AboutUs(request):
    return render(request, 'mysite/aboutus.html')
def AmazonWebServices(request):
    return render(request, 'mysite/aws.html')
def Blog(request):
    return render(request, 'mysite/blog.html')
def BigDataAnalytics(request):
    return render(request, 'mysite/bda.html')
def ContactUs(request):
    return render(request, 'mysite/contactus.html')
def Corporate(request):
    return render(request, 'mysite/corporate.html')
def DigitalMarketing(request):
    return render(request, 'mysite/dm.html')
def ClassRoomLED(request):
    return render(request, 'mysite/led.html')
def LiveOnline(request):
    return render(request, 'mysite/liveol.html')
def OurServies(request):
    return render(request, 'mysite/ourcourses.html')
def Reviews(request):
    return render(request, 'mysite/reviews.html')
def SummerCamp(request):
    return render(request, 'mysite/summercamp.html')
def Workshop(request):
    return render(request, 'mysite/workshop.html')