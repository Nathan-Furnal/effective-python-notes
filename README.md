# README

## Introduction

A series of notes and personal comments on the book with code examples when necessary.

## Tooling

Tools I'm using; the book doesn't take a strong stance of tooling and usually leans
on the standard library.

* IDE: [Emacs](https://www.gnu.org/software/emacs/)
* Python versioning: [uv](https://docs.astral.sh/uv/)
* Package management: [uv](https://docs.astral.sh/uv/)
* Linting: [ruff](https://docs.astral.sh/ruff/)
* Type checking: [basedpyright](https://docs.basedpyright.com/latest/)
* CI/CD: [Github Actions](https://docs.github.com/en/actions)
* Testing: [pytest](https://docs.pytest.org/en/stable/)

## Notes

See the [notes file](./NOTES.md) for comments, following the structure of the book.

## Running the tests

Since the project uses a src layout, you'll need to install the project and then
run the tests.

In the project folder,

```sh
uv pip install -e .  # Running this the first time and every time code changes
```

Then,

```sh
uv run pytest
```
