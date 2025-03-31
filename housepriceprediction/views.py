import joblib;
import numpy as np;
from django.shortcuts import redirect, render
 # loading model
model = joblib.load("housepricepredict.joblib")

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")


def result (request):
    # getting data from user
    income = float(request.GET["income"])
    age = float(request.GET["age"])
    rooms = float(request.GET["rooms"])
    bedrooms = float(request.GET["bedrooms"])
    population = float(request.GET["population"])

    predict=model.predict(np.array([[income, age, rooms, bedrooms, population]]))

    # getting the result
    # access to the predicted first values
    predict = round(predict[0])

    price = "The predicted price is $" + str(predict)

   


    return render(request,"predict.html",{"result2":price})