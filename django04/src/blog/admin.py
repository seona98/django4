from django.contrib import admin
from blog.models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostFile)
admin.site.register(PostImage)
