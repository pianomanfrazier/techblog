+++
title = "Write a Book with Markdown"
date = 2019-11-27
draft = false
+++

I have been working on my book [Learn Elm by Example -- Build a calculator](/courses/) and have developed several scripts to generate PDF and epub from markdown files. I am going to detail my process and gotchas of writing a book with markdown.

On twitter I have seen developers selling ebooks and making good money. Their posts say something like, "I wrote this book and made a billion dollars on my first day." Then they tell you how they did it, except they leave out all the details like how do you make a nice looking PDF and epub.

My requirements for writing a book are the following:

- write in markdown
- source control everything
- output to PDF, epub, mobi, HTML
- code syntax highlighting (because I am writing a technical programming book)

When looking for some options to write a book I found two projects that almost fit my needs.

## Alternative projects

### [MagicBook](https://github.com/magicbookproject/magicbook)

There is no output to epub or mobi and the project seems abandoned on GitHub. The latest commit was several years ago.

### [BookDown](https://bookdown.org/yihui/bookdown/)

BookDown is an R package, so you will need to install R and be somewhat familiar with how R packages work and how to run R programs. You can write a book with the package without actually writing or knowing how to program in R though.

The HTML output looks like GitBook with a couple of added features like embedding R code output like diagrams. It also outputs to really nice looking PDFs.

## My tech stack

- [Pandoc](https://pandoc.org/)
- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) --- a Pandoc filter
- [Eisvogel latex template](https://github.com/Wandmalfarbe/pandoc-latex-template)
- [gumroad](https://gumroad.com/) --- sell digital products online

I wanted to do the simplest thing possible to write a book. I chose to use Pandoc and make everything work from there. Pandoc has an example in their documentation [here](https://pandoc.org/epub.html) which got me close but I needed to make a bunch of customizations to make a decently good looking book.

I made three scripts to output the formats I wanted, PDF, epub, and HTML. It took some fiddling with Pandoc to get good looking output for each format.

## Project structure

Each chapter of the book lives in a separate markdown folder. If you order the files by number the order comes out correctly. The files should look like the following:

```bash
src
├── 01-intro.md
├── 02-setup.md
└── title.txt
```

The trickiest part was configuring the `title.txt`. This is the yaml meta-data for the book. These variables get read into the templates for whatever format Pandoc is rendering to.

```yaml
---
title: Some Markdown Book
subtitle: Everything is awesome
author: Ryan Frazier
...
---
```

## Make a cover page

I designed a cover page in Gimp to the exact page size of the book page size for the PDF. In this case standard letter size.

I then altered the Latex template to include the front page PDF as the first page. This was the easiest way I could find to get a good looking book cover. I tried to write some Latex to generate one but couldn't get anything to look good.

After I designed a cover in Gimp I exported the image in PDF for the PDF book and as PNG for the epub.

## PDF script

```bash
# pandoc version 2.7.3
mkdir -p build

pandoc \
    --pdf-engine=xelatex \
    --template=./templates/eisvogel.latex \
    --highlight-style tango \
    --toc -N \
    --filter pandoc-crossref \
    -o build/output.pdf \
    src/title.txt src/*.md
```

## epub script

```bash
# pandoc version 2.7.3
mkdir -p build

pandoc \
    --filter pandoc-crossref \
    --css templates/epub.css \
    --toc -N \
    -o build/output.epub \
    src/title.txt src/*.md
    # -f markdown+smart -t markdown-smart \
```

I have an android phone so I use the [ReadEra](https://play.google.com/store/apps/details?id=org.readera) app to test it out. On a small device it is **way** easier to read an ebook this way.

I generated the epub styles from the default Pandoc template by running `pandoc -D epub`. Epub format is like writing old CSS from 10 years ago. Things might turn out weird depending on your ereader.

## mobi kindle format

If you want to get the mobi format you will need to get the [kindlegen](https://www.amazon.com/gp/feature.html?docId=1000765211) program from amazon.

You can then feed the epub file to kindlegen to get a mobi book.

```bash
kindlegen ./build/output.epub
```

## HTML format

Since I am planning on selling this book on Gumroad I haven't spent very much time getting the HTML to look good. I discovered that Pandoc provides a slidy template that works pretty good to read from without any effort.

The PDF is slow to render so if you want some immediate feedback how your text will read try the HTML.

## Some markdown gotchas

If you are writing lots of math equations using Latex then epub will not look good at all. PDF will look great and HTML will need some tweaking. You can choose to render your math in HTML with MathJAX or Katex. I didn't need math stuffs so I didn't bother.

The smart markdown extension seemed to break on epub output. The smart extension formats things like `---` to `&mdash;`.

When writing with lots of figures I like to call out the figures in the text. I use the pandoc-crossref filter to get this. It does deviate from standard markdown so your markdown does lose some portability. These figure references work well for all outputs.

```md
![Some image](/img/some-image.png){#fig:someimage}

And then it can be referenced in the text. See [#fig:someimage].
```

## Get the code

I have put all my scripts up on GitLab [here](https://gitlab.com/pianomanfrazier/pandoc-markdown-book). Let me know if you write anything cool with it.

