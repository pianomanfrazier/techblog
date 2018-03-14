+++
title= "Comparing Hugo and Gatsby Static Site Generators"
date= 2018-03-13T16:25:00-06:00
draft=false
markup= "mmark"
+++

## What is a static site generator?

Input your files (i.e. templates, themes,...) and data (i.e. markdown or headless WordPress) and out comes static files such as html, css, and javascript. You can then host the site just about anywhere for quite cheap or free. The advantages of this are cheaper hosting, better security, faster website and you can deploy the site easily through a CDN.

## Roll your own

[<img alt="flask logo" src ="/img/gatsby_vs_hugo/flask.svg" style="max-height:140px"/>](http://flask.pocoo.org)

You can get up and running fast. The application is simple to reason about. Custom pages and routes are easy to define. It is very flexible. The templating engine Jinja is my favorite. I have tried Go templates, Jade, Embedded JS and I always find myself missing features in Jinja such as inheritance, filters, and blocks. I was happy to find out that Mozzilla ported Jinja to JavaScript with Nunjucks. I am definitely using Nunjucks for my next NodeJS project.

Back to Flask. Of course you will have to do a lot of things yourself, however some things I found to be a pain that are just included with a static site generator framework like a sitemap and rss feeds.

A simple implementation in Flask takes less than a hundred lines. There are two key parts to making this work. Frozen Flask will traverse your application and create static assets. The other key part is the custom markdown filter applied to the Jinja templates.

```python
from flask import Flask, render_template
import markdown
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.jinja_env.filters['markdown'] = lambda text: markdown.markdown(text, extensions=['markdown.extensions.tables'])

@app.route('/posts/<string:title>/')
def posts(title=none):
  if title != none:
    md_text=""
    _file = '../posts/' + title + ".md"
    with open(_file) as fout:
      md_text = fout.read()
    return render_template('posts.html', md_text=md_text)

@freezer.register_generator
def posts_generator():
  yield '/posts/my-first-post/'
  yield '/'

freezer.freeze()
```

The template `posts.html` with the filter would look like:

```jinja
<html>
<body>
<div class="content"
{{ md_text | markdown | safe }}
</div>
</body>
</html>
```

Go to [Flask Static Gen](https://github.com/pianomanfrazier/flask-static-gen) to see a minimal working example.


## Gatsby

[<img alt="gatsby logo" src ="/img/gatsby_vs_hugo/gatsby.svg" style="max-height:140px"/>](https://www.gatsbyjs.org)

Gatsby markets itself as a website compiler. Out of the box you get a lightning fast website built with Webpack and React. There is a lot of support behind React so figuring out how to do something is quite easy or it has already been done.

Gatsby feels a bit more raw. It is somewhere between the Flask way and Hugo for blogging. You still have a bit of work to do to get a blog up and running. You can't simply download a theme and start using it. If you are a developer comfortable with React and puting all the pieces together this method is great.

One excellent feature of Gatsby is that is uses GraphQL to pull in data. To build a snappy custom blog powered by Wordpress on the backend would be a great use case. If I were building a blog for a client I would definitely go this route. However I like having the flexibility as a developer when creating my own content. This is where I miss having the shortcode feature. If you want to use WordPress then you would be able to use the shortcode. However, I prefer writing my posts in plain flat files that are version controlled. For non-tech users WordPress has a great UI.

### Pros

- GraphQL
- turn blog into React web app
- super fast website out of the box

### Cons

- cannot create posts with CLI
- remark (Gatsby's default markdown renderer) currently has no easy shortcode support. There is [this plugin](https://github.com/djm/remark-shortcodes); however, it would take some work to get it all hooked up. This would be a good future Gatsby plugin.
- No "themes." However there are [Gatsby starters](https://www.gatsbyjs.org/docs/gatsby-starters/) to get you going. Not as easy as starting with Hugo or Wordpress themes.

## Hugo

[<img alt="hugo logo" src ="/img/gatsby_vs_hugo/hugo.svg" style="max-height:140px"/>](https://www.gohugo.io)

I have used Hugo for this blog, my [piano website](https://frazierpianostudio.com), and the [documentation for a project at work](https://di2e.github.io/openstorefront). For the documentation Hugo worked out great. It was easy to bring new team members up to speed on how to update the documentation. Hugo is easy to install and all they had to do was edit or create new markdown files. We did have to work around how Github publishes its pages. Github will serve anything found in the `docs` directory of the repo. If you want to use Jekyll you can place your Jekyll site there and Github will build it for you. Since all the developers are using Windows and setting up Ruby is quite painful on Windows I ruled that option out. The solution was to create a separate directory to host the Hugo files and then at release time we build to site and commit it to the `docs/` directory. For updating the docs developers use the `hugo server`.

The reason I love Hugo is for its shortcode feature and its great command line interface. If I am writing a post and want some special html button thing I can create a shortcode easily and use it in the markdown. To start a new post use the CLI by `hugo new post/my-new-post.md` and Hugo will use the archetypes template file to create a new post ready to edit.

The Go templating language is not as nice as the other two. It feels very counter intuitive. Jinja and React templates feel just like writing Python and JavaScript. Perhaps if I knew Go better the templating would not feel so difficult. Having written a theme from scratch in Hugo I still have to look up the syntax for the templates. The parameters for functions are also very finicky. Somehow the format string for dates `"Janurary 6, 2016"` doesn't  parse but `"January 2, 2006"` does.

Hugo also includes an extended markdown parser called mmark. It allows for tables, letter ordered lists, figures, citations, including files, latex (provided you have MathJax or Katex support for your website), and more. See the full [mmark spec](https://github.com/miekg/mmark/wiki/Syntax).

### Pros

- shortcodes
- mmark
- awesome CLI
- [lots of themes](https://themes.gohugo.io/) Download a theme and start blogging.

### Cons

- Go templates somewhat painful

## Conclusion

For now I will continue to use Hugo. I will be closely watching Gatsby development though.
