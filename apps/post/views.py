from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, ExtendPost
from ..category.models import CategoryPost
from django.core.mail import send_mail


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


# def category_detail(request, title):  # this function requires title to filter by a category
#     post_category = Post.objects.get(title=title)
#     comments = post_category.comment.all()
#     post_category_name = CategoryPost.objects.get(name=title)
#     return render(request, 'blog_detail.html', locals())

class CategoryDetailView(DetailView):
    model = CategoryPost
    template_name = 'category-detail.html'
    context_object_name = 'post_category'
    print(context_object_name)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        # sending an email
        send_mail(
            message_name,
            message_subject,
            message,
            message_email,
            ['so.fly.azash@gmail.com',]
        )

        return render(request, 'contact.html', locals())
    # else:
    #     return render(request, 'contact.html', {})
