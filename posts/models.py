from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField() # поле для хранения произвольного текста;
    pub_date = models.DateTimeField('date published', auto_now_add=True) # поле для хранения даты и времени;
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') # поле, 
    # в котором указывается ссылка на другую модель; 
    # (ссылка на другую таблицу), Параметр on_delete=models.CASCADE обеспечивает связность данных: если из 
    # таблицы User будет удалён пользователь, то будут удалены все связанные с ним посты.