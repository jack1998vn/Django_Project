from django.shortcuts import render
from stories import models


# Create your views here.
def index(request):
    # Xử lý 5 hình đầu tiên của trang index
    story_list = models.Story.objects.order_by('-public_day')  # => list
    newest_1 = story_list[0]
    newest_4 = story_list[1:5]

    # Đọc danh sách story theo category
    young_children = models.Story.objects.filter(category=1).order_by('-public_day')  # list
    older_children = models.Story.objects.filter(category=2).order_by('-public_day')  # list

    # Danh sách Category
    category_list = models.Category.objects.order_by('name')

    return render(request, 'stories/index.html', context={
        'newest_1': newest_1,
        'newest_4': newest_4,
        'young_children': young_children,
        'older_children': older_children,
        'category_list': category_list,
    })


def blog(request, pk):
    story_list = models.Story.objects.filter(category=pk).order_by('-public_day')

    # Danh sách story mới nhất
    story_list_right = models.Story.objects.order_by('-public_day')
    newest_stories = story_list_right[:7]

    # Hiển thị tiêu đề Category
    selected_category = models.Category.objects.get(pk=pk)
    category_name = selected_category.name

    # Danh sách Category
    category_list = models.Category.objects.order_by('name')

    return render(request, 'stories/blog.html', context={
        'story_list': story_list,
        'newest_stories': newest_stories,
        'category_name': category_name,
        'category_list': category_list,
    })


def single(request, pk):
    story = models.Story.objects.get(pk=pk)

    # Danh sách Category
    category_list = models.Category.objects.order_by('name')

    return render(request, 'stories/single.html', context={
        'story': story,
        'category_list': category_list,
    })


def contact(request):
    # Danh sách Category
    category_list = models.Category.objects.order_by('name')
    return render(request, 'stories/contact.html', context={
        'category_list': category_list,
    })

