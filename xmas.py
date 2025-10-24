import time
import sys
import random
import threading

lyrics = [
    "My God, I thought you were someone to rely on...",
    "Me....?  I guess I was a shoulder to cry on...",
    "A face-on lover.....",
    "with a fire in his heart...",
    "A man undercover....",
    "butttt youuuu toreeee me a.......parttttt...",
    "Ooh...ooh.....",
    "Now I've found a real love,you'll never fool me again....."
]
delays = [0.8,1,0.6,1.4,0.4,1.8,0.7,0]

colors = ['\033[31m', '\033[32m', '\033[33m','\033[39m']
RESET = '\033[0m'

tree = [
    "        .       ",
    "       .*.      ",
    "      .*.*.     ",
    "     .*.*.*.    ",
    "    .*.*.*.*.   ",
    "   .*.*.*.*.*.  ",
    "  .*.*.*.*.*.*. ",
    " .*.*.*.*.*.*.*.",
    "       |||      ",
]

lock = threading.Lock()

def animate_lyrics(text):
    current_row = 1
    for i, line in enumerate(text):
        with lock:
            sys.stdout.write(f"\033[{current_row};25H")
            for j, ch in enumerate(line):
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.05)
        current_row += 1
        time.sleep(delays[i])

def xmas_tree():
    while True:
        with lock:
            sys.stdout.write("\033[1;1H")
            for i, row in enumerate(tree):
                line = ""
                for ch in row:
                    if ch == '*':
                        if (i + len(row)) % 2 == 0:
                            color = random.choice(colors)
                            line += color + '.' + RESET
                        else:
                            color = random.choice(colors)
                            line += color + '*' + RESET
                    else:
                        line += ch
                print(line)
            sys.stdout.flush()
        time.sleep(0.5)
        with lock:
            sys.stdout.write("\033[1;1H")
            for i, row in enumerate(tree):
                line = ""
                for ch in row:
                    if ch == '*':
                        if (i + len(row)) % 2 == 0:
                            color = random.choice(colors)
                            line += color + '*' + RESET
                        else:
                            color = random.choice(colors)
                            line += color + '.' + RESET
                    else:
                        line += ch
                print(line)
            sys.stdout.flush()
        time.sleep(0.5)

sys.stdout.write("\033[2J")
sys.stdout.flush()

thread1 = threading.Thread(target=animate_lyrics, args=(lyrics,))
thread2 = threading.Thread(target=xmas_tree)

thread1.start()
thread2.start()

thread1.join()
