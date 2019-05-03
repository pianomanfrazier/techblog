\score{
  \relative c' {
    \clef treble
    \time 8/4
    \override Staff.TimeSignature #'stencil = ##f
    <\tweak color #red a c e g>
    <\tweak color #red b d f a>
    <\tweak color #green c e g b>
    <d' f a \tweak color #green c>
    <e g b \tweak color #red d>
    <f a c \tweak color #red e>
  }
  \layout{}
}
