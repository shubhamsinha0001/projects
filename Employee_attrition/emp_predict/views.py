from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'home.html')
def predict(request):
	global response
	age=int(request.GET["Age"])
	bt=int(request.GET["BusinessTravel"])
	dr=int(request.GET["DailyRate"])
	dept=int(request.GET["Department"])
	Dfh=int(request.GET["DistanceFromHome"])
	edt=int(request.GET["Education"])
	ef=int(request.GET["EducationField"])
	yac=int(request.GET["YearsAtCompany"])
	dict1={} 
	dict1={"Age":age,"BusinessTravel":bt,"DailyRate":dr,"Department":dept,"DistanceFromHome":Dfh,"Education":edt,"EducationField":ef,"YearsAtCompany":yac}
	#return HttpResponse(str(dict1))
	"""stage 1-->collect data"""
	import pandas as pd
	df=pd.read_csv("C:/Users/VVS/Desktop/Employee_attrition/Employee_attrition/emp_predict/datasetemp.csv")
	import sklearn.preprocessing as pp
	lb=pp.LabelBinarizer()
	df.Gender=lb.fit_transform(df.Gender)
	df.Attrition=lb.fit_transform(df.Attrition)
	x=pd.read_csv("C:/Users/VVS\Desktop/Employee_attrition/Employee_attrition/emp_predict/datasetemp.csv",header=0, usecols=(0,2,3,4,5,6,7,31));
	y=y=df['Attrition']
	x['EducationField'].replace('Life Sciences',1, inplace=True)
	x['EducationField'].replace('Medical',2, inplace=True)
	x['EducationField'].replace('Marketing', 3, inplace=True)
	x['EducationField'].replace('Other',4, inplace=True)
	x['EducationField'].replace('Technical Degree',5, inplace=True)
	x['EducationField'].replace('Human Resources', 6, inplace=True)
	x['Department'].replace('Research & Development',1, inplace=True)
	x['Department'].replace('Sales',2, inplace=True)
	x['Department'].replace('Human Resources', 3, inplace=True)
	x['BusinessTravel'].replace('Travel_Rarely',1, inplace=True)
	x['BusinessTravel'].replace('Travel_Frequently',2, inplace=True)
	x['BusinessTravel'].replace('Non-Travel',3, inplace=True)
	from sklearn.cross_validation import train_test_split
	x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3, random_state=0)
	from sklearn.linear_model import LogisticRegression
	model = LogisticRegression()
	# is a predictive analysis.
	# is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal,
	model = model.fit(x, y)
	#quoting the R2 statistic from the fit (which measures the fraction of the total variability in the response that is accounted for by the model)
	model2=LogisticRegression()
	model2.fit(x_train, y_train)
	#Prediction=model12.predict(x_test)=0.84
	predicted= model2.predict(x_test)
	probs = model2.predict_proba(x_test)#its used for calculating probablity
	user_input=pd.DataFrame(dict1,index=[0],columns=x.columns)
	price=model.predict_proba(user_input)
	response=str(round(price[0,0],4)*100)
	return HttpResponse(response)	
def emp_in(request):
	res = request.GET['res']
	return render(request,'emp_in.html',{"resp":res})
	
def emp_out(request):
	res = request.GET['res']
	return render(request,'emp_out.html',{"resp":res})