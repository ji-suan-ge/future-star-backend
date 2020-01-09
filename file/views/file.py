"""
file

:author: lishanZheng
:date: 2020/01/09
"""
import os
import time

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from file.constant.code import MISS_FILE
from util.result_util import success, error


@csrf_exempt
def upload(request):
    """
    upload

    :author: lishanZheng
    :date: 2020/01/09
    """
    file = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not file:
        return error(MISS_FILE, '没有选择文件')
    time_str = str(time.time()).replace('.', '')
    file_name = 'media/{0}{1}'.format(time_str, file.name)
    path = os.path.join(os.path.join(settings.FILE_ROOT_DIR, file_name))
    # 根据路径打开指定的文件(以二进制读写方式打开)
    destination = open(path, 'wb+')
    # 分块写入文件
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    url = settings.FILE_HOST + '/' + file_name
    res = {
        'url': url
    }
    return success(res)
