+++
title = "Render LilyPond in Markdown"
date = 2019-05-15
draft = false
markup = "mmark"
tags = ["javascript", "lilypond", "ssg"]
+++

- **Demo:** https://lilypond-in-markdown.netlify.com
- **LilyPond Syntax Highlight Demo:** https://lilypond-in-markdown.netlify.com/lilycode
- **Repository:** https://github.com/pianomanfrazier/lilypond-in-markdown

I want to write [LilyPond](http://lilypond) code, a music typesetting markup language, directly in a markdown file and have it rendered directly to embeded SVG in an HTML page. This post explores the process I went through to get this working.

My typical workflow when writing about music on the web is to make a music image and then reference it in the markdown as an image. When doing lots of examples this gets tedious and my source files for the images are not contained within my content.

## What is LilyPond?

LilyPond is a markup language similar to LaTeX but for making music scores. LilyPond takes an input text file like the following

{{< readfile file="/data/lilypond-highlight/piano-score.html" >}}

and it would render to this

{{< figure
  src="/static/img/lilypond_in_markdown/piano_score.min.svg"
  alt="Example LilyPond Output"
  title="Example LilyPond Output"
  caption="Example LilyPond Output"
  style="max-width: 300px !important;"
  inlineSVG="true"
>}}

## Proposed API

If I were using Hugo, my markdown file would contain something like this

```txt
## Some LilyPond Markdown

{{</* lilypond */>}}
\score{
    \relative c'' {
        % some notes
        g8 e \tuplet 3/2 { f[ a c] } e d a b c4
    }
    \layout{}
}
{{</* \lilypond */>}}
```

## Hugo's Shortcomings 

The Hugo developers have chosen [not to allow an exec shortcode](https://github.com/gohugoio/hugo/issues/796). This would allow theme developers to execute arbitrary code on users machines and therefore seen as a security risk.

## Custom Nunjucks Tag

Since I can't do it in Hugo I looked for another <abbr title="Static Site Generator">SSG</abbr> that had a more flexible (and dangerous) template system. I love the jinja2 api so I tried the JS port Nunjucks. Nunjucks allows you to define [custom tags](https://mozilla.github.io/nunjucks/api.html#custom-tags). 

I had a working prototype of Nunjucks just rendering some lilypond from a custom tag. Now I needed an <abbr title="Static Site Generator">SSG</abbr> that would allow access to the Nunjucks API. So I went to [StaticGen.com](https://www.staticgen.com/) and filtered by template type.

I tried out [11ty](https://www.11ty.io/) and it worked out great.

The resulting call in my markdown looks like this
```jinja
{% lilypond 'inline', 'preview', '0.7 in' %}
\score{
  \relative c'' {
    % some notes
    c d e f g
  }
  \layout{}
}
{% endlilypond %}
```

In my `.eleventy.config` I define a new Nunjucks tag

```js
// The Lilypond extension
eleventyConfig.addNunjucksTag("lilypond", function(nunjucksEngine) {
  return new function() {
    // this block is from the Nunjucks docs
    // see https://mozilla.github.io/nunjucks/api.html#custom-tags
    this.tags = ['lilypond'];
    this.parse = function(parser, nodes, lexer) {
        var tok = parser.nextToken();
        var args = parser.parseSignature(null, true);
        parser.advanceAfterBlockEnd(tok.value);
        var body = parser.parseUntilBlocks('endlilypond');
        parser.advanceAfterBlockEnd();
        return new nodes.CallExtensionAsync(this, 'run', args, [body]);
    };
    // this is where the real processing occurs
    this.run = function(context, param, body, callback) {
      // hash the input so we can cache it for later
      let hash = MD5(body())
      // check if hash already exists in the cache
      // if cache miss then process the lilypond code
      fs.writeFile(${outputDir}/${hash}.ly, body(), function(err) {
        exec(`lilypond -dbackend=svg --output=${outputDir} ${outputDir}/${hash}.ly`
        , function(err, stdout, stderr) {
          // read contents of output LilyPond SVG
          // cache the result
          let ret = new nunjucksEngine.runtime.SafeString(lilypondSVG)
          // End the processing
          callback(null, ret);
          )
        })
      }
    }
```

I skipped a couple of things to make the example more readable.

- optimize the output SVG with [svgo](https://github.com/svg/svgo)
- minify the html with [html-minifier](https://www.npmjs.com/package/html-minifier)
- cache the final output by the hash to retrieve it next time

See [the code](https://github.com/pianomanfrazier/lilypond-in-markdown/blob/c2ba87e26bc867ffc3163e3532038518f11e7e31/.eleventy.js#L130) for the full example.

## Highlight LilyPond Code

There are no good LilyPond syntax highlighters for the web. With Highlight.js, Prism.js, or Hugo you could use `tex` or `latex` highlighting but the results aren't great. I made an attempt at defining my own Prism.js syntax but ended up with a huge nasty regex.

A much better solution is to use an actual parser/lexer. Fortunately [python-ly](https://github.com/frescobaldi/python-ly) exposes an API to highlight lilypond code through the command line.

Python-ly is a command line tool used to process LilyPond files. You can transpose, reformat, and output syntax highlighted html from an input file. This is what the [Frescobaldi LilyPond editor](http://frescobaldi.org/index.html)  uses to highlight and manipulate LilyPond files.

After poking around and discovering some undocumented ways of using the python-ly CLI, I had something that provided some great syntax highlighting.

Compare the difference between the outputs of Hugo, PrismJS, and python-ly (screen shots taken from [lilypond in markdown](https://lilypond-in-markdown.netlify.com) and [python-ly highlight test](https://lilypond-in-markdown.netlify.com/lilycode)):

### Hugo using Chroma

Here is some lilypond using the `latex` highlight in Hugo (Chroma):
```latex
\score{
	\relative c'' {
      c8 | c8([ bes)] a a([ g)] f | f'4. b, | c4.~ c4
	}
	\layout{}
}
```

The only thing that gets highlighted are things preceded by a slash `\`.

### PrismJS

And here is PrismJS with my own LilyPond definition.

Since Prism is using regex, it is hard to separate different contexts between strings or note names like in `hills a -- dorn`.

{{< figure src="/img/lilypond_in_markdown/prism_highlight.png" alt="Prism Highlight" title="Prism Highlight" caption="Prism Highlight with Regex" >}}

### Python-Ly

And finally python-ly. I am using my own custom CSS to style the output. Each parsed token is wrapped in a span with a class name.

{{<
  figure src="/img/lilypond_in_markdown/python-ly_highlight.png"
  alt="python-ly Highlight"
  title="python-ly Highlight"
  caption="python-ly Highlight with custom CSS"
>}}

## Custom Nunjucks Highlight Tag

I added another Nunjucks custom tag using the same method as before. This time I pass `body()` to `python-ly`.

```js
// LilyPond Syntax highlight extension
eleventyConfig.addNunjucksTag("lilycode", function(nunjucksEngine) {
  return new function() {
    // define and parse tags
  }
  this.run = function(context, body, callback) {
    let execString = `
      echo "${body()}" |
      ly highlight -d full_html=false -d wrapper_tag=code -d document_id=language-lilypond
      `;
    exec(execString, function(err, stdout, stderr) {
      // wrap the code block with a pre as per convention
      let formatedHtml = `<pre class="language-lilypond">${stdout}</pre>`;
      let ret = new nunjucksEngine.runtime.SafeString(formatedHtml);
      callback(null, ret);
  }
}
```
See [the actual code](https://github.com/pianomanfrazier/lilypond-in-markdown/blob/master/.eleventy.js#L80).

You can then style the output however you like. Here I am using a monokai inspired theme based on the Prism Okaidia theme. See [my css](https://github.com/pianomanfrazier/lilypond-in-markdown/blob/master/css/lilypond.css).

To use the custom tag it looks like

```jinja
{% lilycode %}
\score{
  \relative c'' {
    % some notes
    c d e f g
  }
  \layout{}
}
{% endlilycode %}
```

## Conlusion

What I have learned from this process is that Hugo is great for blogging for most use cases. If you need a more powerful template system to process your markdown files try 11ty. I found 11ty easy to use with good documentation.
