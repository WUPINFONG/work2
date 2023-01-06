from django.shortcuts import render

import hashlib

from .models import Member

from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    msg = ""
    if "email" in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        
        obj = Member.objects.filter(email=email,password=password).count()
        
        if obj > 0 :  # 表示資料表中有這個使用者，且帳密都正確
            # 建立SESSION 物件
            # 可以將值 暫時存在 伺服器端，當瀏覽器關閉時，SESSION 內的值
            # 就會不見，重開瀏覽器，就會抓不到值。
            # 打開瀏覽器時，它會主動跟伺服器端抓取一個id ，id會不同
            # 儲存在本地端電腦的，稱為 COOKIES
            
            request.session['myMail'] = email # 儲存session 資料
            request.session['isAlive'] = True
            
            return HttpResponseRedirect('/') # 指向根目錄 (首頁)
        else:
            msg = "帳密錯誤，請重新輸入"
            return render(request,'login.html',locals())
        
    else:
        if "myMail" in request.session and "isAlive" in request.session:
            return HttpResponseRedirect("/member")
        else:
            return render(request,'login.html',locals())


def logout(request):
    del request.session["isAlive"]   # 刪除 SESSION 內容
    del request.session["myMail"]
    return HttpResponseRedirect('/login')


def register(request):
    msg = ""
    
    if 'userName' in request.POST:
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['pwd']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        address = request.POST['address']
        
        #加密 SHA256
        #password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        
        # 此行是要查詢email 是否已存在的
        obj = Member.objects.filter(email=email).count() #回傳筆數
        
        if obj == 0 : # 表示這個 email 沒有註冊過
            # 新增會員資料
            Member.objects.create(name=username,sex=sex,birthday=birthday,email=email,password=password,address=address)
            msg ="恭喜你，已完成註冊！"
        
        else:
            msg = "此Email 已存在，請換一個 mail 註冊"       
                
    return render(request,'register.html',locals())    


def manage(request):
    
    # 要判斷是否已經登入了。若沒有，就導回去登入頁面
    
    if "myMail" in request.session and "isAlive" in request.session:

        msg = ''
        if "oldpwd" in request.POST:
            oldpwd = request.POST['oldpwd']
            newpwd = request.POST['newpwd']
            
            # 確認使用者輸入的舊密碼是否正確，先將二個密碼加密
            oldpwd = hashlib.sha3_256(oldpwd.encode('utf-8')).hexdigest()
            newpwd = hashlib.sha3_256(newpwd.encode('utf-8')).hexdigest()
            
            email = request.session['myMail']
            
            # 確認使用者輸入的舊密碼是否正確
            obj = Member.objects.filter(email=email,password=oldpwd).count()
            if obj > 0:
                # 更新密碼，將資料抓出來為物件
                user = Member.objects.get(email=email)
                user.password = newpwd
                user.save()
                msg = "密碼變更完成"
            else:
                msg = "舊密碼不正確，請重新輸入"

        return render(request,'manage.html',locals())
    else:
        return HttpResponseRedirect('/login')
