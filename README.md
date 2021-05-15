# HTB-Phonebook
Exploit for the phonebook challenge on HackTheBox

## Running
You need Python 3.
Simply execute in a shell `python3 script.py http://<instance URL>:<port>/login`.

## Explanation
The website uses [Active Directory](https://en.wikipedia.org/wiki/Active_Directory).
We first see that entering `*` as both username and password will log us in.
A cookie is then set. If we try to base64 decode it twice (and ignoring garbage with `base64 -i`),
you will see something like `authuser string reese`. `reese` is the user which we're going to find the password of.
If we try each letter in `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_` as the password plus
`*`, we see that we get logged in with `H*`. Unitl we have a good password which we can log in with
without adding a trailing `*`, we try every letter after the ones we've already found.

