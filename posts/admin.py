from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author') # <- перечисляем поля, которые
    # должны отображаться в админке.
    # pk => уникальный идентификатор записи в базе данных (будет выводиться, если
    # тело поста окажется пустым).
    search_fields = ('text',) # <- отображаем интерфейс для поиска по тексту постов
    list_filter = ('pub_date',) # <- добавляем возможность фильтрации по дате
    empty_value_display = '-пусто-' # <- для отображение пустых полей можно установить
    # значение по умолчанию, и теперь если тело поста окажется пустым, будет выводиться
    # это значение.


admin.site.register(Post, PostAdmin) # <- регистрируем модели в админке