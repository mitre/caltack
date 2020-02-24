# CALDERA plugin: CALT&CK 

A plugin to serve the ATT&CK website embedded inside the CALDERA server. 

[Read the full docs](https://github.com/mitre/caldera/wiki/Plugin:-caltack)

## Update procedure 

First, set the attack-website submodule to reference HEAD of the gh-pages branch and
commiting the new submodule reference to caltack.  Recently, `master` of attack-website
changed to contain the source code for building the site, while the `gh-pages` branch 
holds the built static site.

```bash
# cwd=/path/to/caltack
cd static/attack-website
git checkout gh-pages
git pull
cd ..
git add attack-website
git commit -m 'update attack-website'
```

