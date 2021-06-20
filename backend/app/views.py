from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    print("home")

    return render(req, "home.html", {"temp_key": "temp value"})


def add(req):
    print("add")

    if req.method == "POST":
        print("post")

        val1 = req.POST["firstname"]
        val2 = req.POST["lastname"]

        print(val1)
        print(val2)

        return render(req, "result.html", {"val1": val1, "val2": val2})

    elif req.method == "GET":
        print("GET")

        val1 = "mitre"
        val2 = "miric"

        return render(req, "result.html", {"val1": val1, "val2": val2})


    else:
        print("OTHER")

