#!/usr/bin/env python3

import re

with open('link_list.txt') as f:
	puppets = f.read().split('\n')

puppets = list(filter(None, puppets))
totalcount = len(puppets)
print('The total count of issues is',totalcount)
links = open('9003samazinglistofcards.html', 'w')

links.write("""
<!DOCTYPE html>
<html>
<head>
<style>
td.createcol p {
	padding-left: 10em;
}

p{
	font-family: 'Segoe UI';
}
a {
	text-decoration: none;
    font-family: 'Segoe UI';
	color: black;
}

a:visited {
	color: grey;
}

table {
	border-collapse: collapse;
	max-width: 1000%;
	border: 1px solid grey;
	margin-left:auto; 
    margin-right:auto;
}

tr, td {
	border-bottom: 2px solid green;
}
tr.end, td.end {
	border-bottom: 5px solid rgb(216, 216, 32);
}
td {
	font-family: 'Segoe UI';
	padding: 0.5em;
}

body {
	text-align:center;
	padding-top: 50px;
	margin:0;
}

tr:hover {
	background-color: lightgrey;
}

</style>
</head>
<body onkeypress="select()">
<p>q and e to navigate links, enter or w to open and select next</p>
<table>
""")


for idx, k in enumerate(puppets):
	canonical = k.lower().replace(" ", "_")
	escaped_canonical = re.escape(canonical)
	links.write("""<tr>""");
	links.write("""<td>{} of {}</td>""".format(idx+1, totalcount));
	links.write("""<td><p><a target="_blank" href="{}">Link to Card</a></p></td>""".format(canonical, canonical, canonical))
	links.write("""</tr>\n""")
links.write("""<td><p><a target="_blank" href="https://this-page-intentionally-left-blank.org/">Done!</a></p></td>""".format(canonical))
links.write("""
</table>
<script>
const body = document.querySelector('body');

var count = 0;
document.querySelectorAll('a')[count].style.color = "red";
function select(e){
	if(e==undefined){
		return;
	}
    document.querySelectorAll('a')[count].style.color = "black";
	if (window.event) keycode = window.event.keyCode; 	// IE
	else if (e) keycode = e.which;
	if (keycode == 13 || keycode == 87) { 
		
		document.querySelectorAll('a')[count].click()
		count+=1;
	}
	else if (keycode == 81){
		count-=1;
	}
	else if (keycode == 69){
		count+=1;
	}
	if(count<0){
		count = 0;
	}else if(count>=document.querySelectorAll('a').length){
		count = document.querySelectorAll('a').length-1;	
	}
	document.querySelectorAll('a')[count].style.color = "red";
	if(count>1)
	document.querySelectorAll('a')[count-1].scrollIntoView();
	
}
body.onkeydown=select;
</script>
</script>
</body>
""")
