from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
import pdfkit
# Create your views here.


def create(request):
    if request.method == 'POST':
        pydict = dict(request.POST)
        my_dict = {i: pydict[i] for i in pydict.keys() if not('csrf' in i)}
        with open('resume_app_resume/vitas.json') as jf:
            json_dict = json.load(jf)
            num = 1
            for i in json_dict.keys():
                num = int("".join([s for s in i if s.isdigit()]))
            json_dict[f'cv{num+1}'] = my_dict
        write_json(json_dict)
    context = {}
    return render(request, 'resumies/create_cv.html', context)


def write_json(data, filename='resume_app_resume/vitas.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def home(request):
    with open('resume_app_resume/vitas.json', 'r') as jf:
        json_dict = json.load(jf)
    my_dict = {}
    for item in json_dict.keys():
        my_dict[item] = {i: json_dict[item][i] for i in
                         json_dict[item].keys() if i == "fullname" or i == "professionsInput"}
    context = {"vitas": my_dict}
    return render(request, 'resumies/home.html', context)


def show_cv(request, pk):
    if request.method == 'POST':
        print("nigga")
        redirect("/")
    with open('resume_app_resume/vitas.json', 'r') as jf:
        json_dict = json.load(jf)
    cv_for_show = json_dict[pk]
    skill_set = {cv_for_show['skillname'][y]: cv_for_show['skilltext'][y]
                 for y in range(len(cv_for_show['skillname']))}
    work_set = dictmaker(cv_for_show, 'companyname',
                         'position', 'data-field', 'aboutwork')
    education_set = dictmaker(cv_for_show, 'education',
                              'education-data', 'educationfield', 'gpa')
    context = {
        "cv_for_show": cv_for_show,
        'skillset': skill_set,
        'expirience': work_set,
        'educations': education_set,
    }
    return render(request, 'resumies/index.html', context)


def deletecv(request, pk):
    with open('resume_app_resume/vitas.json', 'r') as jf:
        json_dict = json.load(jf)
    json_dict.pop(pk)
    write_json(json_dict)
    return redirect("/")


def dictmaker(data, *args):
    work_data = {}
    namecount = 1
    keyname = 'exp1'
    for key in range(len(data[args[0]])):
        for i in work_data.keys():
            if i == keyname:
                namecount += 1
        keyname = f"{keyname[0:-1]}{namecount}"
        for arg in range(0, len(args)):
            if arg == 0:
                work_data[keyname] = {arg: data[args[arg]][key]}
            else:
                work_data[keyname].update({arg: data[args[arg]][key]})
    return work_data

def show_cv_for_pdf(request, pk):
    with open('resume_app_resume/vitas.json', 'r') as jf:
        json_dict = json.load(jf)
    cv_for_show = json_dict[pk]
    skill_set = {cv_for_show['skillname'][y]: cv_for_show['skilltext'][y]
                 for y in range(len(cv_for_show['skillname']))}
    work_set = dictmaker(cv_for_show, 'companyname',
                         'position', 'data-field', 'aboutwork')
    education_set = dictmaker(cv_for_show, 'education',
                              'education-data', 'educationfield', 'gpa')
    context = {
        "cv_for_show": cv_for_show,
        'skillset': skill_set,
        'expirience': work_set,
        'educations': education_set,
    }
    return render(request, 'resumies/index2.html', context)




def generate_PDF(request,pk):
    options = {
         'dpi': 400,
         'page-size': 'Letter',
         'margin-top': '0.25in',
         'margin-right': '0.0in',
         'margin-bottom': '0.25in',
         'margin-left': '0.0in',
         'encoding': "UTF-8",
         'custom-header' : [
            ('Accept-Encoding', 'gzip')
         ],
         'no-outline': None,
    }
    pdfkit.from_url(f'https://cvapplicationam.herokuapp.com/show1/{pk}','resume_app_resume/templates/pdf/cv.pdf',options=options)
    file = open('resume_app_resume/templates/pdf/cv.pdf', "r+b")
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')
# def pdfmaker(request):
#     print(request.path)
#     return render(request,'pdf/cv.pdf')


