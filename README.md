## Description
A CLI tool to convert numbers between bases, with as little typing as possible.

```
$ bs --to decimal 0xFFFE
65534
$ bs FFFE
[hexadecimal]
  decimal     65534
  binary      1111111111111110
  octal       177776
```

## Setup
**Requires Python 3**.

* Clone this repo.
* Create a hard link for the command in your `/usr/bin/` directory. It should point to the stand-alone script, `src/bs/__init__.py`. Using a hard link means that the link won't stick around if you ever remove the repo.
* That's it!

```
$ pwd
/home/kg
$ git clone https://github.com/Kevinpgalligan/bs
...
$ ln /home/kg/bs/src/bs/__init__.py /usr/bin/bs
...
```

## Examples
If you don't specify a base, it does all common conversions.

```
$ bs 0
[decimal]
  binary      0
  hexadecimal 0
  octal       0

[binary]
<clipped output here>
```

Specifying base through prefix.

```
$ bs 0xF
[hexadecimal]
  decimal 15
  binary  1111
  octal   17
```

Specifying base through a flag.

```
$ bs --from hex F
<same output>
```

From base-6.

```
$ bs --from 6 54
[base-6]
  decimal     34
  binary      100010
  hexadecimal 22
  octal       42
```

To base-7.

```
$ bs --to 7 54
[decimal]
  base-7 105

[hexadecimal]
  base-7 150

[octal]
  base-7 62
```

Specifying both input and output bases.

```
$ bs --from hex --to dec F
15
```

Shorthand for lazy people.

```
$ bs --to decimal 0xF
15
$ bs -t d 0xF
15
```

Aaaaand input through a pipe.

```
$ echo '5+10' | bc | bs -t h
[decimal]
  hexadecimal F

[octal]
  hexadecimal D
```
