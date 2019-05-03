\score{
  \relative c' {
    \clef treble
    \time 16/4
    \override Staff.TimeSignature #'stencil = ##f
    c \glissando d'
    \tweak color #red e
    \glissando
    \tweak color #red c'
  }
  \layout{}
}
