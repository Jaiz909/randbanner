```
:::::::..    :::.   :::.    :::.:::::::-.  :::::::.    :::.   :::.    :::.:::.    :::..,:::::: :::::::..   
;;;;``;;;;   ;;`;;  `;;;;,  `;;; ;;,   `';, ;;;'';;'   ;;`;;  `;;;;,  `;;;`;;;;,  `;;;;;;;'''' ;;;;``;;;;  
 [[[,/[[['  ,[[ '[[,  [[[[[. '[[ `[[     [[ [[[__[[\. ,[[ '[[,  [[[[[. '[[  [[[[[. '[[ [[cccc   [[[,/[[['  
 $$$$$$c   c$$$cc$$$c $$$ "Y$c$$  $$,    $$ $$""""Y$$c$$$cc$$$c $$$ "Y$c$$  $$$ "Y$c$$ $$""""   $$$$$$c    
 888b "88bo,888   888,888    Y88  888_,o8P'_88o,,od8P 888   888,888    Y88  888    Y88 888oo,__ 888b "88bo,
 MMMM   "W" YMM   ""` MMM     YM  MMMMP"`  ""YUMMMP"  YMM   ""` MMM     YM  MMM     YM """"YUMMMMMMM   "W" 
```

Randbanner is a simple script to generate banners. Just copy randbanner to your path (`~/bin` is good), then add a call to the bottom of your `~/.bashrc` or `~/.zshrc`, or run `python setup.py install` and enjoy.

If you just run `randbanner` your username will be printed in a random font and colour.

## Installation
* Run `python setup.py install` as root to install system wide.
* Run `python setup.py install --user` to install for the current user only. Ensure `$HOME/.local/bin` is in your path.

## Usage
```
usage: randbanner [-h] [--all] [-t TEXT]

optional arguments:
  -h, --help            show this help message and exit
  --all, -a             Display all fonts
  -t TEXT, --text TEXT  Text to display
```
