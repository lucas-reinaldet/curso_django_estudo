from django.contrib import admin
from .models import Post
from .models import Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categories']
    search_fields = ['title', 'sub_title']
    # fields = ['title', 'sub_title']

    # def get_queryset(self, request):
    #     return Post.objects.filter(approved=True)

admin.site.register(Post, PostAdmin)

class PostContact(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Contact, PostContact)

