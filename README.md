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

Example output:

```
SOS
> encabulate
ENTERING ENCABULATOR RECOVERY SYSTEM. OPTIONS 1 INITIATE SIDE FUMBLING 2 ALIGN SPURVING BEARINGS 3 REVERSE TREMIE PIPE
> 3
ERROR TREMIE PIPE NONREVERSIBLE
> 2
MODIAL INTERACTION INITIATED. OPTIONS 1 UNWIND LOTUS O DELTOID 2 INCREASE DEPLENERATION 3 CONNECT GIRDLESPRING ON DOWN END OF GRAMMETER 4 CONNECT SEVENTH CONDUCTOR TO GIRDLESPRING
> 4
PANAMETRIC FAN ACTIVATED. MODIAL INTERACTION STABLE. DEFAULT CONFIGURATION MISSING. MANUALLY ENTER MARZELVANE TYPE TO COMPLETE RECOVERY
> hydrocoptic
RECOVERY SUCCESSFUL. REBOOT Y N?
```
