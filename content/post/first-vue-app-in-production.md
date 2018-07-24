+++
title = "First Vue App in Production"
date = 2018-07-24T17:08:05-06:00
draft = true
markup = "mmark"
+++

I have been tasked with rewriting portions of our current Ext JS application in Vue.js to better work with mobile devices. This post is some thoughts about my experience building a larger application in Vue.

- Vue cli webpack `vue init webpack <new project>`
- Vuetify
- Vuex (used to store security policy, user profile, and branding)

Some useful components that were added in addition to Vuetify:

- [Vue-star-rating](https://github.com/craigh411/vue-star-rating/)
- [Vue-toasted](https://github.com/shakee93/vue-toasted)
- [Date fns](https://date-fns.org/)
- [vue-truncate-filter](https://github.com/imcvampire/vue-truncate-filter)

Components we had to build ourselves:

- lightbox viewer

## Philosopy about breaking up the code

Don't be afraid of large file size. [Evan Czaplicki - The life of a file](https://youtu.be/XpDsk374LDE)

Split into a component if the code can be reused. If you are creating components just to create components then you are wasting your time. Don't create a component that has a one line template calling out another component. This is wasted abstraction.

Consitency across the application:

- margin spacing
- button style
- show loading spinner on every async interaction

## Other problems

- spliting out appropriately small tasks (experience helps in this regard)

I have several students who work under me and having small tasks to give them sure sped things up. Using code reviews as a mentoring opportunity.
