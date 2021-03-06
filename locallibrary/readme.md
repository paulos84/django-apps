**LocalLibrary - Mozilla tutorial**

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django. The tutorial was adapted for Django2.0.

![](https://preview.ibb.co/k9x5mb/locallib.png)



**Model Field Arguments and Metadata**

help_text: Provides a text label for HTML forms (e.g. in the admin site).
verbose_name: A humanreadable name for the field in field labels.
choices: A group of choices for this field. If this is provided, the default corresponding form widget will be a                                   		  select box with these choices instead of the standard text field.
primary_key: If True, sets the current field as the primary key for the model (A primary key is a special database column designated to uniquely identify all the different table records). If no field is specified then Django will automatically add a pk field.

    ordering = ["title", "-pubdate"]
The books would be sorted alphabetically by title, from A-Z, and then by publication date inside each title, from newest to oldest. Another common attribute is verbose_name, for the class in singular and plural form

**Sessions Framework**

The session framework allows e.g. hide warning messages that the user has previously acknowledged next time they visit the site, or store and respect their preferences. It allows you to store and retrieve arbitrary data on a per-site-visitor basis. Sessions to improve your interaction with anonymous users (i.e. not authenticated and authorized users). 

All communication between web browsers and servers is via the HTTP protocol, which is stateless. The fact that the protocol is stateless means that messages between the client and server are completely independent of each other - there is no notion of "sequence" or behaviour based on previous messages. As a result, if you want to have a site that keeps track of the ongoing relationships with a client, you need to implement that yourself. Sessions are the mechanism used by Django (and most of the Internet) for keeping track of the "state" between the site and a particular browser. Sessions allow you to store arbitrary data per browser, and have this data available to the site whenever the browser connects. Individual data items associated with the session are then referenced by a "key", which is used both to store and retrieve the data.

Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default (this is more secure than storing the data in a cookie, where they are more vulnerable to malicious users). You can configure Django to store the session data in other places (cache, files, "secure" cookies), but the default location is a good and relatively secure option. The configuration is set up in the INSTALLED_APPS and MIDDLEWARE sections of settings.py

You can access the session attribute in the view from the request parameter (an HttpRequest passed in as the first argument to the view). This session attribute represents the specific connection to the current user (or to be more precise, the connection to the current browser, as identified by the session id in the browser's cookie for this site). The session attribute is a dictionary-like object that you can read and write as many times as you like in your view, modifying it as wished. You can do all the normal dictionary operations, including clearing all data, testing if a key is present, looping through data, etc.

    my_car = request.session.get('my_car', 'mini')
    
    request.session['my_car'] = 'mini'
    
    del request.session['my_car']

The API also offers a number of other methods that are mostly used to manage the associated session cookie.  For example, there are methods to test that cookies are supported in the client browser, to set and check cookie expiry dates, and to clear expired sessions from the data store (see Django docs).


**Authentication and Authorization**

Django provides "stock" authentication views and forms for login and logout pages.The necessary configuration was all done for us when we created the app using the django-admin startproject command. The configuration is set up in the INSTALLED_APPS and MIDDLEWARE sections of the project file

If you're using function-based views, the easiest way to restrict access to your functions is to apply the login_required decorator to your view function, as shown below. If the user is logged in then your view code will execute as normal. If the user is not logged in, this will redirect to the login URL defined in the project settings (settings.LOGIN_URL), passing the current absolute path as the next URL parameter.

    from django.contrib.auth.decorators import login_required
    @login_required
    def my_view(request):
    ...
Note: You can do the same sort of thing manually by testing on request.user.is_authenticated, but the decorator is much more convenient! The easiest way to restrict access to logged-in users in your class-based views is to derive from LoginRequiredMixin. You need to declare this mixin first in the super class list, before the main view class.

    from django.contrib.auth.mixins import LoginRequiredMixin
    class MyView(LoginRequiredMixin, View):
        ...

This has exactly the same redirect behaviour as the login_required decorator. You can also specify an alternative location to redirect the user to if they are not authenticated (login_url), and a URL parameter name instead of "next" to insert the current absolute path (redirect_field_name).

    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'
        redirect_field_name = 'redirect_to'

**Working with Forms**

The form is defined in HTML as a collection of elements inside forms tags, containing at least one input element of type="submit".

![](https://preview.ibb.co/nm6nzw/basic_form.png)

While here we just have one text field for entering the team name, a form may have any number of other input elements and their associated labels. The field's type attribute defines what sort of widget will be displayed. The name and id of the field are used to identify the field in JavaScript/CSS/HTML, while value defines the initial value for the field when it is first displayed. The matching team label is specified using the label tag (see "Enter name" above), with a for field containing the id value of the associated input. The submit input will be displayed as a button (by default) that can be pressed by the user to upload the data in all the other input elements in the form to the server (in this case, just the team_name). The form attributes define the HTTP method and the destination of the data on the server (action):

action: The resource/URL where data is to be sent for processing when the form is submitted. If this is not set (or set to an empty string), then the form will be submitted back to the current page URL.
method: The HTTP method used to send the data: post or get. The POST method should always be used if the data is going to result in a change to the server's database, because this can be made more resistant to cross-site forgery request attacks. The GET method should only be used for forms that don't change user data (e.g. a search form). 

Creating the HTML, validating the returned data, re-displaying the entered data with error reports if needed can take quite a lot of effort. Django makes this a lot easier, by taking away some of the heavy lifting and repetition. The most fundamental tool is the Form class, which simplifies both generation of form HTML and data cleaning/validation.

Django provides numerous places where you can validate your data. The easiest way to validate a single field is to override the method clean_<fieldname>() for the field you want to check. we get our data using e.g. self.cleaned_data['renewal_date'] and that we return this data whether or not we change it at the end of the function. This step gets us the data "cleaned" and sanitised of potentially unsafe input using the default validators, and converted into the correct standard type for the data (in this case a Python datetime.datetime object). Then if a value falls outside our range we raise a ValidationError, specifying the error text that we want to display in the form if an invalid value is entered.

Creating a form using the Form class is very flexible, allowing you to create whatever sort of form page you like and associate it with any model or models. However if you just need a form to map the fields of a single model then your model will already define most of the information that you need in your form: fields, labels, help text, etc. Rather than recreating the model definitions in your form, it is easier to use the ModelForm helper class to create the form from your model. This ModelForm can then be used within your views in exactly the same way as an ordinary Form.  All you need to do to create the form is add class Meta with the associated model (BookInstance) and a list of the model fields to include in the form (you can include all fields using fields = 'dunder all' or you can use exclude (instead of fields) to specify the fields not to include from the model).

**Testing a Django web application**

Django provides a test framework with a small hierarchy of classes that build on the Python standard unittest library. The Django framework adds API methods and tools to help test web and Django-specific behaviour. These allow you to simulate requests, insert test data, and inspect your application's output.

The best base class for most tests is django.test.TestCase.  This test class creates a clean database before its tests are run, and runs every test function in its own transaction. The class also owns a test Client that you can use to simulate a user interacting with the code at the view level. The django.test.TestCase class may result in some tests being slower than they need  as not every test will need to set up its own database or simulate the view interaction); you can replace some of your tests with the available simpler test classes.

![](https://preview.ibb.co/i5iNXG/testcase.png)

The AssertTrue, AssertFalse, AssertEqual are standard assertions provided by unittest.  There are other standard assertions in the framework, and also Django-specific assertions to test if a view redirects (assertRedirects), to test if a particular template has been used (assertTemplateUsed), etc. Django uses the unittest module’s built-in test discovery, which will discover tests under the current working directory in any file named with the pattern test*.py.

    python3 manage.py test catalog.tests   # Run the specified module
    
    python3 manage.py test catalog.tests.test_models  # Run the specified module
    
    python3 manage.py test catalog.tests.test_models.YourTestClass 
    # Run the specified class
    
    python3 manage.py test catalog.tests.test_models.YourTestClass.test_one_plus_one_equals_two  # Run the specified method

For test_forms we don't actually use the database or test client so SimpleTestCase is used. To validate our view behaviour we use the Django test Client. This class acts like a dummy web browser that we can use to simulate GET and POST requests on a URL and observe the response. We can see almost everything about the response, from low-level HTTP (result headers and status codes) through to the template we're using to render the HTML and the context data we're passing to it. We can also see the chain of redirects (if any) and check the URL and status code at each step. This allows us to verify that each view is doing what is expected. As AuthorListView is a generic list view almost everything is done for us by Django. Arguably if you trust Django then the only thing you need to test is that the view is accessible at the correct URL and can be accessed using its name. Below, the first line checks a specific URL (note, just the specific path without the domain) while the second generates the URL from its name in the URL configuration.

    resp = self.client.get('/catalog/authors/')
    resp = self.client.get(reverse('authors'))

Once we have the response we query it for its status code, the template used, whether or not the response is paginated, the number of items returned, and the total number of items. The most interesting variable above is resp.context, which is the context variable passed to the template by the view. This is very useful for as it allows us to confirm that our template is getting all the data it needs.

**Caching**

Useful reading: https://djangobook.com/djangos-cache-framework/ 
Caching is a technique that stores a copy of a given resource and serves it back when requested. When a web cache has a requested resource in its store, it intercepts the request and returns its copy instead of re-downloading from the originating server. this eases the load of the server and it takes less time to transmit the resource back to the clients. For a web site, it is a major component in achieving high performance.

Caching can be grouped into two main categories: private browser caches and shared caches. A shared cache is a cache that stores responses for reuse by more than one user. A private cache is dedicated to a single user. HTTP headers can be used to control caching by the client browser, e.g. Django has cache_control decorator where cachability and expiry set; sometimes you don’t want caching if the content changes frequently. Share caches involve using intermediaries to serve many users in a way that popular resources are reused a number of times.  They involve in memory key-value stores/ nosql database like redis. Static assets like CSS and JavaScript are good candidates to be cached by CDNs and other intermediaries.

**Deploying Django to production**

Many of the Django project settings (specified in settings.py) should be different for production, either for security or performance reasons. It is common to have a separate settings.py file for production.
he critical settings that you must check are: DEBUG and SECRET_KEY. The Django documents suggest that this might best be loaded from an environment variable or read from a serve-only file.
During development no environment variable will be specified for the key, so the default value will be used (it shouldn't matter what key you use here, or if the key "leaks", because you won't use it in production).

    # SECRET_KEY = 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag'
    import os
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

**Django web application security**

Never trust data from the browser. This includes GET request data in URL parameters, POST data, HTTP headers and cookies, user-uploaded files, etc. Always assume worst, check and sanitize all incoming data.
 
 Cross site scripting (XSS)
 XSS is a term used to describe a class of attacks that allow an attacker to inject client-side scripts through the website into the browsers of other users. This is usually achieved by storing malicious scripts in the database where they can be retrieved and displayed to other users, or by getting users to click a link that will cause the attacker’s JavaScript to be executed by the user’s browser. Django's template system protects you against the majority of XSS attacks by escaping specific characters that are "dangerous" in HTML. script tags have been turned into their harmless escape code equivalents (e.g. > is now &gt;)
 
CSRF attacks allow a malicious user to execute actions using the credentials of another user without that user’s knowledge or consent. For example consider the case where we have a hacker who wants to create additional authors for our LocalLibrary.
![](https://preview.ibb.co/ndbWRb/csrf.png)
Django's CSRF protection is turned on by default. You should always use the {% csrf_token %} template tag in your forms. Forms that are submitted without the correct csrf token will be rejected.

Host header validation
 Use ALLOWED_HOSTS to only accept requests from trusted hosts.     Enforcing SSL/HTTPS e.g. SECURE_SSL_REDIRECT is used to redirect all HTTP requests to HTTPS. Use ‘secure’ cookies by setting SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE to True. This will ensure that cookies are only ever sent over HTTPS.

