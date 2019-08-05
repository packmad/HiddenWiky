# HiddenWiky
HiddenWiky is a simple active link scraper for "[The Hidden Wiki](http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page)", it does not need any Python packages!

(for now) It just prints a JSON ([example](https://raw.githubusercontent.com/packmad/HiddenWiky/master/outputs/2019-08-05_16-20.json)) with:
* onion link
* title
* description



If *torsocks* works, you have all the necessary dependencies.
In order to install and test *torsocks* just type:

```shell script
sudo apt install torsocks
curl 'https://api.ipify.org'
torsocks curl 'https://api.ipify.org'
```
