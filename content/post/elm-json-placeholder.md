+++
title = "Fetch data with Elm from Json Placeholder"
date = 2019-11-19T23:00:53-07:00
draft = false
markup = "mmark"
tags = ["elm", "functional programming"]
+++

- **ellie-app:** https://ellie-app.com/7fxptH4mWMxa1
- **Download file:** [json-placeholder.elm](/files/json-placeholder.elm)

In this blog post I am going to walk through fetching data from a JSON API with Elm. When I started learning Elm this was a pain point for me. I have also been trying to introduce others to Elm and I haven't found enough complete examples to give to people.

This post will use the latest **Elm version 0.19.1**.

I will use the [jsonplaceholder](https://jsonplaceholder.typicode.com/) API and grab a list of posts from [/posts](https://jsonplaceholder.typicode.com/posts).

The JSON looks like this:

```json
[
    {
        "userId": 1,
        "id": 1,
        "title": "some title",
        "body": "some body text"
    },
    ...
]
```


## Records and Decoders 

Let's first deal with what our data will look like. We will need a post record.

```elm
type alias Post =
    { userId : Int
    , id : Int
    , title : String
    , body : String
    }
```

And then a list of posts.

```elm
type alias Posts =
    List Post
```

Now when we fetch this data from the API we will need to parse the JSON into something Elm will understand. We do this by decoding the JSON.

This was really strange to me coming from JavaScript land, but once you get used to decoding your JSON you begin to see its benefits. In this example we are parsing the data fields into primitive types like `Int` and `String`. In other cases you might want to constrain your data even more and parse the data into an Elm type.

For example, I could have an endpoint that turned on a light with a status field.

```json
{
    "status": "on"
}

{
    "status": "off"
}
```

The only two values state could be is `On` and `Off`. You could make a type and only accept those two values.

```elm
type Status
    = On
    | Off
```

Something like `"status": "blue"` would be invalid and you would get a nice error message and a safe way to deal with the error.

Anyway, back to our simple decoder.

We first need to install the Elm decoder package.

```bash
elm install elm/json
```

And now import the package in our Elm code so we can use it.

```elm
import Json.Decode as D exposing (Decoder, field, int, string)
```

Now we can define our decoder for the `Post` record we defined above.

```elm
postDecoder : Decoder Post
postDecoder =
    D.map4 Post
        (D.field "userId" D.int)
        (D.field "id" D.int)
        (D.field "title" D.string)
        (D.field "body" D.string)
```

Since we will be fetching a list of these posts we need another decoder to decode the list. Fortunately decoders compose really nicely.

```elm
postsDecoder : Decoder Posts
postsDecoder =
    D.list postDecoder
```

## Define our app Model

Here I am going to use the package [krisajenkins/remotedata](https://package.elm-lang.org/packages/krisajenkins/remotedata/latest/RemoteData) instead of using just the [elm/http](https://package.elm-lang.org/packages/elm/http/2.0.0/Http) package like in the [official Elm docs](https://guide.elm-lang.org/effects/json.html). The RemoteData packages provides some extra types and helpers on top of elm/http.

```bash
elm install elm/http
elm install krisajenkins/remotedata
```

And again like before, import the things.

```elm
import Http exposing (expectJson)
import RemoteData exposing (RemoteData(..), WebData)
```

And now we can define our application model.

```elm
type alias Model =
    { posts : WebData Posts }


initialModel : Model
initialModel =
    { posts = Loading }
```

Notice how our model is a `WebData Posts` instead of just `Posts`. In VueJS I would declare the data as `undefined` and then when I succeed in fetching my data set the value. I would then have to check that `posts` is not `undefined` when I attempt to use the data.

Elm deals with this uncertainty in a different way. This is one of the reasons why Elm has *no runtime errors*.

Also notice how the initial state of the model is set to `Loading`. This is a type provided by the RemoteData package. The definition looks like the following:

```elm
type RemoteData e a
    = NotAsked
    | Loading
    | Failure e
    | Success a
```

We initialize our app in the `Loading` state because we will fire off the request right when the application starts up.

When we get to the view function later on we will have to deal with each of these cases `NotAsked`, `Loading`, `Failure`, and `Success`.

## Define the update

Now we need to actually make the request. In Elm all side effects are dealt with in the update function. Read more about [The Elm Architecture](https://guide.elm-lang.org/architecture/) if you want to know more about how that works.

You cannot just fire off an AJAX call anywhere in the code like in JavaScript. This might seem like a nuisance, but as your web app grows this constraint makes it easy to find where your data is coming and going in your app.

```elm
type Msg
    = PostsResponse (WebData Posts)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        PostsResponse response ->
            ( { model | posts = response }
            , Cmd.none
            )


getPosts : Cmd Msg
getPosts =
    Http.get
        { url = "https://jsonplaceholder.typicode.com/posts"
        , expect =
            expectJson
                (RemoteData.fromResult >> PostsResponse)
                postsDecoder
        }
```

Now somewhere in the code we need to fire off this getPosts command. We will do that in the app initialization. The `init` function takes an initial model and an initial command message.

{{< highlight elm "hl_lines=4" >}}
main : Program () Model Msg
main =
    Browser.element
        { init = \_ -> ( initialModel, getPosts )
        , view = view
        , update = update
        , subscriptions = subscriptions
        }
{{</ highlight >}}


## View the posts

Lastly we need to be able to view the posts should the request succeed.

```elm
viewPost : Post -> Html msg
viewPost post =
    div
        [ class "post" ]
        [ h2 [] [ text post.title ]
        , p [] [ text post.body ]
        ]

viewPosts : List Post -> Html msg
viewPosts posts =
    div [] (List.map viewPost posts)
```

In order to display our list of posts, we need to account for all cases of the web request. These are the 4 cases of RemoteData that I mentioned above.

```elm
view : Model -> Html msg
view model =
    case model.posts of
        NotAsked ->
            div [] [ text "Initializing" ]

        Loading ->
            div [] [ text "Loading" ]

        Failure _ ->
            div [] [ text "Network Error" ]

        Success posts ->
            viewPosts posts
```

And we're done. We have fetched a list of posts.

P.S. I'm getting close to finishing my book, [Elm Calculator book](/courses). I build a calculator from scratch using Elm. I go through setting up CSS, using Elm types effectively, deployment, and testing.
