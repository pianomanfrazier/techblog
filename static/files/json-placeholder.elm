module Main exposing (main)

import Browser
import Html exposing (Html, div, h2, p, text)
import Html.Attributes exposing (class)
import Html.Events exposing (onClick)
import Http exposing (expectJson)
import Json.Decode as D exposing (Decoder, field, int, string)
import RemoteData exposing (RemoteData(..), WebData)



-- POSTS records and decoders


type alias Post =
    { userId : Int
    , id : Int
    , title : String
    , body : String
    }


type alias Posts =
    List Post


postDecoder : Decoder Post
postDecoder =
    D.map4 Post
        (D.field "userId" D.int)
        (D.field "id" D.int)
        (D.field "title" D.string)
        (D.field "body" D.string)


postsDecoder : Decoder Posts
postsDecoder =
    D.list postDecoder



-- MODEL


type alias Model =
    { posts : WebData Posts }


initialModel : Model
initialModel =
    { posts = Loading }



-- UPDATE


type Msg
    = PostsResponse (WebData Posts)


getPosts : Cmd Msg
getPosts =
    Http.get
        { url = "https://jsonplaceholder.typicode.com/posts"
        , expect =
            expectJson
                (RemoteData.fromResult >> PostsResponse)
                postsDecoder
        }


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        PostsResponse response ->
            ( { model | posts = response }
            , Cmd.none
            )



-- VIEW


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



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none



-- MAIN


main : Program () Model Msg
main =
    Browser.element
        { init = \_ -> ( initialModel, getPosts )
        , view = view
        , update = update
        , subscriptions = subscriptions
        }

