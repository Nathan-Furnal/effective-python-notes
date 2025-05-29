# Notes

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

That's Python for ya!

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

Sure.

### Item 8: Prevent Repetition with Assignment Expressions

### Item 9: Consider match for Destructuring in Flow Control; Avoid When if Statements Are Sufficient

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

> [!WARNING] I'm going to use `pytest` and not `unittest`.

## Chapter 14. Collaboration
