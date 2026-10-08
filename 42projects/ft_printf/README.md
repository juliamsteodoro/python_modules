*This project has been created as part of the 42 curriculum by [jumoreir].*

<h1 align="center">FT_PRINTF &nbsp;·&nbsp; by jumoreir</h1>

<p align="center">
  <img src="https://img.shields.io/badge/C-language-blue?style=flat-square&logo=c" />
  <img src="https://img.shields.io/badge/42-school-gray?style=flat-square" />
  <img src="https://img.shields.io/badge/norminette-passing-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/status-finished-brightgreen?style=flat-square" />
</p>


---

## Description

`ft_printf` is a reimplementation of the C standard library function `printf()`. The goal is to reproduce its core behaviour without replicating its internal buffer management. The function accepts a format string and a variable number of arguments, processes each conversion specifier, and writes the result to standard output.

The following conversion specifiers are supported:

| Specifier | Output |
|-----------|--------|
| `%c` | Single character |
| `%s` | String — prints `(null)` if the pointer is NULL |
| `%p` | Pointer address — `0x` prefix with lowercase hex, or `(nil)` if NULL |
| `%d` | Signed decimal integer |
| `%i` | Signed integer (base 10) |
| `%u` | Unsigned decimal integer |
| `%x` | Unsigned hexadecimal, lowercase |
| `%X` | Unsigned hexadecimal, uppercase |
| `%%` | Literal percent sign |

`ft_printf` returns the total number of characters written to stdout, matching the behaviour of the original `printf()`.

---

## Instructions

### Compilation

Clone the repository and compile using the provided Makefile:

```bash
git clone <repository-url>
cd ft_printf
make
```

This produces `libftprintf.a`, a static library you can link against your own projects.

### Usage

Include the header and link the library at compile time:

```c
#include "ft_printf.h"
```

```bash
gcc main.c -L. -lftprintf -o program
```

### Cleanup

```bash
make clean    # removes object files
make fclean   # removes object files and the library
make re       # full rebuild
```

---

## Algorithm and Data Structure

### Parsing strategy

The format string is traversed character by character inside `ft_printf`. When the loop encounters a regular character, it writes it directly to stdout via `write()` and accumulates the byte count into `count`. When it encounters a `%`, it advances one extra position and passes the following character to `parser()`.

```
ft_printf(fmt, ...)
│
├── va_start(list, fmt)
├── i = 0; count = 0
│
├── while fmt[i] != '\0'
│   ├── fmt[i] != '%' → write(1, &fmt[i], 1) → count++ → i++
│   └── fmt[i] == '%' → parser(fmt[i+1], list, &count) → i += 2
│
├── va_end(list)
└── return count

parser(c, list, count)
├── 'c'     → ft_putchar(va_arg(list, int), count)
├── 's'     → ft_putstr(va_arg(list, char *), count)
├── 'd'/'i' → ft_putnbr(va_arg(list, int), count)
├── 'u'     → ft_putnbr_unsigned(va_arg(list, unsigned int), count)
├── 'x'/'X' → ft_putnbr_hexa(va_arg(list, unsigned int), c, count)
├── 'p'     → ft_putnbr_pointer(va_arg(list, void *), count)
└── '%'     → ft_putchar('%', count)
```

No intermediate buffer or dynamic structure is used for parsing — the format string itself acts as the only state, traversed with a single index.

### Output helpers

Each conversion specifier is handled by a dedicated function:

- `ft_putchar()` prints a single `char`. It is the only place where a byte is actually written and where `count` is incremented. All other helpers eventually route through it or call `write` and update `count` directly.
- `ft_putstr()` iterates over a `char *` with a `while` loop, calling `ft_putchar()` for each character. If the pointer is `NULL`, it writes the literal string `(null)` instead.
- `ft_putnbr()` prints a signed integer recursively, handling the edge case of `INT_MIN` explicitly before casting digits to characters.
- `ft_putnbr_unsigned()` prints an `unsigned int`, converting the value to a string before writing.
- `ft_putnbr_hexa()` prints an unsigned integer in hexadecimal. It uses a character lookup string defined in the header — one for lowercase digits and one for uppercase — selected based on the specifier passed in.
- `ft_putnbr_pointer()` prints a memory address. A `NULL` pointer prints `(nil)` via a direct `write` call. A non-null pointer prints the `0x` prefix followed by the address converted to lowercase hex using `ft_itoa_hexa`, with the value cast to `unsigned long` to ensure correctness on both 32-bit and 64-bit platforms.

### Count propagation via pointer

Rather than returning a character count from each helper and summing it at the call site, all output functions receive an `int *count` parameter and increment it directly. This keeps a single accumulator shared across the entire call chain, avoids adding a return value to every helper, and makes the main loop in `ft_printf` straightforward to read.

### Memory management

Dynamic allocation is limited to four functions — `ft_putnbr`, `ft_putnbr_unsigned`, `ft_putnbr_hexa`, and `ft_putnbr_pointer` — where a numeric value must be converted to a string representation before it can be written. In each case the allocation is immediately followed by the write and then `free`, keeping the allocation lifetime minimal and fully contained within the handler. The main parsing loop and all character/string helpers perform no allocation.

### Variadic argument handling

Arguments are consumed in order through `va_list`:

```c
va_start(list, fmt);       // initialise after the last named parameter
va_arg(list, type);        // retrieve the next argument and advance
va_end(list);              // mandatory cleanup
```

`va_copy` is not used — the argument list is consumed strictly linearly, one `va_arg` call per specifier, so there is never a need to save or rewind the position in the list.

---

## Resources

### References

| Resource | Used for |
|----------|----------|
| [`man 3 printf`](https://man7.org/linux/man-pages/man3/printf.3.html) | Reference for specifier behaviour and expected return value |
| [`man 3 stdarg`](https://man7.org/linux/man-pages/man3/stdarg.3.html) | Understanding `va_list`, `va_start`, `va_arg`, and `va_end` macros |

### AI Usage

Claude (claude.ai) was used throughout the project strictly as a learning and clarification tool — no code was generated by AI.

Specifically, it was used to:

- **Understand variadic functions** — clarifying how `va_list`, `va_start`, `va_arg`, and `va_end` work together, and why arguments like `char` are promoted to `int` when passed through `...`.
- **Explain design decisions** — understanding why `count` is passed as `int *` to helper functions instead of using return values, and why the `parser` receives both `va_list` and `int *count`.
- **Clarify C behaviour** — understanding type promotion rules in variadic functions and why `va_arg(list, char)` would be undefined behaviour.
