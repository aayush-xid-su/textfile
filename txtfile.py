# Color snippets
black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
nc = "\033[00m"

# Regular Snippets
ask = f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error = f"{blue}[{white}!{blue}] {red}"
info = f"{yellow}[{white}+{yellow}] {cyan}"
info2 = f"{green}[{white}•{green}] {purple}"

banner = f"""                                                                                                              
{red}      nnnnz   nnnt  nnn   onnnnnp        znlllo     nnnnnnnnnnr  nnn     znlllq                aaaasyush  xidsuuuu       
{red}       h000ss000q  u000v  b00000000d   j000000000l z0000000000f  000z  g000000000                aaaayush xiddddd         
{blue}       t000000    u000v  b00h   000g l000x   t000t    s000      000z x000t   e00i                  ayush xd          
{blue}        b0000i    u000v  b00h   000e i000     000q    s000      000z s000            c   u         ayush xd           
{red}       z000j000c   u000v  b00h  p000l t000n   i000x    s000      000z y000h   c00k    mwwws       aaaayush xiddddd         
{red}      l000u  0000x u000v  b00000000t   z00000000a      s000      000z   a0000000i               aaaasyush  xidsuuuu  
{cyan}                                         [{blue}By {green}Aayush-xid-su{cyan}]
"""

# -*- cofing: utf-8 -*-
import os
import sys
import collections
import string

script_name = sys.argv[0]

res = {
    "total_lines":"",
    "total_characters":"",
    "total_words":"",
    "unique_words":"",
    "special_characters":""
}

try:
    textfile = sys.argv[1]
    with open(textfile, "r", encoding = "utf_8") as f:

        data = f.read()
        res["total_lines"] = data.count(os.linesep)
        res["total_characters"] = len(data.replace(" ","")) - res["total_lines"]
        counter = collections.Counter(data.split())
        d = counter.most_common()
        res["total_words"] = sum([i[1] for i in d])
        res["unique_words"] = len([i[0] for i in d])
        special_chars = string.punctuation
        res["special_characters"] = sum(v for k, v in collections.Counter(data).items() if k in special_chars)

except IndexError:
    print('Usage: %s TEXTFILE' % script_name)
except IOError:
    print('"%s" cannot be opened.' % textfile)

print(banner)
print("\n")
print(res)