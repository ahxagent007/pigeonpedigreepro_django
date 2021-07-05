from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from FirebaseUtill.FirebaseConfig import configFirebase
from urllib3.exceptions import HTTPError

# Create your views here.
def Home(request):
    context = {}
    request.session['redirect'] = ''
    return render(request, 'home/index.html', context)

def About(request):
    context = {}
    return render(request, 'home/about_us.html', context)

def Demo(request):
    context = {}
    return render(request, 'home/demo.html', context)

def Price(request):
    context = {}
    return render(request, 'home/price.html', context)

def Contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

def Pedigree(request):
    context = {}
    return None

@csrf_exempt
def Login(request):
    #request.session['redirect'] = '/Auction/Event/' + str(id)
    try:
        if request.session['UserID']:
            return redirect(request.session['redirect'])
    except:
        print('No user exist')

    if request.method == 'GET':
        return render(request, 'home/login.html', context={})

    if request.method == 'POST':
        email = request.POST.get('Email')
        pw = request.POST.get('Pass')

        reCaptcha = request.POST.get('g-recaptcha-response')
        if reCaptcha == '':
            print('NONE RECAPTCHA')
            return render(request, 'home/login.html', context={'error': 'Please enter reCAPTCHA correctly'})
        else:
            print('Recaptcha '+reCaptcha)
            secretKey = "6Lf-adIZAAAAAGUx8wfuvs1UrL0eKwnx5NMLX2p9"

            url_recaptcha = 'https://www.google.com/recaptcha/api/siteverify?secret={0}&response={1}'.format(secretKey, reCaptcha)
            recap_response_server = requests.get(url_recaptcha).content

            json_response_google = json.loads(recap_response_server)

            print(json_response_google)

            if json_response_google['success']:
                print('reCAPTCHA match')

                # print(email+' : '+ pw)
                firebase = configFirebase()

                # Get a reference to the auth service
                auth = firebase.auth()

                try:
                    # Log the user in
                    user = auth.sign_in_with_email_and_password(email, pw)
                    print(user, flush=True)

                    user_id = user['localId']
                    idToken = user['idToken']

                    db = firebase.database()
                    user_details = db.child('Registration').order_by_key().equal_to(user_id)
                    details = list(user_details.get().val().values())[0]

                    print(details, flush=True)
                    # print(details['address'])

                    request.session['UserID'] = user_id
                    request.session['UserName'] = details['name']
                    request.session['idToken'] = idToken
                    request.session['UserEmail'] = details['email']
                    request.session['UserPhone'] = details['phone']
                    request.session['UserAddress'] = details['address']

                    return redirect(request.session['redirect'])

                except HTTPError as e:
                    print('Exception : ' + str(e.args))
                    return render(request, 'home/login.html', context={'error': 'Wrong Email or Password'})
            else:
                return render(request, 'home/login.html', context={'error':'Wrong reCAPTCHA'})


def Logout(request):
    session.pop('UserID', None)
    session.pop('UserName', None)
    session.pop('idToken', None)
    session.pop('UserEmail', None)
    session.pop('UserPhone', None)
    session.pop('UserAddress', None)

    return render(request, 'home/home.html', context={})

def Registration(request):
    try:
        if request.session['UserID']:
            return redirect(request.session['redirect'])
    except:
        print('No user exist')

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pigeon = request.form['pigeon']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        address = request.form['address']
        ip = request.remote_addr

        print(name, email, phone, pigeon, pass1, pass2)

        reCaptcha = request.form['g-recaptcha-response']
        if reCaptcha == '':
            print('NONE RECAPTCHA')
            return render_template('login.html', error='Please enter reCAPTCHA correctly')
        else:
            print('Recaptcha ' + reCaptcha)
            secretKey = "6Lf-adIZAAAAAGUx8wfuvs1UrL0eKwnx5NMLX2p9"

            url_recaptcha = 'https://www.google.com/recaptcha/api/siteverify?secret={0}&response={1}'.format(secretKey,
                                                                                                             reCaptcha)
            recap_response_server = requests.get(url_recaptcha).content

            json_response_google = json.loads(recap_response_server)

            print(json_response_google)

            if json_response_google['success']:
                print('reCAPTCHA match')

                firebase = configFirebase()

                if pass1 == pass2:
                    try:
                        # Get a reference to the auth service
                        auth = firebase.auth()
                        # register the user in
                        new_reg = auth.create_user_with_email_and_password(email, pass1)
                        # print(type(reg_user))

                        user_id = new_reg['localId']

                        print(name, email, phone, pigeon, pass1, pass2, user_id)

                        user = {
                            'name': name,
                            'email': email,
                            'address': address,
                            'phone': phone,
                            'pg': pigeon,
                            'ip': ip
                        }

                        db = firebase.database()
                        db.child('Registration').child(user_id).set(user)
                        return redirect(url_for('Home:Login'))

                    except HTTPError as e:
                        print('registration Exception : ' + str(HTTPException), flush=True)
                        print(json.loads(e.args[1])['error']['message'])
                        return render(request, 'home/registration.html', context={'error': str(json.loads(e.args[1])['error']['message'])})

    return render(request, 'home/registration.html', context={})

def privacy_policy(request):
    return None
