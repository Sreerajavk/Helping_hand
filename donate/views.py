from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.


#return to home page
def index(request):
    return redirect('home/')



#home page view
def home(request):




    return render(request , 'home.html')





def send_mail(request , user):

    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        donor_obj = donor_details.objects.get(user=user)
        donor_obj.email_status = True
        donor_obj.save()
        #login(request, user)
        return redirect('/login')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@csrf_exempt
def signup(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        print(first_name , last_name , username , email , mobile , password)

        user = User.objects.create_user(first_name = first_name, last_name=last_name, username = username, email = email, password = password)
        user.save()


        if user:
            #success
            donor_obj = donor_details(user = user , email_status=False , phone=mobile , points=0)
            donor_obj.save()

            #sending email
            send_mail(request , user)

            return JsonResponse({'status' : '200' , 'id' : user.id})

        return JsonResponse({'status' : '400'})


    if request.user.is_authenticated:
        return render(request , 'home.html')
    return  render( request , 'signup.html')

@csrf_exempt
def signup_inst(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        account_name = request.POST.get('account_name')
        account_number = request.POST.get('account_number')
        ifsc = request.POST.get('ifsc')

        print(first_name , last_name , username , email , mobile , password)

        user = User.objects.create_user(first_name = first_name, last_name=last_name, username = username, email = email, password = password)
        user.save()


        if user:
            #success
            inst_obj = institution_details(user = user , email_status=False , phone=mobile ,account_holder=account_name , account_number = account_number , ifsc=ifsc)
            inst_obj.save()

            #sending email
            send_mail(request , user)

            return JsonResponse({'status' : '200' , 'id' : user.id})

        return JsonResponse({'status' : '400'})


    if request.user.is_authenticated:
        return render(request , 'home.html')
    return  render( request , 'signup-instit.html')





@csrf_exempt
def login_fn(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password=password)
        if user:
            user_obj = User.objects.get(username = username)
            donor_obj = donor_details.objects.get(user = user_obj.id )

            print(donor_obj.email_status)

            if donor_obj.email_status:
                return JsonResponse({'status' : '200'})
            else:

                return JsonResponse({'status' : '300'})
        else:
            return JsonResponse({'status': '400'})


        print(username , password)

    else:

        return render(request , 'login.html')


@csrf_exempt
def mobile_login(requsest):



    if requsest.method == 'POST':

        username = requsest.POST.get('username')
        password = requsest.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            user_obj = User.objects.get(username=username)
            donor_obj = donor_details.objects.get(user=user_obj.id)
            print(donor_obj)
            print(donor_obj.email_status)

            if donor_obj.email_status:
                response = {}
                response['first_name']  = user_obj.first_name
                response['last_name']  = user_obj.last_name
                response['username'] = user_obj.username
                response['mobile'] = donor_obj.phone
                response['email'] = user_obj.email

                response['id'] = user_obj.id
                response['status'] = 200

                print(response)

                return JsonResponse(response)
            else:
                response = {}
                response['first_name'] = user_obj.first_name
                response['last_name'] = user_obj.last_name
                response['username'] = user_obj.username
                response['mobile'] = donor_obj.phone
                response['email'] = user_obj.email
                response['status'] = 300
                response['id'] = user_obj.id
                return JsonResponse(response)
        else:
            return JsonResponse({'status': 400})




@csrf_exempt
def mobile_signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = str(request.POST.get('password'))

        print(first_name, last_name, username, email, mobile, password)

        try:

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                       password=password)
            user.save()

            if user:
                #success
                donor_obj = donor_details(user = user , email_status=False , phone=mobile , points=0)
                donor_obj.save()

                #sending email
                print('sending email')
                send_mail(request , user)
                print('mail send')
                print({'status' : '200'})
                return JsonResponse({'status' : 200})
        except:
            return JsonResponse({'text': 'alredy registerd' , 'status' : 500})

        return JsonResponse({'status' : 400})


@csrf_exempt
def add_post(request):

    if request.method == 'POST':


        if request.user.is_authenticated:
            title = request.POST.get('title')
            body = request.POST.get('body')

            post_obj = post.objects.create(user = request.user.username , title = title , body=body , is_satisfied=False , rating=0)
            post_obj.save()

        else:
            return redirect('/login')

    else:

        return  render(request , 'issue.html')


@csrf_exempt
def view_post(request):

    if request.method == 'POST':

        post_obj = post.objects.all()
        all_post=[]

        for i in post_obj:

            dic ={}
            dic['id'] = i.id
            dic['title'] = i.title
            dic['body'] = i.body
            dic['user'] = i.user
            dic['is_satisfied'] = i.is_satisfied
            dic['rating'] = i.rating

            all_post.append(dic)

        return JsonResponse({'data' : all_post})




    return render(request , 'forum.html')


@csrf_exempt
def email_status(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        print(username)
        user_obj = User.objects.get(username = username)
        donor_obj = donor_details.objects.get(user = user_obj.id)

        if donor_obj.email_status:
            return JsonResponse({'status' : 200})

        else:

            return JsonResponse({'status': 400})