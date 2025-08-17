# colors.py
# Modul für farbige und formatierte Terminal-Ausgaben mit ANSI-Escape-Sequenzen

# ---------- ANSI Escape Codes ----------
RESET = "\033[0m"

# Vordergrundfarben (Standard)
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Vordergrundfarben (hell)
BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

# Hintergrundfarben (Standard)
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

# Hintergrundfarben (hell)
BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"

# Textattribute
BOLD      = "\033[1m"
ITALIC    = "\033[3m"
UNDERLINE = "\033[4m"

# ---------- Hilfsfunktion ----------
def _fmt(code: str, *args) -> str:
    """Hilfsfunktion: wendet ANSI-Code auf beliebige Argumente an."""
    return f"{code}{' '.join(map(str, args))}{RESET}"

# ---------- Vordergrundfarben ----------
def black(*args):   return _fmt(BLACK, *args)
def red(*args):     return _fmt(RED, *args)
def green(*args):   return _fmt(GREEN, *args)
def yellow(*args):  return _fmt(YELLOW, *args)
def blue(*args):    return _fmt(BLUE, *args)
def magenta(*args): return _fmt(MAGENTA, *args)
def cyan(*args):    return _fmt(CYAN, *args)
def white(*args):   return _fmt(WHITE, *args)

# Helle Vordergrundfarben
def bright_black(*args):   return _fmt(BRIGHT_BLACK, *args)
def bright_red(*args):     return _fmt(BRIGHT_RED, *args)
def bright_green(*args):   return _fmt(BRIGHT_GREEN, *args)
def bright_yellow(*args):  return _fmt(BRIGHT_YELLOW, *args)
def bright_blue(*args):    return _fmt(BRIGHT_BLUE, *args)
def bright_magenta(*args): return _fmt(BRIGHT_MAGENTA, *args)
def bright_cyan(*args):    return _fmt(BRIGHT_CYAN, *args)
def bright_white(*args):   return _fmt(BRIGHT_WHITE, *args)

# ---------- Hintergrundfarben ----------
def bg_black(*args):   return _fmt(BG_BLACK, *args)
def bg_red(*args):     return _fmt(BG_RED, *args)
def bg_green(*args):   return _fmt(BG_GREEN, *args)
def bg_yellow(*args):  return _fmt(BG_YELLOW, *args)
def bg_blue(*args):    return _fmt(BG_BLUE, *args)
def bg_magenta(*args): return _fmt(BG_MAGENTA, *args)
def bg_cyan(*args):    return _fmt(BG_CYAN, *args)
def bg_white(*args):   return _fmt(BG_WHITE, *args)

# Helle Hintergrundfarben
def bg_bright_black(*args):   return _fmt(BG_BRIGHT_BLACK, *args)
def bg_bright_red(*args):     return _fmt(BG_BRIGHT_RED, *args)
def bg_bright_green(*args):   return _fmt(BG_BRIGHT_GREEN, *args)
def bg_bright_yellow(*args):  return _fmt(BG_BRIGHT_YELLOW, *args)
def bg_bright_blue(*args):    return _fmt(BG_BRIGHT_BLUE, *args)
def bg_bright_magenta(*args): return _fmt(BG_BRIGHT_MAGENTA, *args)
def bg_bright_cyan(*args):    return _fmt(BG_BRIGHT_CYAN, *args)
def bg_bright_white(*args):   return _fmt(BG_BRIGHT_WHITE, *args)

# ---------- Textattribute ----------
def bold(*args):      return _fmt(BOLD, *args)
def italic(*args):    return _fmt(ITALIC, *args)
def underline(*args): return _fmt(UNDERLINE, *args)

# ---------- RGB Farben ----------
def rgb(r: int, g: int, b: int, *args):
    return f"\033[38;2;{r};{g};{b}m{' '.join(map(str, args))}{RESET}"

def bg_rgb(r: int, g: int, b: int, *args):
    return f"\033[48;2;{r};{g};{b}m{' '.join(map(str, args))}{RESET}"