from django.http import HttpResponse
from django.template import Context,loader
from django.forms import *
import os


def index(request):
    msg = ""
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            #destination = open(os.path.join(os.getcwd(),"tmp"),"wb+")
            destination = open("tmp","wb+")
            upfile = request.FILES["file"]
            for chunk in upfile.chunks():
                destination.write(chunk)
            destination.close()
            msg = "Uploaded."
    else:
        form = UploadFileForm()

    t = loader.get_template(r"fileup\index.html")
    c = Context()
    c["form"] = form
    c["msg"] = msg
    return  HttpResponse(t.render(c))


class UploadFileForm(Form):
    title = CharField(max_length=50)
    file = FileField()
