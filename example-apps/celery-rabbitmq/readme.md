Based upon: https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html


**Why use Celery?**

Web applications works with request and response cycles. When the user access a certain URL of your application the Web browser send a request to your server. Django receive this request and do something with it. Usually it involves executing queries in the database, processing data. While Django does his thing and process the request, the user have to wait. When Django finalize its job processing the request, it sends back a response to the user who finally will see something.

Ideally this request and response cycle should be fast, otherwise we would leave the user waiting for way too long. And even worse, our Web server can only serve a certain number of users at a time. So, if this process is slow, it can limit the amount of pages your application can serve at a time.

For the most part we can work around this issue using cache, optimizing database queries, and so on. But there are some cases that theres no other option: the heavy work have to be done. A report page, export of big amount of data, video/image processing are a few examples of cases where you may want to use Celery.

We don’t use Celery through the whole project, but only for specific tasks that are time-consuming. The idea here is to respond to the user as quick as possible, and pass the time-consuming tasks to the queue so to be executed in the background, and always keep the server ready to respond to new requests.