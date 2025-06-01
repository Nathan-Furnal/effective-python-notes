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

## Chapter 3. Loops and Iterators

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
