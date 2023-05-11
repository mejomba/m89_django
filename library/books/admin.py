from django.contrib import admin
from .models import Book, Category, Publisher, Discount, User


class BookAdmin(admin.ModelAdmin):
    # def render_change_form(self, request, context, *args, **kwargs):
    #     context['adminform'].form.fields['author'].queryset = User.objects.filter(is_author=True)
    #     return super(BookAdmin, self).render_change_form(request, context, *args, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super(BookAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = User.objects.filter(is_author=True)
        return form


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Discount)


