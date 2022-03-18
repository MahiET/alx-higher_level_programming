# 0x11. Python - Network #1

urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.

<h2>Fetching URLs</h2>

If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the shutil.copyfileobj() and tempfile.NamedTemporaryFile() functions:

         import shutil
	 
         import tempfile
	
         import urllib.request


         with urllib.request.urlopen('http://python.org/') as response:

         with tempfile.NamedTemporaryFile(delete=False) as tmp_file:

         shutil.copyfileobj(response, tmp_file)


         with open(tmp_file.name) as html:

         pass

<h2>Data</h2>

Sometimes you want to send data to a URL (often the URL will refer to a CGI (Common Gateway Interface) script or other web application). With HTTP, this is often done using what’s known as a POST request. This is often what your browser does when you submit a HTML form that you filled in on the web. Not all POSTs have to come from forms: you can use a POST to transmit arbitrary data to your own application. In the common case of HTML forms, the data needs to be encoded in a standard way, and then passed to the Request object as the data argument. The encoding is done using a function from the urllib.parse library.

             import urllib.parse
             import urllib.request

          url = 'http://www.someserver.com/cgi-bin/register.cgi'
          values = {'name' : 'Michael Foord',
                        'location' : 'Northampton',
                        'language' : 'Python' }

            data = urllib.parse.urlencode(values)
            data = data.encode('ascii') # data should be bytes
            req = urllib.request.Request(url, data)
            with urllib.request.urlopen(req) as response:
                the_page = response.read()

<h2>Headers</h2>


Some websites  dislike being browsed by programs, or send different versions to different browsers. By default urllib identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the Python release, e.g. Python-urllib/2.5), which may confuse the site, or just plain not work. The way a browser identifies itself is through the User-Agent header . When you create a Request object you can pass a dictionary of headers in. The following example makes the same request as above, but identifies itself as a version of Internet Explorer

      import urllib.parse
      import urllib.request

          url = 'http://www.someserver.com/cgi-bin/register.cgi'
         user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
         values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python' }
         headers = {'User-Agent': user_agent}

       data = urllib.parse.urlencode(values)
       data = data.encode('ascii')
       req = urllib.request.Request(url, data, headers)
       with urllib.request.urlopen(req) as response:
       the_page = response.read()
   