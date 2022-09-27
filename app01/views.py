from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from app01.models import Article, Comment

# Create your views here.

def root(request):
    return HttpResponse('Hello Django')

def pattern(request, username):
    return HttpResponse('Hello {}'.format(username))

def param(request):
    text = ''
    for key in request.GET:
        text += '{} : {}, '.format(key, request.GET[key])
    return HttpResponse(text)

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
		article = Article(title=request.POST["title"],body=request.POST["text"])
		#,image=request.POST['image'])
		#if  "image" in request.POST:
		#	article.image=request.FILES['image']
		#else:
		#	article.image=False
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
	if request.method == 'POST':
		article.title = request.POST['title']
		article.body = request.POST['text'] 
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

def rank(request):
	context = {
        "articles": Article.objects.order_by("-like")
		#"articles": Article.objects.all()
	}
	return render(request, 'app01/rank.html', context)