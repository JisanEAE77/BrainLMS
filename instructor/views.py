from django.shortcuts import render
from instructor.models import SubscriptionType, TutionSubscription
from student.models import ClassType, Subject
from django.contrib.auth.models import User

# Create your views here.


def createCourse(request, *args, **kwargs):
    subjects = Subject.objects.all()
    classes = ClassType.objects.all()
    sTypes  = SubscriptionType.objects.all()

    context = {
        "subjects": subjects,
        "classes": classes,
        "sTypes": sTypes,
        "error": "",
    }

    if request.method == "POST":
        subName = request.POST['subjectName']
        className = request.POST['className']
        description = request.POST['courseDescription']
        thumbnail = request.FILES.get('upThumbnail')
        subscription = request.POST["sType"]
        fee = request.POST["fee"]
        hpd = request.POST["hpd"]
        user = request.user.id

        author = User.objects.get(id=user)
        subject = Subject.objects.get(name=subName)
        subscription_type = SubscriptionType.objects.get(slug=subscription)
        fee = fee
        hpd = hpd
        description = description
        classType = ClassType.objects.get(name=className)
        print(author, subject, subscription_type, fee, hpd, classType, thumbnail)

        try:
            course = TutionSubscription.objects.create(author=author, subject=subject, subscription_type=subscription_type, fee=fee, hpd=hpd, description=description, classType=classType, thumbnail=thumbnail)
        except:
            context["error"] = "Course Creation Failed! Please try again with valid details."

    return render(request, 'BrainLMS/icreatecourse.html', context)
