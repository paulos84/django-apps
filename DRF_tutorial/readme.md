http://www.django-rest-framework.org/#tutorial

Complete code used in this tutorial: https://github.com/encode/rest-framework-tutorial

Notes
-----
**Serialization**
To provide a way of serializing and deserializing the snippet instances
into representations such as json. We can do this by declaring
 serializers that work very similar to Django's forms. Like forms has
 ModelForm class as well as Form, ModelSerializer classes are simply a
 shortcut for creating serializer classes:

   An automatically determined set of fields.

   Simple default implementations for the create() and update() methods.

   The above are automatically created based upon the specified model,
   instead of writing out these generic pattern everytime as you would
   otherwise usually do when serializing models.

**Views**
In example of FBV with @api_view decorator, notice that we're no longer
 explicitly tying our requests or responses to a given content type.
 request.data can handle incoming json requests, but it can also handle
 other formats. Similarly we're returning response objects with data,
 but allowing REST framework to render the response into the correct
 content type for us.

To take advantage of the fact that our responses are no longer hardwired
 to a single content type let's add support for format suffixes to our
 API endpoints. Using format suffixes gives us URLs that explicitly
 refer to a given format, and means our API will be able to handle URLs
 such as http://example.com/api/items/4.json.

Start by adding a format keyword argument to both of the views, like so:

def snippet_list(request, format=None):

...

def snippet_detail(request, pk, format=None):

...

