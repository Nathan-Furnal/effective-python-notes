# Notes

Various comments and personal notes on usage, with additional code if needed.
Python emoji 🐍 if there's nothing specific to add.

## Chapter 1. Pythonic Thinking

### Item 1: Know Which Version of Python You’re Using

Many OSes ship with a global Python install. By default I never use it and never
`pip install` anything through it. Because Python is a dependency for many other
tools, bringing anything into your global environment through the global Python
is usually a bad idea as it can break tools because of mismatched versions or
conflicting dependencies. I use a Python version manager like `uv` but there are
plenty more.

Basically, isolate your Python installations. Failing that, it's usually safer
to run any `pip` command with `pip --user --require-virtualenv`.

### Item 2: Follow the PEP 8 Style Guide

Just use a formatter that takes care of styling for you. Consistent style is
important for sharing code and setting expectations in a codebase but not worth
fretting over.

### Item 3: Never Expect Python to Detect Errors at Compile Time

🐍

### Item 4: Write Helper Functions Instead of Complex Expressions

About the DRY principle, I mostly agree but just like any principle, it can be
taken to meaningless extremes. I like ["Repeat Yourself, A
Bit"](https://web.archive.org/web/20250529212037/https://blog.startifact.com/posts/repeat-yourself-a-bit/)
by Martijn Faassen for a more nuanced take on the topic.

### Item 5: Prefer Multiple-Assignment Unpacking over Indexing

A staple of Pythonic code, cannot agree more.

### Always Surround Single-Element Tuples with Parentheses

True but comes up quite rarely in code in general. Since tuples are immutable,
it's rare to have a one element tuple. Instead of destructuring with only one
element, you'd prefer using `[0]`. If you add linters, I don't think I've ever
had issues with this.

### Item 7: Consider Conditional Expressions for Simple Inline Logic

🐍

### Item 8: Prevent Repetition with Assignment Expressions

Definitely an underused feature, especially for simple conditions check. Any time
you're fetching data from somewhere and the possible value is `T | None` or a
possible empty sequence,

Just having,

``` python
if (item := get_one_or_none()):
    do_something(item)

# Or something like

if (items := get_many()):  # where result is list[T], possibly []
    preprocess(items)
```

is useful and more compact than the equivalent code without the walrus operator.

Being able to emulate the `switch/case` and `do/while` constructs does not come
up as often but assignment expressions are the right tool for the job.

### Item 9: Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient

I love [`match`
statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements),
they're very powerful but sometimes confusing; the `enum` example shown in the
book is pretty typical.

There's good talk from Raymond Hettinger about structural pattern matching,

- [slides of the
  talk](https://www.dropbox.com/scl/fi/ggzp2c7l7pbxyf384vtu6/PyITPatternMatchingTalk.pdf?rlkey=qbabyqlixlt99tkcxvohsgj5u&e=1&dl=0)
- [video of the talk](https://www.youtube.com/watch?v=ZTvwxXL37XI)

Just like pointed out in the book, once there's a small space of somewhat
structured data, you can use `match` to handle the cases you want.

For example, if we're parsing moving instructions.

```python
from dataclasses import dataclass
import re
from typing import Literal

@dataclass
class Move:
    direction: Literal["up", "down", "left", "right"]
    steps: int


def extract_move_from_directions(directions: str) -> Move:
    pat = re.compile(r'(down|up|left|right) by (\d+)')
    match (res := pat.findall(directions)):
        case [(direction, steps)]:
            return Move(direction, int(steps))
        case _:
            msg = f"Incorrect match: {res}"
            raise ValueError(msg)

```

Then, we can easily obtain something like this,

```sh
>>> extract_move_from_directions("go down by 12 steps")
Move(direction='down', steps=12)
```

and raise a value error anytime we don't find this pattern exactly once.

It's also possible to extend the matching in case we have multiple moves in the
same sentence.

```python
def extract_move_from_directions(directions: str) -> Move | list[Move]:
    pat = re.compile(r'(down|up|left|right) by (\d+)')
    match (res := pat.findall(directions)):
        case [(direction, steps)]:
            return Move(direction, int(steps))
        case [*matches] if len(matches) > 1:
        return [Move(direction, int(steps)) for direction, steps in matches]
        case _:
            msg = f"Incorrect match: {res}"
            raise ValueError(msg)
```

```sh
>>> extract_move_from_directions("go down by 12 steps, then go left by 11 steps")
[Move(direction='down', steps=12), Move(direction='left', steps=11)]
```

It's important to add a guard `if len(matches) > ...` because `[*matches]` will
include the empty list result and we still want to raise when there's no
matching at all for the regex.

## Chapter 2. Strings and Slicing

### Item 10: Know the Differences Between bytes and str

All things considered, it's relatively rare to have meaningful operations between strings and bytes. So I was not
incredibly convinced it deserved an item. That being said, there are clearly some areas where it comes up a lot.

In most cryptography related libs, you'll work with bytes exclusively, while most of your inputs are strings.
Hashing, (as)symmetric keys encryption, etc. Will often return bytes, since it is the base type for most of those operations.

See the [documentation on hashing](https://docs.python.org/3/library/hashlib.html)
or the [documentation on cryptography](https://cryptography.io/en/latest/).

Another fun exercise that touches on the difference between memory and representation
for strings is [Advent of Code, year 2015, day 8](https://adventofcode.com/2015/day/8).

### Item 11: Prefer Interpolated F-Strings over C-Style Format Strings and str.format

Now there's even a [PEP for template strings](https://peps.python.org/pep-0750/) which will
land in Python 3.14!

100% agree, there's very little reason to use anything other than `f-string`s nowadays.

Something I haven't seen mentioned though, is that you can bind "later" when using `str.format`.
For example,

```python
s = "Hey there {0}"
print(s.format("Jack"))  # Hey there Jack
```

While `f-string`s are eager and you need to bind a name before using it.

```python
i: int
print(f"{i}")  # NameError
i = 0
```

The "fix" of course is to pass the data around until the last moment, when you need to actually produce the string.

### Item 12: Understand the Difference Between repr and str when Printing Objects

Cool distinction of what is sometimes unclear:

- `__repr__` :: Serializable (somewhat) representation. Can be called up in `f-string`s with `f{obj!r}`.
- `__str__` :: Human readable representation.

`dataclasses` will take care of most representation for you but if you can't or won't use them, here's a trick for the lazy.

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}({", ".join(f"{k}={v}" for k,v in self.__dict__.items())})'

class ColoredPoint(Point):
        def __init__(self, x: int, y: int, color: str) -> None:
            super().__init__(x, y)
            self.color = color
```

Then,

```python
p = Point(1, 2)                  # shows: Point(x=1, y=2)
c = ColoredPoint(3, 4, "green")  # shows: ColoredPoint(x=3, y=4, color=green)
```

### Item 13: Prefer Explicit String Concatenation over Implicit, Especially in Lists

🐍

### Item 14: Know How to Slice Sequences

Nothing special here, just a good reminder that slicing creates copies. Which might
be a suprise if you're used to other languages or libraries like [numpy](https://numpy.org/).

```python
l = [1, 2, 3, 4]
ll = l[:2]
ll[0] = 11

# `l` is still [1, 2, 3, 4]
# `ll` is [11, 2]
```

But,

```python
import numpy as np
l = np.array([1, 2, 3, 4])
ll = l[:2]
ll[0] = 11

# `l` is array([11,  2,  3,  4])
# `ll` is array([11,  2])
```

### Item 15: Avoid Striding and Slicing in a Single Expression

🐍 (`itertools` mentioned!)

### Item 16: Prefer Catch-All Unpacking over Slicing

Fully agreed and as shown, useful when you want to get only parts of a sequence,
I often use something like:

```python
first, *rest = seq
```

You can do this as many times as needed,

```python
l = [1, 2, 3, 4, 5, 6]

first, second, *_, second_last, last = l  # 1, 2, <skip>, 5, 6
```

The star notation collects items in a new list, so just make sure you're not using
this pattern in compute intensive loops, because it will be costly.

## Chapter 3. Loops and Iterators

### Item 17: Prefer enumerate over range

🐍

### Item 18: Use zip to Process Iterators in Parallel

### Item 19: Avoid else Blocks After for and while Loops

### Item 20: Never Use for Loop Variables After the Loop Ends

## Chapter 4. Dictionaries

## Chapter 5. Functions

## Chapter 6. Comprehensions and Generators

## Chapter 7. Classes and Interfaces

## Chapter 8. Metaclasses and Attributes

## Chapter 9. Concurrency and Parallelism

## Chapter 10. Robustness

## Chapter 11. Performance

## Chapter 12. Data Structures and Algorithms

## Chapter 13. Testing and Debugging

> [!WARNING]
> I'm going to use `pytest` and not `unittest`.

## Chapter 14. Collaboration
