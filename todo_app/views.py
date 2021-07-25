from django.shortcuts import render, get_object_or_404#追加
from django.utils import timezone
from .models import Folder, Task#追加

# Create your views here.
def index(request, id):
    #すべてのフォルダを取得する
    folders = Folder.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    #選ばれたフォルダを取得する
    current_folder = get_object_or_404(Folder, id=id)
    #選ばれたフォルダのタスクを取得する
    tasks = Task.objects.filter(folder_id = current_folder.id)

    return render(request, 'index.html', {
        'folders':folders,
        'tasks':tasks,
        'current_folder_id': current_folder.id,
    })![Screenshot from 2020-04-17 11-03-21.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/370196/2effc6d9-ccd6-3485-3eaa-4dceb2ae76da.png)

