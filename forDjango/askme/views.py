from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from . import models

# Create your views here.
def mainPage(request):
    base_context = {
        "popular_tags": models.Tag.objects.order_by_popular()[:6],
        "best_members": models.Profile.objects.all()[:5],
    }
    return render(request, 'mainPage.html', context=(base_context | paginate(models.Question.objects.order_by_rating(), request)))

def answerPage(request, id: int):
    base_context = {
        "popular_tags": models.Tag.objects.order_by_popular()[:6],
        "best_members": models.Profile.objects.all()[:5],
    }
    question_item = models.Question.objects.get_by_id(id)
    context = {"question": question_item} | paginate(
        models.Answer.objects.get_answers(question_item), request)
    return render(request, 'answerPage.html', context=(context | base_context))

def askQuestPage(request):
    return render(request, 'askQuestPage.html')

def logInPage(request):
    base_context = {
        "popular_tags": models.Tag.objects.order_by_popular()[:6],
        "best_members": models.Profile.objects.all()[:5],
    }
    return render(request, 'logInPage.html', context=base_context)

def registrationPage(request):
    base_context = {
        "popular_tags": models.Tag.objects.order_by_popular()[:6],
        "best_members": models.Profile.objects.all()[:5],
    }
    return render(request, 'registrationPage.html', context=base_context)

def searchingByTagPage(request, tag_name: str):
    base_context = {
        "popular_tags": models.Tag.objects.order_by_popular()[:6],
        "best_members": models.Profile.objects.all()[:5],
    }
    context = {"tag": tag_name} | paginate(
        models.Question.objects.get_by_tag(tag_name), request)
    return render(request, "searchingByTagPage.html", context=(context | base_context))

def settingsPage(request):
    return render(request, 'settingsPage.html')

def paginate(objects_list, request, per_page=3):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get("page") or 1
    page_obj = paginator.get_page(page_number)
    result = {
        "page_obj": page_obj,
        "ELLIPSIS": paginator.ELLIPSIS,
        "elided_page_range": []
    }
    try:
        result["elided_page_range"] = [
            p for p in paginator.get_elided_page_range(
                number=page_number, on_each_side=2, on_ends=1)]
    except (PageNotAnInteger, EmptyPage):
        result["elided_page_range"] = [
            p for p in paginator.get_elided_page_range(
                number=paginator.num_pages, on_each_side=2, on_ends=1)]
    return result


