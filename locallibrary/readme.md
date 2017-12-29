Source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

The tutorial is adapted to use Django2.0. Therefore it uses django.urls.path() and django.urls.re_path() instead of django.conf.urls.url()

It covers the following topics in addition to the basics:

Sessions framework, User authentication and permissions, Django Testing, Deploying Django to production and Web application security

**What are sessions?**
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

