# Networking
Materials from my networking class at Pace University with Professor Ganis; raspberry pis used

How it Works

Each character in the string morsecode = ".--. .- -.-. ." represents the Morse code for P A C E:

P = .--.

A = .-

C = -.-.

E = .

The script loops through each symbol (. for dot, - for dash, space for separation) and blinks the LED with different timing rules:

Dot (·) → LED on for 0.3 seconds

Dash (–) → LED on for 1 second

Space → LED off for 2 seconds (between letters)

0.1 second pause → between each dot or dash

Timing Recap

Dot = 0.3s ON

Dash = 1.0s ON

Between dot/dash = 0.1s OFF

Between letters = 2.0s OFF

For routing.png-it's the result of:
•	192.168.15.0 / 255.255.255.0
•	192.168.16.0 / 255.255.255.0
•	192.168.17.0 / 255.255.255.0
•	192.168.18.0 / 255.255.255.0
•	192.168.19.0 / 255.255.255.0
•	192.168.20.0 / 255.255.255.0

Please allocate IP addresses to the routers (R1, R2, R3) as well as your users (Joe, Bill, Jane)
