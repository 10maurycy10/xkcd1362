# XKCD 1362 Simulator

[XKCD 1362](https://xkcd.com/1362/) is one of those interactive XKCD, even including a full on text adventure.
However, ever since the invention of the telephone, many people lack the clicking skills (and patience) to enjoy the comic.
This program (depending only on the python standard library) lets you explore the xkcd in a terminal, without relying on clicking skills or patience.

To use it, first you must fetch the data for the xkcd with the `getswitchboard.sh` script:

```
./getswitchboard.sh
```

Alternatively, if you are on windows or don't have curl installed, go to (https://xkcd.com/2445/switchboard.json) and save it as `switchboard.json` in the same directory as the `emulator.py` script.
Once you have the file, you can simply run the program.

```
python3 emulator.py
```

You can type `/help` to see a list of options in a given situation.

