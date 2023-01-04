from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from app01.models import Article, Comment
from .forms import Image, Comment_Image
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from accounts.models import Person
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def root(request):
    return HttpResponse('Hello Django')

def pattern(request, username):
    return HttpResponse('Hello {}'.format(username))

def param(request):
    text = ''
    for key in request.GET:
        text += '{} : {}, '.format(key, request.GET[key])
    return HttpResponse(text)

@login_required
def top(request):
    return render(request, 'app01/top.html')

def dm(request):
    return render(request, 'app01/dm.html')

def tt(request):
    return render(request, 'app01/tt.html')

def logout(request):
    return render(request, 'app01/login.html')

def cla(request):
    return render(request, 'app01/cla.html')

def event(request):
    return render(request, 'app01/event.html')
    
def osero(request):
    return render(request, 'app01/osero.html')

def home(request):
    return render(request, 'app01/mytest.html')

def index(request):
	if request.method == 'POST':
		form = Image(request.POST)
		article = Article(title=request.POST["title"],body=request.POST["text"])
		article.user = request.user
		if "checkbox" in request.POST:
			article.anonymity = False
		else:
			article.anonymity = True
						
		if form.is_valid():
			article.image=request.FILES.get('image')
		else:
			article.image=False
		article.save()
		context = {
				"articles": Article.objects.order_by("-posted_at"),
			}
		return render(request, 'app01/top.html', context)
	else:
		context = {
            "articles": Article.objects.order_by("-posted_at")
			#"articles": Article.objects.all()
	    }
		return render(request, 'app01/top.html', context)

def update(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	#if article.user != Person.objects.get(pk=1):
	if article.is_owner(request.user) == False:
		raise PermissionDenied
	if request.method == 'POST':
		article.title = request.POST['title']
		article.body = request.POST['text'] 
		if "checkbox" in request.POST:
			article.anonymity = False
		else:
			article.anonymity = True
		article.save()
		return redirect(detail, article_id)
	context = {
		"article": article
	}
	return render(request, 'app01/keijiban-edit.html', context)

def delete(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article dose not exist")
	article.delete()
	return redirect(index)

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	if request.method == 'POST':
		comment = Comment(article=article, text=request.POST['text'])
		comment.user = request.user
		if "checkbox" in request.POST:
			comment.anonymity = False
		else:
			comment.anonymity = True
		form = Comment_Image(request.POST)
		if form.is_valid():
			comment.image=request.FILES.get('image')
		else:
			comment.image=False
		comment.save()

	context = {
		"article": article,
		"comments": article.comments.order_by("-posted_at")
		}
	return render(request, 'app01/keijiban-detail.html', context)

def like(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect(index)

def comment_detail(request, comment_id):
	try:
		comment = Comment.objects.get(pk=comment_id)
	except Comment.DoesNotExist:
		raise Http404("Comment does not exist")

	context = {
		"comment": comment,
		}
	return render(request, 'app01/comment-detail.html', context)

def comment_delete(request, comment_id):
	try:
		comment = Comment.objects.get(pk=comment_id)
	except Comment.DoesNotExist:
		raise Http404("Comment dose not exist")
	comment.delete()
	#return redirect(index)
	return redirect(detail, comment.article_id)

def comment_update(request, comment_id):
	try:
		comment = Comment.objects.get(pk=comment_id)
	except Comment.DoesNotExist:
		raise Http404("Comment does not exist")

	if comment.is_owner(request.user) == False:
		raise PermissionDenied
	if request.method == 'POST':
		comment.text = request.POST['text'] 
		if "checkbox" in request.POST:
			comment.anonymity = False
		else:
			comment.anonymity = True
		comment.save()

		return redirect(comment_detail, comment_id)
	context = {
		"comment": comment
	}
	return render(request, 'app01/Comment-edit.html', context)

def comment_like(request, comment_id):
	try:
		comment = Comment.objects.get(pk=comment_id)
		comment.like += 1
		comment.save()
	except Comment.DoesNotExist:
		raise Http404("Comment does not exist")
	return redirect(detail, comment.article.id)

def rank(request):
	context = {
        "articles": Article.objects.order_by("-like")
		#"articles": Article.objects.all()
	}
	return render(request, 'app01/rank.html', context)

"""
def comment_delete(comment_id):
	comment = get_object_or_404(Comment, id=comment_id)
	comment.delete()
	return redirect(index)
"""

"""
def comment_delete(comment_id):
	try:
		comment = Comment.objects.get(pk=comment_id)
	except Comment.DoesNotExist:
		raise Http404("Comment dose not exist")
	comment.delete()

	try:
		article = comment.article
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	context = {
		"article": article,
		"comments": article.comments.order_by("-posted_at")
		}
	return render('app01/keijiban-detail.html', context)

"""