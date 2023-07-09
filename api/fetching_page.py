"""Once we run requests.get, a python object is returned. It’s an instance of a class called Response that is defined
in the requests module. We won’t look at it’s definition. Think of it as analogous to the Turtle class. Each instance
of the class has some attributes; different instances have different values for the same attribute. All instances can
also invoke certain methods that are defined for the class.

In the Runestone environment, we have a very limited version of the requests module available. The Response object
has only two attributes that are set, and one method that can be invoked.

The .text attribute. It contains the contents of the file or other information available from the url (or sometimes
an error message).

The .url attribute. We will see later that requests.get takes an optional second parameter that is used to add some
characters to the end of the base url that is the first parameter. The .url attribute displays the full url that was
generated from the input parameters. It can be helpful for debugging purposes; you can print out the URL,
paste it into a browser, and see exactly what was returned.

The .json() method. This converts the text into a python list or dictionary, by passing the contents of the .text
attribute to the jsons.loads function.

The full Requests module provides some additional attributes in the Response object. These are not implemented in the
Runestone environment.

The .status_code attribute.

When a server thinks that it is sending back what was requested, it sends the code 200.

When the requested page doesn’t exist, it sends back code 404, which is sometimes described as “File Not Found”.

When the page has moved to a different location, it sends back code 301 and a different URL where the client is
supposed to retrieve from. In the full implementation of the requests module, the get function is so smart that when
it gets a 301, it looks at the new url and fetches it. For example, github redirects all requests using http to the
corresponding page using https (the secure http protocol). Thus, when we ask for
http://github.com/presnick/runestone, github sends back a 301 code and the url https://github.com/presnick/runestone.
The requests.get function then fetches the other url. It reports a status of 200 and the updated url. We have to do
further inquire to find out that a redirection occurred (see below).

The .headers attribute has as its value a dictionary consisting of keys and values. To find out all the headers,
you can run the code and add a statement print(p.headers.keys()). One of the headers is ‘Content-type’. Some possible
values are text/html; charset-utf-8 and application/json; charset=utf-8.

The .history attribute contains a list of previous responses, if there were redirects.

To summarize, a Response object, in the full implementation of the requests module has the following useful
attributes that can be accessed in your program:

.text

.url

.json()

.status_code (not available in Runestone implementation)

.headers (not available in Runestone implementation)

.history (not available in Runestone implementation)"""

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])  # print the first 150 characters
print(page.url)  # print the url that was fetched
print("------")
x = page.json()  # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2))  # pretty print the results

# parameters
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150])  # print the first 150 characters
print(page.url)  # print the url that was fetched


# -------------------------------------

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}  # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3"  # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    # return resp.json()  # Return a python object (a list of dictionaries in this case)


print(get_rhymes("funny"))


# -------------------------------------
"""
DEBUGGING
In a full python environment
In a full python environment, you will not always get a Response object back from a call to requests.get. What you get back will generally be even more informative than what you get in the Runestone environment, but you have to know where to look.

The first thing that might go wrong is that you get a runtime error when you call requests.get(dest_url). There are two possibilities for what’s gone wrong in that case.

One possibility is that the value provided for the params parameter is not a valid dictionary or doesn’t have key-value pairs that can be converted into text strings suitable for putting into a URL. For example, if you execute requests.get("http://github.com", params = [0,1]), [0,1] is a list rather than a dictionary and the python interpreter generates the error, TypeError: 'int' object is not iterable.

The second possibility is that the variable dest_url is either not bound to a string, or is bound to a string that isn’t a valid URL. For example, it might be bound to the string "http://foo.bar/bat". foo.bar is not a valid domain name that can be resolved to an ip address, so there’s no server to contact. That will yield an error of type requests.exceptions.ConnectionError. Here’s a complete error message:

requests.exceptions.ConnectionError: HTTPConnectionPool(host='foo.bar', port=80): Max retries exceeded with url: /bat?key=val (Caused by <class 'socket.gaierror'>: [Errno 11004] getaddrinfo failed)
The best approach is to look at the URL that is produced, eyeball it, and plug it into a browser to see what happens. Unfortunately, if the call to requests.get produces an error, you won’t get a Response object, so you’ll need some other way to see what URL was produced. The function defined below takes the same parameters as requests.get and returns the URL as a string, without trying to fetch it.

import requests
def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

print(requestURL(some_base_url, some_params_dictionary))
Assuming requestURL() returns a URL, match up what you see from the printout of the params dictionary to what you see in the URL that was printed out. If you have a sample of a URL from the API documentation, see if the structure of your URL matches what’s there. Perhaps you have misspelled one of the API parameter names or you misspelled the base url.

You can also try cutting and pasting the printed URL into a browser window, to see what error message you get from the website. You can then try changing the URL in the browser and reloading. When you finally get a url that works, you will need to translate the changes you made in the url back into changes to make to your baseurl or params dictionary.

If requests.get() executes without generating a runtime error, you are still not done with your error checking. No error means that your computer managed to connect to some web server and get some kind of response, but it doesn’t mean that it got the data you were hoping to get.

Fortunately, the response object returned by requests.get() has the .url attribute, which will help you with debugging. It’s a good practice during program development to have your program print it out. This is easier than calling requestURL() but is only available to you if requests.get() succeeds in returning a Response object.

More importantly, you’ll want to print out the contents. Sometimes the text that’s retrieved is an error message that you can read, such as {"request empty": "There is no data that corresponds to your search."}. In other cases, it’s just obviously the wrong data. Print out the first couple hundred characters of the response text to see if it makes sense.

import requests
dest_url = <some expr>
d = <some dictionary>
resp = requests.get(dest_url, params = d)
print(resp.url)
print(resp.text[:200])
Now you try it. Use requests.get() and/or requestURL() to generate the following url, https://www.google.com/search?tbm=isch&q=%22violins+and+guitars%22. (Don’t look at the previous page of the textbook, at least not yet. If you can’t figure it out after 15 minutes of trying the approaches on this page, then look back.)
"""
