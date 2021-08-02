from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Blog 
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Post listing
def home(request):
	# Fetching all the posts
	post_list = Blog.objects.all().order_by('-id')
	page = request.GET.get('page',1)

	paginator = Paginator(post_list, 5)
	try: 
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'front/posts/posts.html',{'posts':posts})

# Adding a new Post
class AddPost(View):

	def get(self, request):
		post_form = PostForm()
		return render(request,'front/posts/store.html',{'post_form':post_form})

	def post(self,request):
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			title       = post_form.cleaned_data['title']
			description = post_form.cleaned_data['description']

			# Insert to blog table
			blog = Blog(title=title,description=description)
			blog.save()

			messages.success(request, "Post Added Successfully!")
			return HttpResponseRedirect(reverse('add_post'))
		else:
			messages.error(request, "Validate your Input Data")
			return render(request,'front/posts/store.html',{'post_form':post_form})


# Update a Post
class EditPost(View):

	def get(self,request,*args,**kwargs):
		id = kwargs.get('id',None)

		try:
			data = Blog.objects.get(id=id)
		except Blog.DoesNotExist:
			data = None

		if data is not None:
			post_form = PostForm(initial={'title': data.title,'description':data.description})
			return render(request,'front/posts/update.html',{'post_form':post_form,'edit_id':id})

		else:
			messages.error(request, "Post not exist!")
			return HttpResponseRedirect(reverse('home'))

	def post(self,request):

		post_form = PostForm(request.POST)
		if post_form.is_valid():
			id          = request.POST['edit_id']
			title       = post_form.cleaned_data['title']
			description = post_form.cleaned_data['description']

			Blog.objects.filter(pk=id).update(title=title,description=description)

			messages.success(request, "Post updated successfully!")
			return HttpResponseRedirect(reverse('edit_get', kwargs={'id':id}))

		else:
			messages.error(request, "Validate your Input Data")
			return render(request,'front/posts/update.html',{'post_form':post_form})
		return HttpResponse('In edit post')


# Show post details
def show_post(request,id):

	if id is not None:

		try:
			post_data = Blog.objects.get(pk=id)
		except Blog.DoesNotExist:
			post_data = None

		if post_data is not None:
			return render(request,'front/posts/show.html',{'post_data':post_data})
		else:
			messages.error(request, "Post Not Exists")
			return HttpResponseRedirect(reverse('home'))

	else:
		messages.error(request, "Invalid Request")
		return HttpResponseRedirect(reverse('home'))
 		
