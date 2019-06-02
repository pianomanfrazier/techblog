+++
title = "New Web Tech 2019"
date = 2019-05-30T21:57:18-06:00
draft = true
markup = "mmark"
+++

Writing a blog is a great excuse to explore some new and unfamiliar technology. In this post I will explore two new JavaScript frameworks, [Stencil](https://stenciljs.com/) and [Svelte](https://svelte.dev/).

## Stencil

A web component compiler. The framework generates standard Web Components.

- TypeScript
- JSX
- virtual DOM

Created by the Ionic Framework team. Compiler tool instead of a runtime tool. Focus on web standards instead of the opinions of a particular framework or build tools. Leverage modern browser APIs like [Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements). Supports IE11 and up.

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

- No virtual DOM
- No runtime (all work done at compile time)

Example component. Very similar to Vue single file components. A `.svelte` file can have 3 sections a script tag with the business logic, a style tag with CSS, and finally markup.

The markup differs from a Vue component because you don't need a root level element.

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

Works with

- Rollup
- Webpack
- Parcel

See also [Sapper](https://sapper.svelte.dev/). Similar to the Vue CLI to generate larger Single Page Applications with routing, server-side rendering, and code splitting.

## Compare With [Real World App](https://github.com/gothinkster/realworld)

{{< figure
  src="/img/new-web-tech-2019/compare.svg"
  alt=    "Comparison Bar Chart"
  title=  "Comparison Bar Chart"
  caption="RealWorld App JS Asset Size"
>}}

| Framework | Number of JS Files | JS size (KB) | % |
|-----------|---:|----------:|----:|
| Svelte    | 7  | 43.54    | 4 |
| Stencil   | 10 | 120.06    | 12 |
| **Other Frameworks** |    |    |     |
| Angular   | 8  | 551.97    | 54  |
| React/Redux | 1  | 1,024.00 | 100 |
| Vue       | 6  | 218.13    | 21  |
| Elm       | 1  |  90.52    | 9  |


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

## Compare With Angular, React, and Elm

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

