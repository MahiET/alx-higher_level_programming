# 0x10. Python - Network #0

HTTP (HyperText Transfer Protocol)
=

Many applications are running concurrently over the Web, such as web browsing/surfing, e-mail, file transfer, audio & video streaming, and so on.  In order \
for proper communication to take place between the client and the server, these applications must agree on a specific application-level protocol such as HTT\
P, FTP, SMTP, POP, and etc.

HyperText Transfer Protocol (HTTP)
=

* HTTP is an asymmetric request-response client-server protocol as illustrated.An HTTP client sends a request message to an HTTP server.  The server, in tur\
n,returns a response message.  In other words, HTTP is a pull protocol, the client pulls information from the server (instead of server pushes information d\
own to the client).

* HTTP is a stateless protocol. In other words, the current request does not know what has been done in the previous requests.

* HTTP permits negotiating of data type and representation, so as to allow systems to be built independently of the data being transferred.

HTTP Protocol
=

As mentioned, whenever you enter a URL in the address box of the browser, the browser translates the URL into a request message according to the specified p\
rotocol; and sends the request message to the server.

For example, the browser translated the URL http://www.nowhere123.com/doc/index.html into the following request message:

           GET /docs/index.html HTTP/1.1
           Host: www.nowhere123.com
           Accept: image/gif, image/jpeg, */*
           Accept-Language: en-us
           Accept-Encoding: gzip, deflate
           User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
           (blank line)


