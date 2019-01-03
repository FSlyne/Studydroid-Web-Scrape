from lxml import html
import requests
import re

packlist=[317053, 313374, 312695, 134520, 133919, 317053, 313374, 312695, 132107, 86229, 131177, 130286, 117219, 117219, 128014, 117220, 128014, 117224, 57056, 118220, 130009, 131092, 131971, 132108, 134037, 234556, 309600, 309591, 309625, 313384]

# packlist=[132107]

fle = {317053: "Evidence", 234556: "Evidence", 309625:"Evidence", 
313374: "Equity", 117220: "Equity", 309600: "Equity", 313384: "Equity",
312695: "Public Law",
134520: "Contract", 117224: "Contract", 
133919: "Tort", 118220: "Tort", 134037: "Tort", 
132107: "Criminal", 131092: "Criminal", 132108: "Criminal", 
86229: "Interview", 
131177: "Property", 130009: "Property", 
130286: "Constitutional", 
117219: "Doctrines", 
128014: "EU", 131971: "EU", 
57056: "General", 
309591: "Corporate" }

fle={74737:"CISSP", 56683:"CISSP"} 

for pack in fle.keys():
  bgn=0; elemno = 10
  while elemno > 5:
     page = requests.get('http://www.studydroid.com/index.php?page=viewPack&packId=%d&begin=%d'%(pack,bgn))
     q=unicode(page.content,'utf-8')
     q=q.replace("<p>"," ")
     q=q.replace("<P>"," ")
     q=re.sub(r'[^\x20-\x7f]',r'. ',q)
     
     tree = html.fromstring(q)

     card=tree.xpath('//div[@class="view_card"]')
#     front_card=tree.xpath('//div[@name]')
     elemno=0
     line=""
     for label in card:
        side=label.xpath("@name")[0]
        txt = label.text_content()
        if "front" in side:
           if len(line) > 5:
              with open("%s.csv" % fle[pack],"a+") as f:
                 f.write(line+"\n")
#              print fle[pack],side,pack,bgn,line
           line=txt
        else:
            line=line+"\t"+txt
        elemno+=1
     bgn+=50

