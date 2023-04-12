from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .forms import NameForm, CreateBioLower14, CreateBioUpper14
from .models import GetInfor, CCCD, Queue
import datetime
from datetime import timedelta
import calendar
from .generator import queuegenerator, queueextractor, stringlizing
# Create your views here.

def index(response):
    """
    if response.method == "POST":
        if response.POST.get("save"):
            na=response.POST.get('gender')
        
            return render(response, 'temps/t.html', {'text': na})
    """
    return render(response, 'temps/index.html', {})

def camera(response):
    return render(response, 'temps/category.html', {})

def dslr(response):
    return render(response, 'temps/dslr.html', {})

def mirrorless(response):
    return render(response, 'temps/mirrorless.html', {})

def login(response):
    return render(response, 'temps/login.html', {})

def canon750D(response):
    return render(response, 'temps/canon750D.html', {})

def introduction(response):
    return render(response, 'temps/introduction.html', {})

def contact(response):
    return render(response, 'temps/contact.html', {})
def container(response):
    return render(response, 'temps/container.html', {})



def tokhaithongtin(response):
    return render(response, 'temps/tokhaithongtin.html', {})
        
def ktrthongtin(response):
    return render(response, 'temps/ktrthongtin.html', {})

def tokhaiduoi14(response):
    if response.method == "POST":
        if response.POST.get("save"):

            cccd = response.POST.get('cccd')
            if CCCD.objects.filter(cccd=cccd).exists()==False:
                a=CCCD(cccd=cccd)
                a.save()

                name=response.POST.get('name')
                birth  = response.POST.get('birth')
                phonenumber = response.POST.get('phonenumber')
                gender = response.POST.get('gender')
                location = response.POST.get('location')
                guardian = response.POST.get('guardian')

                content = {
                    'name':name,
                    'birth':birth,
                    'gender':gender,
                    'phonenumber':phonenumber,
                    'location':location,
                    'guardian':guardian,
                    'cccd':cccd,
                    'text':'Successed',
                }

                c=Queue.objects.all().first()

                queuenumber,c.day,c.month,c.stt = queuegenerator(c.day,c.month,c.stt)

                b=a.getinfor_set.create(name=name,birth=birth,gender=gender,phonenumber=phonenumber,location=location,guardian=guardian,queuenumber=queuenumber)
                b.save()
                c.save()
                return render(response, 'temps/tokhaiduoi14.html', content)
        
            else:
                return render(response, 'temps/tokhaiduoi14.html', {'warning':"* CCCD đã tồn tại:"})


    return render(response, 'temps/tokhaiduoi14.html', {})

def tokhaitren14(response):
    if response.method == "POST":

        if response.POST.get("save"):

            cccd = response.POST.get('cccd')
            if CCCD.objects.filter(cccd=cccd).exists()==False:
                a=CCCD(cccd=cccd)
                a.save()

                name=response.POST.get('name')
                birth  = response.POST.get('birth')
                phonenumber = response.POST.get('phonenumber')
                gender = response.POST.get('gender')
                location = response.POST.get('location')
                #guardian = response.POST.get('guardian')

                content = {
                    'name':name,
                    'birth':birth,
                    'gender':gender,
                    'phonenumber':phonenumber,
                    'location':location,
                    #'guardian':guardian,
                    'cccd':cccd,
                    'text':'Successed',
                }

                c=Queue.objects.all().first()

                queuenumber,c.day,c.month,c.stt = queuegenerator(Queue.objects.all().first().day,Queue.objects.all().first().month,Queue.objects.all().first().stt)

                b=a.getinfor_set.create(name=name,birth=birth,gender=gender,phonenumber=phonenumber,location=location,guardian='',queuenumber=queuenumber)
                b.save()
                c.save()
                return render(response, 'temps/tokhaitren14.html', content)
        
            else:
                return render(response, 'temps/tokhaitren14.html', {'warning':"* CCCD đã tồn tại:"})

    return render(response, 'temps/tokhaitren14.html', {})

def laythongtin(response):
    if response.method == "POST":
        if response.POST.get("save"):
            cccd = response.POST.get('cccd')
            if CCCD.objects.filter(cccd=cccd).exists():
                a=CCCD.objects.filter(cccd=cccd).first()
                b=a.getinfor_set.all().first()
                content = {
                    'cccd': b.cccd,
                    'name': b.name,
                    'gender': b.gender,
                    'phonenumber': b.phonenumber,
                    'location': b.location,
                    'guardian': b.guardian,
                    'birth': str(b.birth).replace("/","-"),
                }
                return render(response, 'temps/laythongtin2.html', content)
            
            else:
                return render(response, 'temps/laythongtin.html', {'text':'CCCD nhập sai hoặc không tồn tại, vui lòng nhập lại'})

        elif response.POST.get('change')=='change':
            cccd = response.POST.get('cccd')
            a=CCCD.objects.filter(cccd=cccd).first()
            b=a.getinfor_set.all().first()

            name=response.POST.get('name')
            birth  = response.POST.get('birth')
            phonenumber = response.POST.get('phonenumber')
            gender = response.POST.get('gender')
            location = response.POST.get('location')
            guardian = response.POST.get('guardian')

            content = {
                'name':name,
                'birth':birth,
                'gender':gender,
                'phonenumber':phonenumber,
                'location':location,
                'guardian':guardian,
                'cccd':cccd,
            }

            text=[]
            
            if b.name != name:
                b.name=name
                text.append('Tên thành: '+name)
            if str(b.birth).replace("/","-") != birth:
                b.birth=birth
                birth= datetime.datetime.fromisoformat(birth).date()
                text.append('Ngày sinh thành: '+birth.strftime("%d")+'/'+birth.strftime("%m")+'/'+birth.strftime("%Y"))
            if b.phonenumber != phonenumber:
                b.phonenumber=phonenumber
                text.append('Số điện thoại thành: '+phonenumber)
            if b.gender != gender:
                b.gender=gender
                if gender == 'male':
                    text.append('Giới tính thành: Nam')
                elif gender == 'female':
                    text.append('Giới tính thành: Nữ')
            if b.guardian != guardian and guardian!= None:
                b.guardian=guardian
                text.append('Họ và tên người bảo hộ thành: '+guardian)
            if b.location != location:
                b.location=location
                text.append('Địa chỉ thành: '+location)

            leng=len(text)
            content['text']=text
            content['leng']=leng
            b.save()

            return render(response, 'temps/laythongtin2.html', content)

        elif response.POST.get('delete') == 'delete':
            cccd = response.POST.get('cccd')
            deletequeuenum=CCCD.objects.filter(cccd=cccd).first().getinfor_set.all().first().queuenumber
            deleteday, deletemonth, deletestt=queueextractor(deletequeuenum)
            endday=Queue.objects.all().first().day
            endmonth=Queue.objects.all().first().month
            endstt=Queue.objects.all().first().stt
            currentqueuenum=stringlizing(endmonth)+stringlizing(endday)+stringlizing(endstt)

            a_date = datetime.date(2022, deletemonth, deleteday)
            b_date = datetime.date(2022, endmonth, endday)

            GetInfor.objects.filter(queuenumber=deletequeuenum).first().delete()

            day_count = (b_date - a_date).days + 1
            for single_date in (a_date + timedelta(n) for n in range(day_count)):
                # print(single_date)
                temp=single_date.strftime('%m')+single_date.strftime('%d')
                i_start=1
                if single_date == a_date:
                    i_start=deletestt+1
                if single_date.weekday()==5:
                    i_end=23
                elif single_date.weekday()<5:
                    i_end=47
                    
                for i in range(i_start,i_end):
                    if GetInfor.objects.filter(queuenumber=(temp+stringlizing(i))).exists():
                        if stringlizing(i-1)=='00':
                            tempday,tempmonth,tempstt = queueextractor(newvalue)
                            newvalue=stringlizing(tempmonth)+stringlizing(tempday)+stringlizing(tempstt+1)
                        else:
                            newvalue=temp+stringlizing(i-1)

                        if temp+stringlizing(i) == currentqueuenum:
                            k=Queue.objects.all().first()
                            k.day,k.month,k.stt = queueextractor(newvalue)
                            k.save()

                        q=GetInfor.objects.filter(queuenumber=(temp+stringlizing(i))).first().cccd
                        w=q.getinfor_set.all().first()
                        w.queuenumber=newvalue
                        w.save()
                
            CCCD.objects.filter(cccd=cccd).first().delete()
       
            return render(response, 'temps/laythongtin.html', {'text':'Bạn đã xoá thông tin thành công'})

        else:
            return render(response, 'temps/laythongtin2.html', {'warning':'nhập lại2'})
        
    return render(response, 'temps/laythongtin.html', {})

def tracuu(response):
    if response.method == "POST":
        if response.POST.get("save"):
            cccd = response.POST.get('cccd')
            if CCCD.objects.filter(cccd=cccd).exists():
                a=CCCD.objects.filter(cccd=cccd).first()
                b=a.getinfor_set.all().first()
                c=b.queuenumber

                day, month, stt = queueextractor(c)

                time=0
                for i in range(int(stt)):
                    if time==220:
                        time=300
                    time+=10

                hours=7
                mins=50
                mins+=time%60
                if mins>=60:
                    mins-=60
                    hours+=1
                hours+=time//60

                content={
                    'queuenumber':b.queuenumber,
                    'day':day,
                    'month':month,
                    'stt':stt,
                    'time':str(hours)+" giờ "+str(mins),
                }
                return render(response, 'temps/thoigiannhanhochieu.html', content)

            else:
                return render(response, 'temps/tracuu.html', {'text':'CCCD nhập sai hoặc không tồn tại, vui lòng nhập lại'})

        elif response.POST.get("done") == 'done':
            return render(response, 'temps/t.html', {})

        else:
                return render(response, 'temps/tracuu.html', {'text':'false'})
        
    return render(response, 'temps/tracuu.html', {})

def thoigiannhanhochieu(response):

    return render(response, 'temps/thoigiannhanhochieu.html')