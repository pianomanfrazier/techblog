+++
title = "My Side Projects"
lastUpdate = true
date = "2020-08-13"
markup = "mmark"
+++

## Table of Contents

- [KnowYourTheory](#knowyourtheory)
- [Frazier Piano Studio](#frazier-piano-studio)
- [Elm Piano Teacher](#elm-piano-teacher)
- [Lilypond in Markdown](#lilypond-in-markdown)
- [Popcorn Cove Subscriptions](#popcorn-cove-subscriptions)
- [Lemmings Clone](#lemmings-clone)
- [Dr Doug's Pediatrics](#dr-dougs-pediatrics)

## KnowYourTheory

[![Know Your Theory app thumbnail](/img/projects/know-your-theory-thumbnail.png)](https://app.knowyourtheory.com)

- The app: https://knowyourtheory.com

This is the music learning platform I have been working on since fall of 2018. The front end is all in Elm.

I gave a talk at [Elm Conf 2019](/speaking#elm-conf-2019) about how I built this app. 

I am currently working and planning out the backend. My current plan is the following:

- netlify identity for authorization and authentication
- PouchDB/CouchDB for storing user data using IBM's [cloudant](https://www.ibm.com/cloud/cloudant)
- netlify functions for glueing everything together

And [here](https://www.knowyourtheory.com/posts/planned-features/) are some of my ideas for my next features.

## Frazier Piano Studio

This is my piano teaching website https://frazierpianostudio.com. I post my teaching resources and blog a little bit. 

[![Frazier Piano Studio](/img/projects/frazier-piano-studio-thumbnail.png)](https://frazierpianostudio.com)

I also put up my coding music experiments and visualizations on this site. Here are some of them.

### Music Scale Explorer

[![Music Scale Explorer](/img/projects/music-scale-explorer-thumbnail.png)](https://frazierpianostudio.com/resources/scale-explorer/)

### Circle of Fifths Explorer

[![Circle of Fifths Explorer](/img/projects/circle-of-fifths-explorer-thumbnail.png)](https://frazierpianostudio.com/resources/circle-of-fifths-explorer/)

## Elm Piano Teacher

[![Elm Piano Teacher](/img/projects/elm-piano-teacher.png)](https://elm-piano-teacher.netlify.app)

This little app is built in Elm to demonstrate music concepts for my [Elm Conf 2019 talk](/speaking#elm-conf-2019).

You will need a midi keyboard plugged into your computer and use a browser, like Chrome, that supports the web midi api.

I needed an audio and visual way to talk about music stuffs with a keyboard. It uses the WebMIDI api available in Chrome. It also uses a lot of the tooling like note and keyboard rendering I have built up for [knowyourtheory.com](https://knowyourtheory.com).

The things I added were

- sound with [Tone.js](https://tonejs.github.io/)
- midi with [WebMidi.js](https://github.com/djipco/webmidi)

I then added decoders and encoders for all the midi messages so I could handle everything else in Elm.

## Lilypond in Markdown

- GitHub: https://github.com/pianomanfrazier/lilypond-in-markdown-v2
- [Blog Post on Version 1](/post/lilypond-in-markdown/)

[![Lilypond in Markdown screenshot](/img/projects/lilypond-in-markdown.png)](https://lilypond-in-markdown.netlify.com)

This projects generates music SVG from a markdown file using GNU Lilypond. I made a custom Nunjucks tag to process the markup and inject Lilypond's SVG output into the resulting HTML file.

More about the process can be found [in this blog post](https://pianomanfrazier.com/post/lilypond-in-markdown/)

I also extended this to generate music files and play them in the browser using the output MIDI from Lilypond.

[![Lilypond audio from markdown](/img/projects/lilypond-audio-in-markdown.png)](http://lilypond-in-markdown.surge.sh)

It uses

- [LilyPond](http://lilypond.org/index.html) markup and compiler to generate music SVG
- [TiMidity++](http://timidity.sourceforge.net/) to transform the midi files
- [FFmpeg](https://ffmpeg.org/) to process the audio for the web
- [Howler.js](https://howlerjs.com/) to manage the audio in the browser

I then stitch all the sound and audio stuff together using vanilla JavaScript.

## Popcorn Cove Subscriptions

{{< youtube P_8gmr_Ol-4 >}}

I built an app to help manage subscription boxes for a popcorn candy store my sister and brother-in-law run in Washington.

- GitHub: https://github.com/pianomanfrazier/popcorncove_subscriptions

The app is built with the following

- deployed on Heroku
- python flask
- PostgresDB
- VueJS with Vuetify for the UI

## Lemmings Clone

{{< youtube knKsHbLo6Yc >}}

- GitHub: https://github.com/pianomanfrazier/lemmings-clone

I built this for my game development class in [vanilla javascript](http://vanilla-js.com/). It uses no game engine so we had to program the game loop ourselves. I learned a lot about sprite sheets and managing game state.

The levels that you see in the game were described in CSV. My goal for this was to have users be able to create their own levels and upload them. I never got that far.


## Dr Doug's Pediatrics

[![Dr. Doug's Pediatrics website](/img/projects/dr-doug.png)](https://drdougspediatrics.com/)

The website: https://drdougspediatrics.com/

This was my first freelance web project. My kid's dentist's old website was broken for mobile so I built them a new website.

The dependecies are really minimal for this project. I didn't use a framework. I stitched together some things to make it work.

- [Tachyons](http://tachyons.io/) for the CSS
- [Swiper.js](https://swiperjs.com/) for mobile image swipers
- [Zepto](https://zeptojs.com/) because I was into JQuery at the time and wanted something lighter
- [particles.js](https://vincentgarreau.com/particles.js/) for the bubble effect on the landing splash image
