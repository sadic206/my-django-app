from django.shortcuts import render
from django.template import loader 
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')   

def samp(request):
    return HttpResponse('<!DOCTYPE html>'
        '<html lang="en">'
         '<head>'
      '<title>Sample page</title>'
      '<meta  charset="UTF-8">'
       
  
         '</head>'
         '<body>'
        '<h2>My Sample page</h2>'
          '<hr>'

       
         '</body>'
        '</html>')
                          


from myapp.functions.functions import handle_uploaded_file  
from myapp.forms import Student  
def index(request):  
  if request.method == 'POST':  
      
     student = Student(request.POST, request.FILES)  
       
     if student.is_valid():  
        handle_uploaded_file(request.FILES['file'])  
        return HttpResponse("File uploaded successfuly")  
  else:  
      student = Student()  
      return render(request,"index.html",{'form':student})  



from  myapp.forms import Employee  
def emp(request):  
        if request.method == 'POST':  
            employee  = Employee(request.POST)  
            if student.is_valid():  
                try:  
                    return redirect('/')  
                except:  
                    pass  
        else:  
            employee = Employee()  
        return render(request,'index.html',{'form':employee})  


class FirstMiddleware:  
    def __init__(self, get_response):  
        self.get_response = get_response  
      
    def __call__(self, request):  
        response = self.get_response(request)  
        return response 

def methodinfo(request):  
    return HttpResponse("Http request is: "+request.method) 


def getdata(request):  
    try:  
        data = Employee.objects.get(id=12)  
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
    return HttpResponse(data);

def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  

  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial); 

import csv  
      
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  

from myapp.models import Employee 
import csv  
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = Employee.objects.all()  
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.eid,employee.ename,employee.econtact])  
    return response
from reportlab.pdfgen import canvas  
def getpdf(request):  
   response = HttpResponse(content_type='application/pdf')  
   response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
   p = canvas.Canvas(response)  
   p.setFont("Times-Roman", 55)  
   p.drawString(100,700, "Hello, Javatpoint.")  
   p.showPage()  
   p.save()  
   return response  


from myproject import settings  
from django.core.mail import send_mail  
  
  
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "swadickangubo7@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  
