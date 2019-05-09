+++
title = "Render Lilypond in Markdown"
date = 2019-05-15
draft = true
markup = "mmark"
+++

- Demo: https://lilypond-in-markdown.netlify.com
- Repository: https://github.com/pianomanfrazier/lilypond-in-markdown

## Hugo's Shortcomings 

The Hugo developers have chosen not to allow an exec shortcode. This would allow theme developers to execute arbitrary code on users machines and therefore seen as a security risk. This would be useful for developers because there are times when you could process some piece of data and return some html.

I have long wanted to write [LilyPond](http://lilypond) in a markdown file and have it render as a music image. In Hugo this would look something like

```txt
# Some LilyPond Markdown

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

## Custom Nunjucks Tag

Since I can't do it in Hugo I looked for another <abbr title="Static Site Generator">SSG</abbr> that had a more flexible (and dangerous) template system. I love the jinja2 api so I tried the JS port Nunjucks. Nunjucks allows you to define [custom tags](https://mozilla.github.io/nunjucks/api.html#custom-tags). 

I had a working prototype of Nunjucks just rendering some lilypond from a custom tag. Now I needed an <abbr title="Static Site Generator">SSG</abbr> that would allow access to the Nunjucks API. So I went to [StaticGen.com](https://www.staticgen.com/) and filtered by template type.

I tried out [11ty](https://www.11ty.io/) and it worked out great. 11ty is a very flexible static website builder framework.

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

# Highlight LilyPond Code

There are no good LilyPond syntax highlighters for the web. With Highlight.js ,Prism.js, or Hugo you could use `tex` but the results aren't great. I made an attempt at defining my own Prism.js syntax but ended up with a huge nasty regex.

A much better solution is to use an actual parser/lexer. Fortunately [python-ly](https://github.com/frescobaldi/python-ly) exposes an API to highlight lilypond code through the command line. This is what the Frescobaldi LilyPond editor uses to highlight.

After poking around and discovering some undocumented ways of using the python-ly CLI I had something that provided some great syntax highlighting.

Compare the difference between the two outputs (screen shots taken from [lilypond in markdown](https://lilypond-in-markdown.netlify.com) and [python-ly highlight test](https://lilypond-in-markdown.netlify.com/lilycode)):

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

F>![Prism Highlight](/img/lilypond_in_markdown/prism_highlight.png)
Figure: Prism Highlight with Regex 

F>![python-ly Highlight](/img/lilypond_in_markdown/python-ly_highlight.png)
Figure: python-ly Hightlight

Since Prism is using regex it is hard to separate different contexts between strings or note names like in `hills a -- dorn`.

I added another Nunjucks custom tag using the same method as before. This time I pass `body()` to `python-ly`.

```js
// LilyPond Syntax highlight extension
eleventyConfig.addNunjucksTag("lilycode", function(nunjucksEngine) {
  return new function() {
    // define and parse tags
  }
  this.run = function(context, body, callback) {
    let execString = `echo "${body()}" | ly highlight -d full_html=false -d wrapper_tag=code -d document_id=language-lilypond`;
    exec(execString, function(err, stdout, stderr) {
      // wrap the code block with a pre as per convention
      let formatedHtml = `<pre class="language-lilypond">${stdout}</pre>`;
      let ret = new nunjucksEngine.runtime.SafeString(formatedHtml);
      callback(null, ret);
  }
}
```
See [the actual code](https://github.com/pianomanfrazier/lilypond-in-markdown/blob/master/.eleventy.js#L80).

You can then style the output however you like. Here I am using a monokai inspired theme based on the Prism Okaidia theme. See my [the css](https://github.com/pianomanfrazier/lilypond-in-markdown/blob/master/css/lilypond.css).

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
