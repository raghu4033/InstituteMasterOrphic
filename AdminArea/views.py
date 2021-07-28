from django.shortcuts import render,redirect
from django.conf import settings
from .models import Admin_Registration,Student_Inquiry
from django.core.mail import BadHeaderError,send_mail
from datetime import datetime
from django.utils import timezone

def index(request):
	return render(request,'Login/admin_login.html')

def admin_login(request):
	if request.method=="POST":
		admin_email=request.POST['admin_email']
		admin_password=request.POST['admin_password']
		try:
			admin_user=Admin_Registration.objects.get(email=admin_email,password=admin_password)
			if admin_user.status == 'activated':
				request.session['admin_email']=admin_user.email
				request.session['mname']=admin_user.mname
				request.session['imageurl']=admin_user.photo.url
				return redirect('AdminArea:AdminDashboard')
			else:
				FailedMsg="Your Login is Not activated"
				return render(request,'Login/admin_login.html',{'FailedMsg':FailedMsg})
		except:
			FailedMsg="Encorect Email or Password"
			return render(request,'Login/admin_login.html',{'FailedMsg':FailedMsg})
	else:
		return render(request,'Login/admin_login.html')
	return render(request,'Login/admin_login.html')

def AdminDashboard(request):
	return render(request,'AdminArea/AdminDashboard.html')

def Users(request):
	return render(request,'AdminArea/Users.html')

def InstituteDetailes(request):
	return render(request,'AdminArea/InstituteDetailes.html')

def AddAdminUser(request):
	return render(request,'AdminArea/AddAdminUser.html')

def EnrollStudentInquiry(request):
	if request.method=="POST":
		visa=request.POST['service']
		inquiry_date=request.POST['date']
		full_name=request.POST['full_name']
		dob=request.POST['dob']
		gender=request.POST['gender']
		address=request.POST['address']
		mobile=request.POST['mobile_number']
		pin=request.POST['PinCode']
		email=request.POST['email']
		married= request.POST['married']
		IfMarried = request.POST['IfMarried']

		HSC_INS =request.POST['HSC_INS']
		HSC_YEAR =request.POST['HSC_YEAR']
		HSC_GRADES =request.POST['HSC_GRADES']
		HSC_BACK =request.POST['HSC_BACK']

		DIPLOMA_INS =request.POST['DIPLOMA_INS']
		DIPLOMA_YEAR =request.POST['DIPLOMA_YEAR']
		DIPLOMA_GRADES =request.POST['DIPLOMA_GRADES']
		DIPLOMA_BACK =request.POST['DIPLOMA_BACK']

		BACHOLOR_INS =request.POST['BACHOLOR_INS']
		BACHOLOR_YEAR =request.POST['BACHOLOR_YEAR']
		BACHOLOR_GRADES =request.POST['BACHOLOR_GRADES']
		BACHOLOR_BACK =request.POST['BACHOLOR_BACK']

		MASTER_INS =request.POST['MASTER_INS']
		MASTER_YEAR =request.POST['MASTER_YEAR']
		MASTER_GRADES =request.POST['MASTER_GRADES']
		MASTER_BACK =request.POST['MASTER_BACK']

		jobExp =request.POST['jobExp']
		IfExam =request.POST['IfExam']
		L =request.POST['L']
		R =request.POST['R']
		W =request.POST['W']
		S =request.POST['S']
		ALL =request.POST['ALL']
		country=request.POST['country']
		intake =request.POST['intake']

		FieldOfStudy =request.POST['FieldOfStudy']
		HavePassport =request.POST['HavePassport']
		RelativesIn =request.POST['RelativesIn']
		CRequired =request.POST['CRequired']
		reference=request.POST['reference']
		brance=request.POST['brance']
		
		try:
			Student_Inquiry.objects.create(visa=visa,inquiry_date=inquiry_date,full_name=full_name,dob=dob,gender=gender,address=address,mobile=mobile,IfMarried=IfMarried,pin=pin,email=email,married =married,HSC_INS =HSC_INS,HSC_YEAR =HSC_YEAR,HSC_GRADES =HSC_GRADES,HSC_BACK =HSC_BACK,DIPLOMA_INS =DIPLOMA_INS,DIPLOMA_YEAR =DIPLOMA_YEAR,DIPLOMA_GRADES =DIPLOMA_GRADES,DIPLOMA_BACK =DIPLOMA_BACK,BACHOLOR_INS =BACHOLOR_INS,BACHOLOR_YEAR =BACHOLOR_YEAR,BACHOLOR_GRADES =BACHOLOR_GRADES,BACHOLOR_BACK=BACHOLOR_BACK,MASTER_INS =MASTER_INS,MASTER_YEAR =MASTER_YEAR,MASTER_GRADES =MASTER_GRADES,MASTER_BACK =MASTER_BACK
,jobExp =jobExp,IfExam = IfExam,L =L,R =R,W =W,S =S,ALL =ALL,country=country,intake =intake,FieldOfStudy =FieldOfStudy,HavePassport =HavePassport,RelativesIn =RelativesIn,CRequired =CRequired,reference=reference,brance=brance)
			msg="Student Inquery Registered Successefully"
			subject="Thanks for visiting Kalaveethi Institute"
			website="https://kalaveethi.com/"
			booklate="https://kalaveethi.com/courses/kalaveethibook/"
			message=f"Hi {full_name}\n \nThank you for reaching out to Kalaveethi Institue Of Design. I’m Trupal, your admissions counselor. I look forward to working with you. Please feel free to text me here or my colleagues at  if you have any questions. \n \n \n Phone: +91 8160892915 \n Website: {website} \n \nDownload Booklate:{booklate}"
			
			# client = Client(settings.TWILIO['TWILIO_ACCOUNT_SID'],settings.TWILIO['TWILIO_AUTH_TOKEN'])
			# client.api.messages.create(to=f"+91{mobile_number}",from_=settings.TWILIO['TWILIO_NUMBER'],body=message)

			rec=[email,]
			email_from=settings.EMAIL_HOST_USER
			send_mail(subject,message,email_from,rec)

			SuccessMsg="Student Inquery Successefully Added"
			return render(request,'AdminArea/EnrollStudentInquiry.html',{'SuccessMsg':SuccessMsg})
		except Exception as e:
			print(e)
			FailedMsg="Student Inquery Added Failed!"
			return render(request,'AdminArea/EnrollStudentInquiry.html',{'FailedMsg':FailedMsg})
	else:
		return render(request,'AdminArea/EnrollStudentInquiry.html')

def InquiryLists(request):
	StudentInquiryList = Student_Inquiry.objects.all().order_by('-inquiry_num')
	return render(request,'AdminArea/InquiryLists.html',{'StudentInquiryList':StudentInquiryList})

def AdminProfile(request):
	return render(request,'AdminArea/AdminProfile.html')

def AdminChangePassword(request):
	return render(request,'AdminArea/AdminChangePassword.html')

def AdminLockScreen(request):
	return render(request,'AdminArea/AdminLockScreen.html')

def admin_logout(request):
	try:
		del request.session['admin_email']
		return render(request,'Login/admin_login.html')
	except:
		return render(request,'Login/admin_login.html')
	