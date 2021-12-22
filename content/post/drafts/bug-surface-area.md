+++
title = "Bug Surface Area"
date = 2021-05-18T10:37:39-06:00
draft = true
markup = "mmark"
+++

```js
const days = [
    { day: 'Monday', val: false },
    { day: 'Tuesday', val: false },
    { day: 'Wednesday', val: false },
    { day: 'Thursday', val: false },
    { day: 'Friday', val: false },
    { day: 'Saturday', val: false }
]
```

```js
let result = '';
for (day of days) {
    if (day.val) {
        result += ' ' + day.day
    }
}
return result;
```

```js
days
    .filter(x => x.val) // get all the true days
    .map(x => x.day) // get list of the day names
    .join(', ') // combine them all into one string
```

