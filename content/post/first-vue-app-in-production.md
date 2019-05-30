+++
title = "First Vue App in Production"
date = 2018-09-24T17:08:05-06:00
draft = false
markup = "mmark"
tags = ["vuejs", "javascript"]
+++

At work I have been tasked with rewriting portions of our current Ext JS application in Vue.js to work better with mobile devices. This post is some thoughts about my experience building a larger application in Vue. The Vue mobile client has around 12 different pages.

## Tooling and Libraries

Here are some of the tools I used for the project:

- Vue cli webpack `vue init webpack <new project>`
- Vuetify
- Vuex (used to store security policy, user profile, and branding)

Some useful components and libraries in addition to Vuetify:

- [Vue-star-rating](https://github.com/craigh411/vue-star-rating/)
- [Vue-toasted](https://github.com/shakee93/vue-toasted)
- [Date fns](https://date-fns.org/)
- [vue-truncate-filter](https://github.com/imcvampire/vue-truncate-filter)

Components we had to build ourselves:

- lightbox viewer

## Philosophy About Files and Components

Don't be afraid of large file size. [Evan Czaplicki - The life of a file](https://youtu.be/XpDsk374LDE)

We chose to use single file Vue components. It is clear where the logic, view, and styling are in the file. We chose to break up a component into smaller pieces only if we needed some function elsewhere. Managing a lot of needless component props is not fun.

## Other problems

Since this was my first time leading a small team in a new feature I learned a lot. I realized the importance of splitting up tasks into small chunks.

I have several students who work under me and having small tasks to give them sure sped things up. I also used code reviews as a mentoring opportunity.

One thing I was not expecting was keeping design consistency across the application. These issues included:

- margin spacing
- button style
- show loading spinner on every async interaction

## Conclusion

The development experience shipping a Vue app was nice. Having worked on ExtJS in the previous version of the application, Vue was refreshing. I had a lot of control over how things worked and looked. Vuetify provided a lot of functionality and got things going fast. When I needed a custom component, I had the freedom to do so. Doing custom things with ExtJS can be very painful.

