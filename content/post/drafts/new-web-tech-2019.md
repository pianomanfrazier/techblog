+++
title = "New Web Tech 2019"
date = 2019-05-30T21:57:18-06:00
draft = true
markup = "mmark"
+++

Writing a blog is a great excuse to explore some new and unfamiliar technology. This is a todo list to myself of libraries and things I would like to explore.

- [Stencil](https://stenciljs.com/)
- [Svelte](https://svelte.dev/)
- [Pollen](https://docs.racket-lang.org/pollen/)
- [Sergey](https://sergey.cool/)

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

## Pollen

## Sergey

