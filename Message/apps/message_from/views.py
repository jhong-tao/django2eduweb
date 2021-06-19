from django.shortcuts import render

# 如何配置一个html页面显示的步骤
# 1.配置url
# 2.配置对应的views逻辑
# 3.拆分静态文件（css,js,img）放入到static文件夹，html文件放入到template文件夹下
#   1、静态文件可以放入到对应app下面的static文件夹下
#   2、也可以放入到全局static文件夹和template文件夹下
# 4.配置全局的static文件的路径
# Create your views here.


def message_form(request):
    return render(request, 'message_form.html')