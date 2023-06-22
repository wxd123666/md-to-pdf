import markdown
import pdfkit
import os

# /Users/wuxiaodong/1project/MIT6.S081/lec03-os-organization-and-system-calls
path = input("输入路径")
out_path = path+"/out/"
a = r"/usr/local/bin/wkhtmltopdf"
configuration = pdfkit.configuration(wkhtmltopdf=a)
for i in os.listdir(path):
    if i.endswith("md"):
        with open(path+"/"+i,"r",encoding="utf-8") as f:
            text = f.read()
        html = markdown.markdown(text, output_format='html')
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        pdfkit.from_string(html, output_path=out_path+"{}.pdf".format(i.split(".md")[0]),configuration=configuration, options={'encoding':'utf-8',"enable-local-file-access":True})