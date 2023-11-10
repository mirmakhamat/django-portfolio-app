from django.shortcuts import render
from .models import Info, Service, Skill, Project, Feedback, Blog, ContactInfo
from .forms import GetInTouchForm
from bot.main import send_getintouch


def index(request):
    info = Info.objects.first()
    services = Service.objects.all()
    skills = Skill.objects.all()
    all_projects = Project.objects.all()
    count_projects = all_projects.count()
    n = 3
    projects = [all_projects[i * count_projects//n: (i+1)
                             * count_projects//n] for i in range(n)]
    projects.reverse()
    feedbacks = Feedback.objects.all()
    blogs = Blog.objects.all()
    contact_info = ContactInfo.objects.first()

    if request.method == "POST":
        get_in_touch_form = GetInTouchForm(request.POST)
        if get_in_touch_form.is_valid():
            get_in_touch_form.save()
            name = get_in_touch_form.data['name']
            email = get_in_touch_form.data['email']
            message = get_in_touch_form.data['message']
            send_getintouch(name, email, message)

    return render(request, 'index.html', {'info': info,
                                          'services': services,
                                          'skills': skills,
                                          'projects': projects,
                                          'feedbacks': feedbacks,
                                          'blogs': blogs,
                                          'contact_info': contact_info})
