# Candy on Google App Engine

Candy Project Page: http://amiadogroup.github.com/candy/

**THIS IS EXPERIMENTAL**

## Quirks
* using urlfetch instead of proxy redirect (like mod_rewrite / mod_proxy on Apache) is terrible slow, expect lots of timeouts.
* urlfetch does timeout after 15 seconds and is therefore not really suited for long-polling