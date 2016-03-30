import csv
import urllib
from BeautifulSoup import BeautifulStoneSoup
import os
import subprocess
import re
i=0
direct_output=subprocess.check_output ('''curl -X POST -H "Cache-Control: no-cache" -H "Postman-Token: c5fd4fc2-87d4-6b09-993c-5d3a1514a03e" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -F "sellerId=140" -F "isAjax=1" -F "productId=3090" 'http://www.buildzar.com/marketplace/marketplace/configPrice/''',shell=True)
Soup = BeautifulStoneSoup(direct_output)
print s