This example project is based upon the Mozilla tutorial:  https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django. It has been adapted for Django2.0, using django.urls.path() and django.urls.re_path() instead of django.conf.urls.url()

**Sessions Framework**

The session framework allows e.g. hide warning messages that the user
has previously acknowledged next time they visit the site, or store and
respect their preferences. It allows you to store and retrieve arbitrary
data on a per-site-visitor basis. Sessions to improve your interaction with anonymous users (i.e. not authenticated and authorized users).

All communication between web browsers and servers is via the HTTP
protocol, which is stateless. The fact that the protocol is stateless
means that messages between the client and server are completely
independent of each other - there is no notion of "sequence" or behaviour
based on previous messages. As a result, if you want to have a site that
keeps track of the ongoing relationships with a client, you need to implement
that yourself.

Sessions are the mechanism used by Django (and most of the Internet) for keeping track of the "state" between the site and a particular browser. Sessions allow you to store arbitrary data per browser, and have this data available to the site whenever the browser connects. Individual data items associated with the session are then referenced by a "key", which is used both to store and retrieve the data.

Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default (this is more secure than storing the data in a cookie, where they are more vulnerable to malicious users). You can configure Django to store the session data in other places (cache, files, "secure" cookies), but the default location is a good and relatively secure option.

The configuration is set up in the INSTALLED_APPS and MIDDLEWARE sections of settings.py

You can access the session attribute in the view from the request parameter (an HttpRequest passed in as the first argument to the view). This session attribute represents the specific connection to the current user (or to be more precise, the connection to the current browser, as identified by the session id in the browser's cookie for this site).

The session attribute is a dictionary-like object that you can read and write as many times as you like in your view, modifying it as wished. You can do all the normal dictionary operations, including clearing all data, testing if a key is present, looping through data, etc.



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
Note: You can do the same sort of thing manually by testing on request.user.is_authenticated, but the decorator is much more convenient!

The easiest way to restrict access to logged-in users in your class-based views is to derive from LoginRequiredMixin. You need to declare this mixin first in the super class list, before the main view class.

from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    ...

This has exactly the same redirect behaviour as the login_required decorator. You can also specify an alternative location to redirect the user to if they are not authenticated (login_url), and a URL parameter name instead of "next" to insert the current absolute path (redirect_field_name).

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

**Working with Forms**

The form is defined in HTML as a collection of elements inside <form>...</form> tags, containing at least one input element of type="submit".

(basic form pic)

While here we just have one text field for entering the team name, a form may have any number of other input elements and their associated labels. The field's type attribute defines what sort of widget will be displayed. The name and id of the field are used to identify the field in JavaScript/CSS/HTML, while value defines the initial value for the field when it is first displayed. The matching team label is specified using the label tag (see "Enter name" above), with a for field containing the id value of the associated input.

The submit input will be displayed as a button (by default) that can be pressed by the user to upload the data in all the other input elements in the form to the server (in this case, just the team_name). The form attributes define the HTTP method used to send the data and the destination of the data on the server (action):

    action: The resource/URL where data is to be sent for processing when the form is submitted. If this is not set (or set to an empty string), then the form will be submitted back to the current page URL.
    method: The HTTP method used to send the data: post or get.
        The POST method should always be used if the data is going to result in a change to the server's database, because this can be made more resistant to cross-site forgery request attacks.
        The GET method should only be used for forms that don't change user data (e.g. a search form). It is recommended for when you want to be able to bookmark or share the URL.

creating the HTML, validating the returned data, re-displaying the entered data with error reports if needed can take quite a lot of effort. Django makes this a lot easier, by taking away some of the heavy lifting and repetitive code! The most fundamental tool is the Form class, which simplifies both generation of form HTML and data cleaning/validation.

Django provides numerous places where you can validate your data. The easiest way to validate a single field is to override the method clean_<fieldname>() for the field you want to check. we get our data using e.g. self.cleaned_data['renewal_date'] and that we return this data whether or not we change it at the end of the function. This step gets us the data "cleaned" and sanitised of potentially unsafe input using the default validators, and converted into the correct standard type for the data (in this case a Python datetime.datetime object). Then if a value falls outside our range we raise a ValidationError, specifying the error text that we want to display in the form if an invalid value is entered.

Creating a form using the Form class is very flexible, allowing you to create whatever sort of form page you like and associate it with any model or models. However if you just need a form to map the fields of a single model then your model will already define most of the information that you need in your form: fields, labels, help text, etc. Rather than recreating the model definitions in your form, it is easier to use the ModelForm helper class to create the form from your model. This ModelForm can then be used within your views in exactly the same way as an ordinary Form.
 All you need to do to create the form is add class Meta with the associated model (BookInstance) and a list of the model fields to include in the form (you can include all fields using fields = '__all__', or you can use exclude (instead of fields) to specify the fields not to include from the model).

**Testing a Django web application**