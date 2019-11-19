+++
title = "Fetch data with Elm from Json Placeholder"
date = 2019-11-18T23:00:53-07:00
draft = true
markup = "mmark"
+++

- **ellie-app:** https://ellie-app.com/7fxptH4mWMxa1
- **Download file:** [json-placeholder.elm](/files/json-placeholder.elm)

In this blog post I am going to walk through fetching data from a JSON api. I will use https://jsonplaceholder.typicode.com/ grab a list of posts.

This blog post is intended for Elm beginners. When I started using Elm I got confused about commands and messages.

I'm taking a break from writing my Elm book to write this quick blog post on fetching remote data. I got a question recently about how to fetch data from an API and I thought it would be easiest to explain in a blog post.

## Define the Post record and decoders

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

Now when we fetch this data from the API we will need to parse the JSON object into something Elm will understand. We do this by decoding the JSON.

We first need to install the Elm decoder package.

```bash
elm install elm/json
```

And now import the package in our Elm code so we can use it.

```elm
import Json.Decode as D exposing (Decoder, field, int, string)
```

Now we can define our decoder for the post record we defined above.

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

RemoteData provides the following type for the state of a remote data request.

```elm
type RemoteData e a
    = NotAsked
    | Loading
    | Failure e
    | Success a
```

So we initialize our app in the `Loading` state because we will fire off the request right when the application starts up.

## Define the update

Now we need to actually make the request. In Elm all side effects are stated in the update function. Look up more about The Elm Architecture if you want to know more about this.

You cannot just fire off an ajax call anywhere in the code like in JavaScript. This might seem like a nuissance, but as your web app grows it makes it easy to find where your data is coming and going in your app.

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
```

```elm
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

Now somewhere in the code Elm needs to fire off this getPosts command. We will do that in the app initialization.

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

And finally we need to account for all cases of the web request. These are the 4 cases of RemoteData mentioned above.

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

<iframe src="https://ellie-app.com/embed/7fxptH4mWMxa1" style="width:100%; height:400px; border:0; overflow:hidden;" sandbox="allow-modals allow-forms allow-popups allow-scripts allow-same-origin"></iframe>

P.S. I'm done with my first draft of my [Elm Calculator book](/courses). I build a calculator from scratch using Elm. I go through setting up CSS, using Elm types effectively, deployment, and testing.
