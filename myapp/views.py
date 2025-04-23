from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import regfrom
from.models import reg
from .forms import coursefrom
from .models import course
from .forms import subjectfrom
from .models import subject
from .models import paper
from .forms import paperfrom
from .forms import resultfrom
from .models import resultmodel
from .models import course, subject, reg

# Create your views here.
def home(request):
    return render(request,"index.html")
def adminportal(request):
    return render(request,"adminportal.html")
def regg(request):
    if request.method == 'POST':
        form = regfrom(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Registration successful!")
            return redirect("/myapp/login")
    else:
        form = regfrom()
    return render(request, "reg.html", {"form": form})

def admin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['pass']
        if name=='bhola' and password=='12345':
            # view_all=reg.objects.all()
            # return render(request,"view.html",{"view_all":view_all})
            return render(request,"adminportal.html")
        else:
            # return HttpResponse("Invalid admin....try again")
            return render(request,"admin.html",{"error":"invalid password or name  try again...."})
    return render(request,"admin.html")

def view(request):
    view_all=reg.objects.all()
    return render(request,"view.html",{"view_all":view_all})

def courseview(request):
    form=course.objects.all()

    return render(request,"adcourseview.html",{"form":form})
    # return render(request,"course_view.html",{"form":form})

def courseview2(request):
    form=course.objects.all()
    return render(request,"course_view.html",{"form":form})
def courses(request):
    if request.method=='POST':
        form=coursefrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/courses')
        else:
            return render(request,"addcourse.html",{"form":form})
    else:
        form = coursefrom()
        return render(request, "addcourse.html", {"form": form})
 

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        catch = reg.objects.filter(name=name, password=password)
        if catch:
            course_name = course.objects.all()
            # sub_view=course_name.sub.filter('cid')
            name=reg.objects.get(name=name)

            return render(request, "student.html", {
                "course_name": course_name,
                "name": name,
                # 'sub_view':sub_view,
            })
        else:
            return render(request, "login.html", {"error": "Invalid name or password try again..."})
    return render(request, "login.html")
def coursesub(request,course_id,id):
        # name='bhola'
        course_name = course.objects.filter(id=course_id)
        name=reg.objects.get(id=id)
        return render(request, "student.html", {
                # "course_name": course_name,
                "name": name,
                'selected':course_name,
            })

def sub(request):
    if request.method=='POST':
        form=subjectfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/myapp/sub")
        else:
             return render(request,"subject.html",{"form":form})
    else:
        form=subjectfrom()
        return render(request,"subject.html",{'form':form})
def subview(request):
    sub_view=subject.objects.all()
    return render(request,"adminsub.html",{"sub_view":sub_view})
def addpaper(request):
    sb=subject.objects.all()
    pa=None
    if request.method=='POST':
        form=paperfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/paperview')
        # pa=paper(
        #     question=request.POST.get('question'),
        #     option1=request.POST.get('option1'),
        #     option2=request.POST.get('option2'),
        #     option3=request.POST.get('option3'),
        #     option4=request.POST.get('option4'),
        #     answer=request.POST.get('answer'),
        # )
        # pa.save()
    else:
        form=paperfrom()
    return render(request,"addpaper.html",{'sb':sb,"pa":pa,"form":form})

def paperview(request):
    papers=paper.objects.all().order_by('subject')
    questions={}
    for pa in papers:
        if pa.subject not in questions:
            questions[pa.subject]=[]
        questions[pa.subject].append(pa)
    return render(request,"paperview.html",{'questions':questions})
def edit(request,id):
    ed=paper.objects.get(id=id)
    return render(request,"editpaper.html",{"ed":ed})
def editsub(request,id):
    ed=subject.objects.get(id=id)
    return render(request,"editsub.html",{"ed":ed})
def updatesub(request,id):
    ed=subject.objects.get(id=id)
    ed.sub_name=request.POST['sub_name']
    ed.shor_name=request.POST['shor_name']
    ed.save()
    return render(request,"adminsub.html",{"ed":ed})
def delete(request,id):
    de=paper.objects.get(id=id)
    de.delete()
    return redirect("/myapp/paperview",{"de":de})
def deletesub(request,id):
    de=subject.objects.get(id=id)
    de.delete()
    return redirect("/myapp/subview")
def update(request,id):
    ed=paper.objects.get(id=id)
    ed.question=request.POST['question']
    ed.option1=request.POST['option1']
    ed.option2=request.POST['option2']
    ed.option3=request.POST['option3']
    ed.option4=request.POST['option4']
    ed.answer=request.POST['answer']
    ed.save()
    return render(request,"editpaper.html",{"ed":ed})

def viewpaper(request):
    su=subject.objects.all()
    pa=paper.objects.all()
    return render(request,"paperview.html",{"pa":pa,'su':su})


def exam(request):
    if request.method=='POST':
        course_id=request.POST.get('cid')
        subject_name=request.POST.get('sid')
        subjectmodel=subject.objects.get(sub_name=subject_name)
        name=request.POST.get('name')
        name=reg.objects.get(name=name)
        nn=paper.objects.filter(course_id=course_id,subject_id=subjectmodel.id)
        return render(request, "exam.html" ,{"nn":nn, 'name':name ,'course_id':course_id ,'subject_id':subjectmodel.id})


def result(request):
    if request.method == 'POST':
        course_id=request.POST.get('course_id')
        subject_id = request.POST.get('subject_id')
        if not subject_id:
            return HttpResponse("Subject ID is missing", status=400)

        try:
            sub_name = subject.objects.get(id=subject_id).sub_name

        except subject.DoesNotExist:
            return HttpResponse("Invalid Subject ID", status=400)
        
        try:
            course_name=course.objects.get(id=course_id).course_name
        except course.DoesNotExist:
            return HttpResponse("invalid course id")
        

        name=request.POST.get('name')
        student = reg.objects.filter(name=name).first()
        if student:
            student_name=student.name
        else:
            student_name = "Anonymous"

        questions = paper.objects.filter(course_id=course_id,subject_id=subject_id)
        score = 0

        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer:
                if user_answer == question.answer:  
                    score += 1

        total_questions = questions.count()
        result_percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        return render(request, "result.html", {
            'score': score,
            'total_questions': total_questions,
            'result_percentage': result_percentage,
            'student_name': student_name,
            'subject_id': subject_id,
            'subject_name': sub_name,
            'course_name':course_name,
        })
    return redirect('/myapp/exam')
def examresult(request):
    if request.method=='POST':
        # form=resultfrom(request.POST)
        # if form.is_valid():
            # form.save()
        name=request.POST.get('student_name')
        re=resultmodel(
            # student_name=request.POST.get('student_name'),
            student_name=request.POST.get('student_name'),
            course_name=request.POST.get('course_name'),
            subject_id=request.POST.get('subject_id'),
            subject_name=request.POST.get('subject_name'),
            score=request.POST.get('score'),
            total_questions=request.POST.get('total_questions'),
            result_percentage=request.POST.get('result_percentage'),
        )
        re.save()
        return redirect(f'/myapp/sturesult/{name}')
         
    else:
            return render(request,"result.html",)
def viewresult(request):
    re=resultmodel.objects.all()
    return render(request,"viewresult.html",{'re':re})


def sturesult(request,name):
    # if request.method == 'POST':
        # Get the student's name from the POST request
        # student_name = request.POST('student_name')
        student_results = resultmodel.objects.filter(student_name=name)


        if not student_results.exists():
            return HttpResponse(f"No results found for student: {name}", status=404)
        # student_results = resultmodel.objects.get(student_name=name)
       
        return render(request, "sturesult.html", {'student_results': student_results, 'student_name': name})
    

