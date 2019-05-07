+++
title = "Button State With Elm"
date = 2019-04-26T14:38:50-06:00
draft = true
markup = "mmark"
+++

Define a type to specify each state
Pattern match on the type to represent each state
Consistent button states across all exercises

Define different states for your button using types.

```elm
type BtnState
  = Check
  | Next
  | Reset

btn : BtnState -> List (Attribute msg) -> Html msg
bnt state attributes =
  case state of
    Check ->
      btn attributes [ text "Check" ]
    Next ->
      btn attributes [ text "Next" ]
    Reset ->
      btn attributes [ text "Reset" ]
```

This gives me a buttons that I can use throughout my application and represent the state of my exercise.

In the view I resolve the state of the exercise and render my button.

```elm
view : Model -> Html Msg
view model =
  ...
  , if done then
      UI.btn
        UI.Reset
        [ onClick ResetProblem ]
    else if showAnswer then
      UI.btn
        UI.Next
        [ onClick NextProblem ]
    else
      UI.btn
        UI.Check
        [ disabled (not model.valid)
        , onClick CheckAnswer
        ]
```


