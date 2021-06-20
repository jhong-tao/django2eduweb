from django.shortcuts import render

# 如何配置一个html页面显示的步骤
# 1.配置url
# 2.配置对应的views逻辑
# 3.拆分静态文件（css,js,img）放入到static文件夹，html文件放入到template文件夹下
#   1、静态文件可以放入到对应app下面的static文件夹下
#   2、也可以放入到全局static文件夹和template文件夹下
# 4.配置全局的static文件的路径
# Create your views here.

from apps.message_from.models import Message


def message_form(request):
    # Message.objects.all()返回queryset对象
    # queryset本身并没有执行sql操作，只有执行对数据的访问query的时候在执行sql

    # all() 方法 返回所有的数据 列表
    # all_message = Message.objects.all()
    # filter() 返回有条件的查询 列表
    # all_message = Message.objects.filter(name='bobby')
    # for message in all_message:
    #     print(message.name)
    #
    # # get()返回一条数据，是一个单独的一条记录，如果数据不存在，或者有多条数据存在会抛出异常
    # message = Message.objects.get(name='bobby')
    # message.delete()    # 从数据库中删除这条记录
    # print(message.address)
    #
    # # 数据插入操作
    # message = Message()
    # message.name = 'bobby'
    # message.address = '北京'
    # message.message = 'hello'
    # message.email = 'bobby@qq.com'
    # message.save()      # save()方法将数据保存到数据，如果源数据库中有主键对应的数据那么直接更新数据。存在更新，不存在插入

    # 通过request对象从html中提取数据，保存到数据库中
    # 如果浏览器是做POST请求，也就是提交数据请求
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message_text = request.POST.get('message', '')

        message = Message()

        message.name = name
        message.address = address
        message.message = message_text
        message.email = email

        message.save()

        return render(request, 'message_form.html', {
                'message': message
            })

    # 从数据库中取出数据，在HTML展示
    if request.method == 'GET':
        var_dict = {}
        all_message = Message.objects.all()
        if all_message:
            message = all_message[0]
            var_dict = {
                'message': message
            }
        return render(request, 'message_form.html', var_dict)
