# HiddenWiky
HiddenWiky is a simple active link scraper for "[The Hidden Wiki](http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page)" onion site.
 
It visits every link and, in the end, it creates a JSON file ([example](https://raw.githubusercontent.com/packmad/HiddenWiky/master/hiddenwiky/2019-11-08_10%3A49.json)) with:
* active onion link
* title
* description

HiddenWiky does not need any Python packages, it just needs [torsocks](https://trac.torproject.org/projects/tor/wiki/doc/torsocks).

In order to install and test *torsocks* just type:

```shell script
sudo apt install torsocks
curl 'https://api.ipify.org'
torsocks curl 'https://api.ipify.org'
```
