+++
title = "Add Tags to Hugo Theme"
date = 2019-09-25
draft = false
markup = "mmark"
+++

To add support for tags in a Hugo theme you need two pieces. One template to render the list of tags and another to render the list of everything under that tag. After wading through Hugo's documentation several times I am documentating the process here.

Hugo's template [lookup order](https://gohugo.io/templates/lookup-order/) can be overwhelming. I recognize it's power, but to add a simple feature to a blog theme it can be too much.

Here is a simple way to add tag support. You will need two files.

```go-html-template
{{/* layouts/taxonomy/terms.html */}}

{{ partial "header.html" . }}

<section>
  <h1>Tags</h1>
  <ul>
    {{ range .Data.Terms.Alphabetical }}
      <li>
        <h2>
          <a href="{{ .Page.Permalink }}">({{ .Count }}) {{ .Page.Title }}</a>
        </h2>
      </li>
    {{ end }}
  </ul>
</section>

{{ partial "footer.html" . }}
```

```go-html-template
{{/* layouts/taxonomy/list.html */}}

{{ partial "header.html" . }}

<section>
  <h1>Tag: {{ .Title }}</h1>
  <ul>
    {{ range .Pages }}
      <li>
        <h2>
          <a href="{{ .Permalink }}">{{ .Title }}</a>
        </h2>
        <time>{{ .Date.Format (.Site.Params.dateform | default "January 2006") }}</time>
      </li>
    {{ end }}
  </ul>
</section>

{{ partial "footer.html" . }}
```

