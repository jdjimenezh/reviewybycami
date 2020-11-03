from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):

    model = Post
    list_display =  ('id', 'created_at', 'updated_at',
    'uuid',
    'title',
    'content',
    'image' )



admin.site.register(Post,PostAdmin)