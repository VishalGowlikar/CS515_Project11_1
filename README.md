# CS 515 Project 1

## Author Information
Gowlikar Vishal
Vgowlika@stevens.edu

[Github Repository](https://github.com/VishalGowlikar/CS515_Project_1)

## Spending the time on the project
I spent around 20 hours approximately on the project.

## Testing of the code
1.I began by sketching out the code's logic on paper, then put it into action on my computer terminal for testing. 

 

## Unresolved Bugs or Issues
1. I had quiet experience to push the files to git using gitbash but due to some extensions in my computer i could not commit and push the files to github account using gitbash, 
 moreover i could not Handle Stdin by reading the file.
2. the other bug was in the gron where there is a lot of attention needed to add more keys and value pass other json file to the gron which needs a lot a eye blinks.



## Examples of difficult bugs resolved
1. the difficult bug was in the argparse which was new to me and my machine but understood the practical problem how to handle it with the terminal and the other bug is in the 
wc.py to get the exact output like -w,-wlc,lc,wh and in the gron the i have resovled how to use the json.obj on the python but the hard task was to add the keys and values in the list then in the keys and values.
2. at a moment i could not handle the exception which blown my mind but i could manage with the exceptions.
3. In the csv problem i could not handle with the index errors and float parsing which could lead to precise error or other behaviour due to floating-oint arthimetic but got resolved it by using int.


## Extensions Implemented
1. **More advanced wc: Multple Files** : I have implemented the extension for wc where one can input multiple files and get the total count of characters, words, and lines. The following example shows the sample input and output for this.

```
$ python3 prog/wc.py wc_basic.in wc.huge.in
34    | 19 |  210   |  ['wc.huge.in'] 
5     | 4  |  20    |  ['wc_basic.in']  
39    | 23 |  410       total
```

2. **More advanced wc: Flags to control output**: I have implemented wc flags **-l**, **-w** and **-c**, to control output. The following example shows sample input and the sample output for this.
```
$ python3 prog/wc.py test/wc_basic.in -l -w
34 210 test/wc_basic.in
$ python3 prog/wc.py test/wc_basic.in -c
210 test/wc_basic.in
```

3. **Extension: More advanced gron: control the base-object name** : I have implemented the extension to control the main object name for gron. The following shows sample input and the sample output for the same.
```
$ python3 prog/gron.py eg.json 
o = {};
o.menu = {};
o.menu.id = "file"
o.menu.value = "File"
o.menu.popup = {};
o.menu.popup.menuitem = [];
o.menu.popup.menuitem[0] = {};
o.menu.popup.menuitem[0].value = "New"
o.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
o.menu.popup.menuitem[1] = {};
o.menu.popup.menuitem[1].value = "Open"
o.menu.popup.menuitem[1].onclick = "OpenDoc()"
o.menu.popup.menuitem[2] = {};
o.menu.popup.menuitem[2].value = "Close"
o.menu.popup.menuitem[2].onclick = "CloseDoc()"
```
**extension**: i have also implemented this by using the other example which is other input of keys and values in the json-obj naming the file as addgron.json for the gron. the following shows the sample of the input and output for the same:
```
$ python3 prog/gron.py addgron.json
json = {};
.menu = {};
.menu.id = "file";
.menu.popup = {};
.menu.popup.menuitem = [];
.menu.popup.menuitem[0] = {};
.menu.popup.menuitem[0].onclick = "CreateNewDoc()";
.menu.popup.menuitem[0].value = "New";
.menu.popup.menuitem[1] = {};
.menu.popup.menuitem[1].onclick = "opendoc()";
.menu.popup.menuitem[1].value = "Open";
.menu.popup.menuitem[2] = {};
.menu.popup.menuitem[2].onclick = "CloseDoc()";
.menu.popup.menuitem[2].value = "Close";
.menu.popup.menuitem[3] = {};
.menu.popup.menuitem[3].onclick = "SaveDoc()";
.menu.popup.menuitem[3].value = "Save";
.menu.popup.menuitem[4] = {};
.menu.popup.menuitem[4].onclick = "PrintDoc()";
.menu.popup.menuitem[4].value = "Print";
.menu.popup.menuitem[5] = {};
.menu.popup.menuitem[5].onclick = "FormatDoc()";
.menu.popup.menuitem[5].value = "Format";
.menu.popup.value = "file";
```

## Program 3: csv.py
For my Program 3 I have implemented the csvpy functionality, which takes input the columns number  and returns the sum of the columns. The following example highlights the working of csvpy functionality.
```
$ python3 prog/csvbasic.csv [1,3]
145.0,0

```
