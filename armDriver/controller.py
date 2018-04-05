import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

n = 0

motors = ["Base", "Elbow", "Wrist", "Claw"]

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            # screen.addstr(0, 0, 'right')
            screen.addstr(0, 0, '')
            print("moving motor " + motors[n] + "right")
        elif char == curses.KEY_LEFT:
            # screen.addstr(0, 0, 'left ')
            screen.addstr(0, 0, '')
            print("moving motor " + motors[n] + "left")
        elif char == curses.KEY_UP:
            # screen.addstr(0, 0, 'up   ')
            screen.addstr(0, 0, '')
            n += 1
            print("switching to previous motor " + motors[n])
        elif char == curses.KEY_DOWN:
            # screen.addstr(0, 0, 'down ')
            screen.addstr(0, 0, '')
            n -= 1
            print("switching to next motor " + motors[n])
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
