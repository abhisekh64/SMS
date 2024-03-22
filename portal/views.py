from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Employee

# Create your views here.
def create(request):
     if request.method == 'POST':
        e_name = request.POST.get("name")
        e_email = request.POST.get("email")
        e_department = request.POST.get("department")
        e_position = request.POST.get("position")
        e_salary = request.POST.get("salary")
        print(e_name,e_email,e_department,e_position,e_salary)
        employee =  Employee(name=e_name,email=e_email,department = e_department,position = e_position, salary = e_salary )
        employee.save()
        return render(request,"pages/create.html")

     else:
        return render(request,"pages/create.html")

       


def update(request, id):
    object = get_object_or_404(Employee, pk=id)
    context = {"obj": object}
    print(context)
    if request.method == 'POST':
        object.name=request.POST.get("name")
        object.email=request.POST.get("email")
        object.department=request.POST.get("department")
        object.position=request.POST.get("position")
        object.position=request.POST.get("salary")
        object.save()
        return redirect("/")
    
    return render(request, "pages/update.html", context)



# Create your views here.
def delete(request,id):
    try:
     object = Employee.objects.get(id=id)
     object.delete()
    except:
    
       pass
    return redirect("/")


def view(request):
    employes =  Employee.objects.all()
    return render(request,"pages/view.html",{"emps":employes})