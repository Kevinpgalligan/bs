## Description
A CLI tool to convert numbers between bases, with as little typing as possible.

```
$ bs FFFE
[from hexadecimal]
  decimal     65534
  binary      1111111111111110
  octal       177776
$ bs -t d F
15
```

## Installation
This is a Python 3 script, installed from [PyPI](https://pypi.org/project/base-convert-cli/) using pip.

```
pip3 install base-convert-cli
```

Hasn't been tested on Windows.

## Examples
If you don't specify a base, it does all common conversions.

```
$ bs 0
[from decimal]
  binary      0
  hexadecimal 0
  octal       0

[from binary]
<clipped output here>
```

Specifying base through a flag.

```
$ bs --from hex F
[from hexadecimal]
  decimal     15
  binary      1111
  octal       17
```

From base-6.

```
$ bs --from 6 54
[from base-6]
  decimal     34
  binary      100010
  hexadecimal 22
  octal       42
```

To base-7.

```
$ bs --to 7 54
[from decimal]
  base-7 105

[from hexadecimal]
  base-7 150

[from octal]
  base-7 62
```

Specifying both input and output bases.

```
$ bs --from hex --to dec F
15
```

Shorthand for lazy people.

```
$ bs -f h -t d F
15
```

Aaaaand input through a pipe.

```
$ echo '5+10' | bc | bs -t h
[from decimal]
  hexadecimal F

[from octal]
  hexadecimal D
```

## Contributing
Feel free to submit tweaks. To run tests, install tox via `pip3 install tox` and then run the `tox` command from the base directory.
