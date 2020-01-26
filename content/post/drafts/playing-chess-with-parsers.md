+++
title = "Playing Chess With Parsers"
date = 2020-01-25T22:47:50-07:00
draft = true
markup = "mmark"
+++


### Some references

- [Chess Notation](https://en.wikipedia.org/wiki/Chess_notation)
- [Algebraic Chess Notation](https://en.wikipedia.org/wiki/Algebraic_chess_notation)
- [Portable Game Notation](https://en.wikipedia.org/wiki/Portable_Game_Notation)

Import and export formats.

## Create Domain Specific Languages

These are referred to DSLs. Sometimes you want to craft a minimal language to let your users describe something they want.

[Robert Fowler on DSLs](https://www.martinfowler.com/bliki/DomainSpecificLanguage.html)

Graphical DSLs. Like Scratch or Code.org

## Robot Language

```robo
up 
down
left
right
pickup
putdown
speak "I am a robot"
```

```robo
u 
d
l
r
pu
pd
s "I am a robot"
```

Move a robot on a 2D grid. Pick up items and put them down.

## Chess notation

```pgn
[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6
23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5
hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5
35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6
Nf2 42. g4 Bd3 43. Re6 1/2-1/2
```
Source https://en.wikipedia.org/wiki/Portable_Game_Notation#Example

## Figured Bass Notation

{{< figure
	src="/img/chess-parsers/figured_bass_example_BWV_443.png"
	alt="Figured Bass Example from BWV 443"
	title="Figured Bass Example from BWV 443"
	caption="Figured Bass Example from BWV 443. The implied pitches are the small notes."
>}}

I made a prototype of doing harmonic analysis and needed a language to describe what the figured bass should be. I wanted something that was like using pencil and paper. It needed to be open ended and allow users to input some kind of valid figured bass notation.

[Demo](https://pianomanfrazier.com/post/theory-app-prototypes/#harmonic-analysis)

Here is the language.

### Figured Bass

- 6/4
- 6#/b3

### Chord

Valid inputs are in the form of `<Roman Numeral><+|aug|hd|dim>(<fig bass>)`. The first roman numeral part is required. The last two parts are optional.

Roman numerals for music theory are the numbers I through VII. Upper case numerals indicate major or and lower case indicate either minor.

- I
- I(6/4)
- viihd
- viihd(4/2)
- ii(6/b5)
- iii(6/#5)
