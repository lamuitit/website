from datetime import timedelta, date
import calendar

def queuegenerator(day,month,stt):
    main_database={
        'day':day,
        'month':month,
        'stt':stt,
    }

    check=False
    currenttoday = date.today()
    currentmonth=currenttoday.strftime('%m')
    currentday=currenttoday.strftime('%d')

    current={
		'month':int(currentmonth),
		'day':int(currentday),
	} 

    if date(2022,main_database['month'],main_database['day'])<=date(2022,current['month'],current['day']):
        main_database['month']=int((date(2022,current['month'],current['day'])+timedelta(days=1)).strftime('%m'))
        main_database['day']=int((date(2022,current['month'],current['day'])+timedelta(days=1)).strftime('%d'))
        main_database['stt']=0
        check=True

    day=main_database['day']
    month=main_database['month']
    stt=main_database['stt']

    d = date(2022, month, day)
    
    stt+=1
    if (d.weekday()==5) and stt>=23:
        stt=1
        d+= timedelta(days=1)
    elif (d.weekday()<5) and stt>=47:
        stt=1
        d+= timedelta(days=1)

    if d.weekday()==6:
        d+= timedelta(days=1)

    database={
		"day":int(d.strftime("%d")),
		"month":int(d.strftime("%m")),
		"stt":stt,
	}

    if stt<10:
        stt='0'+str(stt)
    else:
        stt=str(stt)
    if month<10:
        month='0'+str(month)
    else:
        month=d.strftime("%m")
    if int(d.strftime("%d"))<10:
        day='0'+str(int(d.strftime("%d")))
    else:
        day=d.strftime("%d")

    if check:
        main_database['stt']=1
    else:
        main_database['stt']+=1

    return month+day+stt, main_database['day'], main_database['month'], main_database['stt']

def queueextractor(c):
    j=0;day="";month="";stt=""
    for i in c:
        j+=1
        if j<=2:
            month+=i
        elif 2<j and j<=4:
            day+=i
        else:
            stt+=i
    return int(day), int(month), int(stt)

def stringlizing(s):
    if s<10:
        s='0'+str(s)
    else:
        s=str(s)
    return s