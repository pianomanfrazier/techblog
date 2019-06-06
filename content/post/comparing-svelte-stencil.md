+++
title = "Comparing Svelte and Stencil JS Frameworks"
date = 2019-06-12
draft = false
markup = "mmark"
+++

Writing a blog is a great excuse to explore some new and unfamiliar technology. In this post I will explore two new(er) JavaScript frameworks, [Stencil](https://stenciljs.com/) and [Svelte](https://svelte.dev/).

As of writing this post. Svelte is at version 3.4.4 and Stencil is at version 1.0.0. Both projects seem actively worked on based on GitHub activity.

Both frameworks are web compiler frameworks. Meaning, they take some source input and generate some minified optimized version in JavaScript, HTML, and CSS.

## Stencil

Stencil was created and is maintained by the Ionic Framework team. The focus is on using web standards, like custom web components, and not the opinions of a particular framework or build tools.

Since it generates standard web components, the components can be used in any JavaScript framework. It leverages modern browser APIs like [Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements). It supports IE11 and up.

Stencil also provides support for TypeScript and JSX. Here is an example component.

[Example component](https://stenciljs.com/docs/my-first-component). TypeScript + JSX = TSX

```tsx
import { Component, Prop } from '@stencil/core';

@Component({
  tag: 'my-first-component',
})
export class MyComponent {

  // Indicate that name should be a public property on the component
  @Prop() name: string;

  render() {
    return (
      <p>
        My name is {this.name}
      </p>
    );
  }
}
```

Usage

```html
<my-first-component name="Max"></my-first-component>
```

[Learning resources](https://stenciljs.com/resources)

## Svelte

Svelte seems like it has been around longer since it is at version 3. Some of the features of Svelte are:

- No virtual DOM
- No runtime (all work done at compile time)

`.svelte` files are very similar to Vue single file components. A `.svelte` file can have 3 sections a script tag with the business logic, a style tag with CSS, and finally markup.

The markup, or template section, differs from a Vue component because you don't need a root level element.

Here is an example component. I went through the tutorial in their documentation and combined all the parts I found useful or interesting into a compact example.

```html
<script>
  import Nested from './Nested.svelte';

  let msg = 'A string with <strong>HTML</strong>';
  let things = ['dog', 'cat', 'bear', 'frog'];

  let count = 0;
  function handleClick() {
    count += 1;
  }
  // reactive statement
  // code is run when count changes
  $: console.log(`the count is ${count}`);
</script>

<style>
  button {
    color: white;
    background-color: blue;
  }
</style>

<p>{@html msg}</p>

<button on:click={handleClick}>
	Clicked {count} {count === 1 ? 'time' : 'times'}
</button>

{#if count > 10}
  <p>count &gt; 10</p>
{:else if count > 5}
  <p>count &gt; 5</p>
{:else}
  <p>count &lt; 5</p>
{/if}

<ul>
  {#each items in item}
    <li>{item}</li>
  {/each>
</ul>

<Nested title="nested"/>
```
Nested.svelte
```html
<script>
  // export props and give it a default (optional)
  export let title = 'Title';
</script>

<p>{title}</p>
```

Svelte works with the following build tools.

- Rollup
- Webpack
- Parcel

For generating larger projects, similar to the Vue CLI, see [Sapper](https://sapper.svelte.dev/). It supports routing, server-side rendering, and code-splitting.

## Bundle Size Comparisons

I thought it would be interesting to compare the outputs of each of these frameworks with the [Real World App](https://github.com/gothinkster/realworld). I went to the demo page of each implementation and compared the network statistics in the network tab in my browser's dev tools (Firefox).

{{< figure
  src="/img/new-web-tech-2019/compare.svg"
  alt=    "Comparison Bar Chart"
  title=  "Comparison Bar Chart"
  caption="**RealWorld App**"
>}}

| Framework | Number of JS Files | JS bundle size (KB) | % |
|-----------|---:|----------:|----:|
| Svelte    | 7  | 43.54    | 4 |
| Stencil   | 10 | 120.06    | 12 |
| **Other Frameworks** |    |    |     |
| Angular   | 8  | 551.97    | 54  |
| React/Redux | 1  | 1,024.00 | 100 |
| Vue       | 6  | 218.13    | 21  |
| Elm       | 1  |  90.52    | 9  |

## Network Charts From Dev Tools

{{< figure
  src="/img/new-web-tech-2019/svelte-network-performance.png"
  alt="Svelte Asset Size"
  title="Svelte Asset Size"
  caption="Svelte Asset Size"
>}}

{{< figure
  src="/img/new-web-tech-2019/stencil-network-performance.png"
  alt="Stencil Asset Size"
  title="Stencil Asset Size"
  caption="Stencil Asset Size"
>}}

{{< figure
  src="/img/new-web-tech-2019/angular-network-performance.png"
  alt="Angular Asset Size"
  title="Angular Asset Size"
  caption="Angular Asset Size"
>}}

{{< figure
  src="/img/new-web-tech-2019/react-network-performance.png"
  alt="React Asset Size"
  title="React Asset Size"
  caption="React Asset Size"
>}}

{{< figure
  src="/img/new-web-tech-2019/vue-network-performance.png"
  alt="Vue Asset Size"
  title="Vue Asset Size"
  caption="Vue Asset Size"
>}}

{{< figure
  src="/img/new-web-tech-2019/elm-network-performance.png"
  alt="Elm Asset Size"
  title="Elm Asset Size"
  caption="Elm Asset Size"
>}}

A great future side project would be to generate these statistics for all the implementations of the RealWorld App. After scraping the project's REAMDE for the projects, you could use something like Selenium to hit each demo page and gather all the stats.

## Conclusion

The new generation of JS frameworks seem more focused on bundle size. I thought nothing would be able to beat Elm's bundle size. Svelte proved me wrong.

After a brief look at these two frameworks, I would use Svelte as a replacement for Vue. It seems to provide a similar API.

I would use Stencil if I was concerned about sharing my component with the JS community and needed it to work across any JS framework.