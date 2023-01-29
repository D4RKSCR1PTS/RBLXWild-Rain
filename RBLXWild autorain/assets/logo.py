import random

from .colors import BLINK, FG, RESET_ALL, REVERSE

colors_list = [
    FG.orange,
    FG.blue,
    FG.purple,
    FG.cyan,
    FG.yellow,
    FG.pink,
    FG.lightblue,
    FG.lightcyan,
]
colors = random.choice(colors_list)
replace = REVERSE + colors
banner = (
    BLINK
    + f"""{colors}
██████╗░██████╗░██╗░░░░░██╗░░██╗██████╗░░█████╗░██╗███╗░░██╗
██╔══██╗██╔══██╗██║░░░░░╚██╗██╔╝██╔══██╗██╔══██╗██║████╗░██║
██████╔╝██████╦╝██║░░░░░░╚███╔╝░██████╔╝███████║██║██╔██╗██║
██╔══██╗██╔══██╗██║░░░░░░██╔██╗░██╔══██╗██╔══██║██║██║╚████║
██║░░██║██████╦╝███████╗██╔╝╚██╗██║░░██║██║░░██║██║██║░╚███║
╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝
{RESET_ALL}"""
)
