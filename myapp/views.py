import datetime
from django.core.paginator import Paginator

from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.

def login_page(request):
    return render(request,'login.html')

def login_post(request):
    uname = request.POST['Email']
    pwrd = request.POST['Password']
    print("Helloooooo")
    if login.objects.filter(username=uname, password=pwrd).exists():
        lg = login.objects.get(username=uname, password=pwrd)
        if lg.type == 'admin':
            request.session['id'] = lg.id
            print("LOgIN ID",request.session['id'])
            return redirect(home)
        else:
            print(type)
            return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")
    else:
        print(type)
        return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")

def home(request):
    return render(request,'admin/index.html')

# Course manage



def add_course(request):
    return render(request,'admin/short-course-create.html')

def addcourse_post(request):
    title = request.POST['title']
    sub = request.POST['subtit']
    descr = request.POST['desc']
    amt = request.POST['amt']
    qualif = request.POST['qual']
    img = request.FILES['filefield']
    stat = request.POST['status']

    res = course()
    res.cname = title
    res.subtitle = sub
    res.description = descr
    res.fee = amt
    res.qualification=qualif
    res.status =stat

    fs = FileSystemStorage()
    s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
    fn = fs.save(s, img)

    res.image=fs.url(s)

    res.save()



    return redirect(view_course)

def view_course(request):
    res = course.objects.all()
    items_per_page = 3
    paginator = Paginator(res, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }

    # return render(request, 'admin/short-course-view.html', context)
    return render(request,'admin/demoview.html',context)




def courseactive(request,id):
    res = course.objects.filter(id=id).update(status='Enable')
    return view_course(request)

def courseainctive(request,id):
    res = course.objects.filter(id=id).update(status='Disable')
    return view_course(request)



def deletecourse(request,id):
    res = course.objects.get(id=id).delete()
    return redirect(view_course)

def edit_course(request,id):
    res = course.objects.get(id=id)
    return render(request,'admin/editcourse.html',{'data':res})


def edit_coursepost(request):
    courseid = request.POST['cid']
    title = request.POST['title']
    sub = request.POST['subtit']
    descr = request.POST['desc']
    amt = request.POST['amt']
    qualif = request.POST['qual']
    stat = request.POST['status']

    if 'filefield' in request.FILES:
        photo = request.FILES['filefield']
        if photo.name != '':
            fs = FileSystemStorage()
            s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
            fn = fs.save(s, photo)
            res = course.objects.filter(pk=courseid).update(cname=title, subtitle=sub, qualification=qualif, fee=amt,image=s, status=stat, description=descr)
            return HttpResponse(
                '''<script>alert('Update Successfully');window.location="/myapp/view_course/"</script>''')

        else:
            res = course.objects.filter(pk=courseid).update(cname=title, subtitle=sub, qualification=qualif, fee=amt,status=stat, description=descr)
            return HttpResponse(
                '''<script>alert('Update Successfully');window.location="/myapp/view_course/"</script>''')

    else:
        res = course.objects.filter(pk=courseid).update(cname=title, subtitle=sub, qualification=qualif, fee=amt, status=stat,
                                                  description=descr)
        return HttpResponse('''<script>alert('Update Successfully');window.location="/myapp/view_course/"</script>''')




def viewprofile(request):
    return render(request,'admin/profile.html')


def changepswrd_post(request):
    cp = request.POST['cp']
    np = request.POST['np']
    cnp = request.POST['cnp']
    if np == cnp:
        if login.objects.filter(password=cp, id=request.session['id']).exists():
            res = login.objects.filter(id=request.session['id']).update(password=np)
            return redirect(login_page)
        else:
            return HttpResponse("Confirm password does not match")
    else:
        return HttpResponse("Current password does not match")

def jqry_dataview(request):
    res = course.objects.all()
    l=[]

    for i in res:
        l.append({'id':i.id,'title':i.cname,'subtit':i.subtitle,'quali':i.qualification,'feee':i.fee,'descr':i.description,'statu':i.status,'img':str(i.image)})

    return JsonResponse({'status': 'ok','data':l})


def demoview(request):
    return render(request,'admin/ajaxview.html')



def searchcourse(request,a):
    print("---a", a)

    res = course.objects.filter(cname__icontains=a)
    print(res)
    l=[]
    for i in res:
        obj = {'id':i.id,'title':i.cname,'subtit':i.subtitle,'quali':i.qualification,'feee':i.fee,'descr':i.description,'statu':i.status,'img':str(i.image)}
        l.append(obj)
        print(l,"LIST")

        if len(l) > 0:
            return JsonResponse({"status": "ok", "data": l})
        else:
            return JsonResponse({"status": "no"})



def AjaxDelete(request,id):
    res = course.objects.get(id=id)
    res.delete()
    return JsonResponse({'status': 'ok'})