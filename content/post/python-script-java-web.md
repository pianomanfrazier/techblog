+++
title = "Python Script a Java Web Application"
date = 2019-06-04
draft = false
tags = ["python","productivity"]
markup = "mmark"
+++

In this post I am going to describe my process for providing a simple way to run scripts on a web application. I work on a fairly mature Java web application and writing a web front end for every administration task can be tedious and take too much time.

These tasks might be to generate a report for the client or do some complicated data migration. The script could also allow you to inspect some data and then create a response to send back to the server.

This approach also has the added benefit of being able to cache all my taken actions. This way I can run a report or do a data migration on our **staging environment** and then use the cached version on **production**. No need to do the same thing twice.

## Grab Your Auth Token

You will need to grab your session id or whatever authentication token your app uses. You could write a client that logs in using your credentials but I wanted to keep things simple. Here is what I grab for our application:

{{< figure
  src="/img/script_java/jsession-id.png"
  alt="Grab the JSESSIONID"
  title="Grab the JSESSIONID"
  caption="Grab the JSESSIONID in the network tools"
>}}

## The Script

Copy and paste the auth ID into the script below. You may need to change the cookie or header depending on your application authentication strategy.

```python
import requests

# grab this from the browser network tools
SESSION_ID = "<YOUR SESSION ID>"

COOKIES = {
  'JSESSIONID': SESSION_ID,
}
HEADERS = {
  'Cookie': f'JSESSIONID={SESSION_ID};',
  'Content-Type': 'application/json',
}
BASE_URL = 'http://localhost:8080' # or 'https://production.site
ENDPOINT = '/api/v1/some/endpoint'

def main():
  res = requests.get(BASE_URL + ENDPOINT, cookies=COOKIES, headers=HEADERS)

  # make some JSON thing to update server endpoint
  data = {'some': 'data'}
  res = requests.put(f'{BASE_URL}{ENDPOINT}', data=json.dumps(data), cookies=COOKIES, headers=HEADERS)
  print(res)

if __name__ == "__main__":
  main()
```

## Pretty Print the JSON Response

Pretty print of the response is helpful when debugging these scripts.

```python
def prettyPrint(r):
  print("URL: ", BASE_URL + ENDPOINT)
  print("STATUS: ", r.status_code)
  parsed = json.loads(r.text)
  print(json.dumps(parsed, indent=4))
```

## Pickle Actions

If you want to rerun your script with the same actions you took previously, you should stash your responses in a dictionary and then fetch them in subsequent runs.

The pickle module is perfect for this.

> The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
Quote: -- [The Pickle Documentation](https://docs.python.org/3.5/library/pickle.html)

What this means is that you can save off any python object and retrieve it for later.

```python
import pickle
import requests

def main():
  # declare the cached map global so you can use
  # throughout your script
  global CACHE_MAP

  # load the pickled actions on script startup 
  PICKLE_FILE = 'my.pickle'
  try:
    with open(PICKLE_FILE, 'rb') as fin:
      CACHE_MAP = pickle.load(fin)
    print(f'Loaded {PICKLE_FILE} file')
  except FileNotFoundError:
    print(f'No {PICKLE_FILE} file found')

  # resume script as before
  res = requests.get(BASE_URL + ENDPOINT, cookies=COOKIES, headers=HEADERS)
  
  if 'somekey' in CACHE_MAP.keys():
    data = CACH_MAP['somekey']
  else:
    data = {'some': 'data'}
    # cache the new data for later
    CACHE_MAP['somekey'] = data
    # update the pickle files
    with open(PICKLE_FILE, 'wb') as fout:
        pickle.dump(CACHE_MAP, fout)

  res = requests.put(f'{BASE_URL}{ENDPOINT}', data=json.dumps(data), cookies=COOKIES, headers=HEADERS)

if __name__ == "__main__":
  main()
```

## Conclusion

I have found this to be a quick way to automate tasks that I previously needed a web front-end for. I have a handful of these scripts for generating reports and running one-off data migration tasks.

