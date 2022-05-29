from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Answer, Question, Category

import logging
logger = logging.getLogger('pybo')


def index(request, category_name='qna'):
    logger.info('INFO 레벨로 출력')
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)
    
    question_list = question_list.order_by('-create_date')
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  
            Q(content__icontains=kw) |  
            Q(answer__content__icontains=kw) |  
            Q(author__username__icontains=kw) |  
            Q(answer__author__username__icontains=kw)  
        ).distinct()
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw,
               'category_list': category_list, 'category': category}
    # context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    page = request.GET.get('page', '1')
    question = get_object_or_404(Question, pk=question_id)
    answer_set = Answer.objects.filter(Q(question_id=question.id)).order_by('-create_date')
    paginator = Paginator(answer_set, 5)
    page_obj = paginator.get_page(page)
    context = {'question': question, 'answer_set': page_obj, 'page': page}
    return render(request, 'pybo/question_detail.html', context)
