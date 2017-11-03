

with open(fname) as f:
    content = f.readlines()
	content = content.lower()
	currentFill = ""
	While True:
		if(content.contains("var1 var2")):
			currentFill = content
		else:
			content = content.replace("var", "")
			p = content.split(":")
			pos = p[1].split(",");
			currentFill.replace("var" + p, pos.random())
	
	