This project uses [Black] to format code. To avoid manually running `black .`,
you can install a Git hook or a format-on-save plugin for your editor.

[Black]: https://github.com/psf/black

## Documenting Django version quirks

For code that can be deleted as the minimum supported version of Django is
raised, add a comment like `DJANGO<version>`.
