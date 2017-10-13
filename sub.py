
def updatePage(page, template, tagSet):

    f2=open(page, "w+")

    with open(template) as f1:
        for line in f1:
            for key in tagSet:
                line = line.replace(key, tagSet[key])
            f2.write(line)
    f1.close()
    f2.close()
    
# --------------------------------------------------------------

tagSet1 = {
    "{title}":"This is the Title", 
    "{heading}":"This is the Heading", 
    "{body}":"This is the Body", 
    "{footer}":"This is the Footer",  
    "{add tag 1}":"This is another tag called 1", 
    "{add tag 2}":"This is another tag called 2" 
    }
    
tagSet2 = {
    "{title}":"This not is the Title", 
    "{heading}":"This is not the Heading", 
    "{body}":"This is not the Body", 
    "{footer}":"This is the Footer",  
    "{add tag 1}":"This is not another tag called 1", 
    "{add tag 2}":"This is not another tag called 2" 
    }

pages = {
    "index":"index2.html",
    "home":"home.html",
    "endPage":"endPage.html"
    }

tags = {
    "index": tagSet1,
    "home": tagSet1,
    "endPage": tagSet2
    }
    
templates = {
    "index": "template1.html",
    "home": "template2.html",
    "endPage":"template2.html"
    }

for key in pages:
    
    page = pages[key]
    template = templates.get(key, "template1.html")
    tagSet = tags.get(key, "tagSet1")
    
    updatePage(page, template, tagSet)
