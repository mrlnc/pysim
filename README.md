pySim - SIM card utility
====================================================

> pySim reads and writes data to programmable SIM/USIM cards.

This is useful particularly if you are running your own cellular
network and want to issue your own SIM/USIM cards for that network.
For most pySim features, you will need a *programmable* SIM card and
sufficient credentials (ADM PIN). You cannot re-program the SIM cards
issued by your mobile operator.

`pySim-shell.py` is the main script. It supports reading and writing in
an interactive shell. The scripts `pySim-read` and `pySim-prog`
exist for more specialized use-cases like bulk-programming. If you are
unsure where to start, use `pySim-shell`.

![pySim-shell](./shell.svg)

Installation
------------

Clone from the official repository ([cgit](http://git.osmocom.org/pysim/)):
```
git clone git://git.osmocom.org/pysim.git
```

Install the Python dependencies (see [requirements.txt](./requirements.txt)), e.g., using `pip`:
```
pip3 install -r requirements.txt
```

You're ready to run `./pySim-shell.py`

Usage
-----

Check out the [pySim User Manual](https://people.osmocom.org/laforge/tmp/pysim-doc-test/html/). Alternatively, try `--help` for command line options or call `help` within the shell.
```
./pySim-shell.py --help
```

```
pySIM-shell (MF)> help

Documented commands (use 'help -v' for verbose/'help <topic>' for details):
ISO7816 Commands
================
activate_file  close_channel    disable_chv  open_channel  unblock_chv
…
```

Note that some commands are file-specific and require selecting a file.

There is also a 45 minute workshop recording,
[available here ](https://people.osmocom.org/tnt/osmodevcall/osmodevcall-20210409-laforge-pysim-shell_h264_420.mp4) (MP4, 394MB).


Project Homepage
----------------

pySim is an osmocom project.
* [Homepage](http://osmocom.org/projects/pysim)
* [Wiki](http://osmocom.org/projects/pysim/wiki)
* [Issue Tracker](http://osmocom.org/projects/pysim/issues)

### Mailing List

Discussions related to pySim are happening on the
openbsc@lists.osmocom.org mailing list. For subscription and archives, see
<https://lists.osmocom.org/mailman/listinfo/openbsc>

Please observe the [Osmocom Mailing List
Rules](https://osmocom.org/projects/cellular-infrastructure/wiki/Mailing_List_Rules)
when posting.

### Contributing
Submit patches to [gerrit.osmocom.org](https://gerrit.osmocom.org) for review. Please
consider the [Guidelines](https://osmocom.org/projects/cellular-infrastructure/wiki/Gerrit)
and our [Coding Standards](https://osmocom.org/projects/cellular-infrastructure/wiki/Coding_standards).
