from django.db import models

class Admin_Registration(models.Model):
	fname=models.CharField(max_length=100)
	mname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	dob=models.DateField(max_length=8)
	GENDER_CHOICES = (("male",'male'),("female",'female'),)
	gender=models.CharField(max_length=10,choices=GENDER_CHOICES,default="")
	aadhar=models.CharField(max_length=12)

	address=models.TextField()
	city=models.CharField(max_length=100)
	pin=models.CharField(max_length=10)
	mobile=models.CharField(max_length=10)
	photo=models.ImageField(upload_to='AdminPhotos/',default="")
	
	status=models.CharField(max_length=100,default="activated")
	last_login=models.CharField(max_length=100,default="")
	email=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100,default="")
	cpassword=models.CharField(max_length=100,default="")
	sreenpin=models.CharField(max_length=100,default="")
	csreenpin=models.CharField(max_length=100,default="")

	def __str__(self):
		return self.mname+" "+self.email

class Student_Inquiry(models.Model):
	admin_user=models.ForeignKey(Admin_Registration,on_delete=models.CASCADE,null=True,blank=True)
	
	VISA_CHOICES = (("Student Visa",'Student Visa'),("Work Visa",'Work Visa'),("PR Visa",'PR Visa'),("Dependent Visa",'Dependent Visa'),)
	visa=models.CharField(max_length=200,choices=VISA_CHOICES,default="")
	inquiry_num=models.AutoField(primary_key=True)
	inquiry_date=models.DateField(max_length=8)
	full_name=models.CharField(max_length=100)
	dob=models.DateField(max_length=8)
	CHOICES = (("male",'male'),("female",'female'),)
	gender=models.CharField(max_length=200,choices=CHOICES,default="")
	address=models.TextField(default="-")
	mobile=models.CharField(max_length=10,default="-")
	IfMarried=models.CharField(max_length=10,default="-")
	pin=models.CharField(max_length=10,default="-")
	email=models.CharField(max_length=100,default="-")
	MARRIED_CHOICES = (("YES",'YES'),("NO",'NO'),)
	married =models.CharField(max_length=200,choices=MARRIED_CHOICES,default="-")
	IfMarried=models.CharField(max_length=10,default="-")

	HSC_INS = models.CharField(max_length=200,default="-")
	HSC_YEAR = models.CharField(max_length=20,default="-")
	HSC_GRADES = models.CharField(max_length=20,default="-")
	HSC_BACK = models.CharField(max_length=20,default="-")

	DIPLOMA_INS = models.CharField(max_length=200,default="-")
	DIPLOMA_YEAR = models.CharField(max_length=20,default="-")
	DIPLOMA_GRADES = models.CharField(max_length=20,default="-")
	DIPLOMA_BACK = models.CharField(max_length=20,default="-")

	BACHOLOR_INS = models.CharField(max_length=200,default="-")
	BACHOLOR_YEAR = models.CharField(max_length=20,default="-")
	BACHOLOR_GRADES = models.CharField(max_length=20,default="-")
	BACHOLOR_BACK = models.CharField(max_length=20,default="-")

	MASTER_INS = models.CharField(max_length=200,default="-")
	MASTER_YEAR = models.CharField(max_length=20,default="-")
	MASTER_GRADES = models.CharField(max_length=20,default="-")
	MASTER_BACK = models.CharField(max_length=20,default="-")

	jobExp = models.CharField(max_length=20,default="No Experienc")

	EXAM_CHOICES = (("IELTS",'IELTS'),("TOEFL",'TOEFL'),("PTE",'PTE'),)
	IfExam = models.CharField(max_length=200,choices=EXAM_CHOICES,default="No Appeared")

	L = models.CharField(max_length=10,default="-")
	R = models.CharField(max_length=10,default="-")
	W = models.CharField(max_length=10,default="-")
	S = models.CharField(max_length=10,default="-")
	ALL = models.CharField(max_length=20,default="-")
	
	VISAFOR_CHOICES = (("AUSTRALIA",'AUSTRALIA'),("CANADA",'CANADA'),("UK",'UK'),("USA",'USA'),("OTHERS",'OTHERS'),)
	country=models.CharField(max_length=200,choices=VISAFOR_CHOICES,default="")
	
	intake = models.CharField(max_length=20,default="-")
	FieldOfStudy = models.CharField(max_length=20,default="-")
	PASSPORT_CHOICES = (("YES",'YES'),("NO",'NO'),)
	HavePassport =models.CharField(max_length=200,choices=PASSPORT_CHOICES,default="-")

	REL_CHOICES = (("AUSTRALIA",'AUSTRALIA'),("CANADA",'CANADA'),("UK",'UK'),("USA",'USA'),("OTHERS",'OTHERS'),)
	RelativesIn = models.CharField(max_length=200,choices=REL_CHOICES,default="")
	
	C_CHOICES = (("IELTS Academic",'IELTS Academic'),("IELTS Genaral",'IELTS Genaral'),("Spoken English",'Spoken English'),("PTE",'PTE'),)
	CRequired = models.CharField(max_length=200,choices=C_CHOICES,default="No Appeared")

	REFERENCE_CHOICES = (("Friend",'Friend'),("Relative",'Relative'),("News paper",'News paper'),("Google",'Google'),("Website",'Website'), ("Others",'Others'),)
	reference=models.CharField(max_length=200,choices=REFERENCE_CHOICES,default="")

	BRANCH_CHOICES = (("Surat",'Surat'),("Ankleshwar",'Ankleshwar'),)
	brance=models.CharField(max_length=200,choices=BRANCH_CHOICES,default="")