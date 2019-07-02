# CALT&CK (ATT&CK Plug-In for CALDERA)

Serve the ATT&CK website directly from the CALDERA server. 

## Installation

First install CALDERA server as usual, then do the following.

```bash
cd /path/to/caldera/installation
cd plugins
git clone --recursive https://github.com/mitre/caltack.git

```

Add the caltack plugin to the `plugins` section of the CALDERA config file.  For example:

```
# conf/local.yml
...
plugins:
  - stockpile
  - sandcat
  - gui
  - chain
  - caltack
...

```