from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Classify, Photographer, MyPicture, Celebrity, Message
from .forms import MessageForm
# Create your views here.


class IndexView(View):

    def get(self, req):
        classify = Classify.objects.all()
        celebrity = Celebrity.objects.all()
        pictures = MyPicture.objects.all()
        return render(req, 'picture/index.html', locals())


class PortfolioView(View):

    def get(self, req):
        classify = Classify.objects.all()
        return render(req, 'picture/portfolio.html', locals())


class AboutView(View):

    def get(self, req):
        photographers = Photographer.objects.all()
        return render(req, 'picture/about.html', locals())


class ContactView(View):

    def get(self, req):
        mf = MessageForm()
        messages = Message.objects.all()
        return render(req, 'picture/contact.html', locals())

    def post(self, req):
        mf = MessageForm(req.POST)
        mf.save()
        return redirect(reverse('picture:contact'))


class SingleView(View):

    def get(self, req, id):
        classify = Classify.objects.get(pk=id)
        pictures = classify.mypicture_set.all()

        return render(req, 'picture/single.html', locals())


class PersonalView(View):

    def get(self, req, id):
        photographer = Photographer.objects.get(pk=id)
        classify_list = Classify.objects.filter(photographer=photographer)
        # sum_num = 0
        data_list = []
        for i in classify_list:
            data_use = {}
            pictures = MyPicture.objects.filter(belong=photographer).filter(classify=i)
            num = len(pictures)
            # data_use.setdefault("pcitures",pictures)
            data_use.setdefault("classify", i)
            data_use.setdefault("number", num)
            data_list.append(data_use)
            # sum_num += num
        data_num={}
        # data_num["sum_pictures"]=sum_num
        data_num["data"] = data_list

        # print(data_num)
        return render(req, 'picture/personal.html', locals())


class PersonalSingleView(View):

    def get(self, req, id1, id2):
        belong = Photographer.objects.get(pk=id1)
        classify = Classify.objects.get(pk=id2)
        pictures = MyPicture.objects.filter(belong=belong, classify=classify)
        return render(req, 'picture/single.html', locals())
