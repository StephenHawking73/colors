# colors.py
# Modul für farbige und formatierte Terminal-Ausgaben mit ANSI-Escape-Sequenzen

# ---------- Grundfarben ----------
# Vordergrund (Textfarben)
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Hintergrundfarben
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# ---------- Textattribute ----------
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"

# ---------- Hilfsfunktionen (Vordergrundfarben) ----------
def red(text: str) -> str:
    return f"{RED}{text}{RESET}"

def green(text: str) -> str:
    return f"{GREEN}{text}{RESET}"

def yellow(text: str) -> str:
    return f"{YELLOW}{text}{RESET}"

def blue(text: str) -> str:
    return f"{BLUE}{text}{RESET}"

def magenta(text: str) -> str:
    return f"{MAGENTA}{text}{RESET}"

def cyan(text: str) -> str:
    return f"{CYAN}{text}{RESET}"

def white(text: str) -> str:
    return f"{WHITE}{text}{RESET}"

# ---------- Hilfsfunktionen (Hintergrundfarben) ----------
def bg_red(text: str) -> str:
    return f"{BG_RED}{text}{RESET}"

def bg_green(text: str) -> str:
    return f"{BG_GREEN}{text}{RESET}"

def bg_yellow(text: str) -> str:
    return f"{BG_YELLOW}{text}{RESET}"

def bg_blue(text: str) -> str:
    return f"{BG_BLUE}{text}{RESET}"

def bg_magenta(text: str) -> str:
    return f"{BG_MAGENTA}{text}{RESET}"

def bg_cyan(text: str) -> str:
    return f"{BG_CYAN}{text}{RESET}"

def bg_white(text: str) -> str:
    return f"{BG_WHITE}{text}{RESET}"

# ---------- Textattribute ----------
def bold(text: str) -> str:
    return f"{BOLD}{text}{RESET}"

def underline(text: str) -> str:
    return f"{UNDERLINE}{text}{RESET}"

def italic(text: str) -> str:
    return f"{ITALIC}{text}{RESET}"