# import  httplib

# conn =  httplib.HTTPConnection("www.buildzar.com")

# payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sellerId\"\r\n\r\n140\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isAjax\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"productId\"\r\n\r\n3090\r\n-----011000010111000001101001--"

# headers = {
#     'Host': 'www.buildzar.com'
#     'Content-Length':'36'
#     'Connection': 'keep-alive'
#     'content-type': "multipart/form-data; boundary=---011000010111000001101001",
#     'x-requested-with': "XMLHttpRequest",
#     'cache-control': "no-cache",
#     'postman-token': "bff46129-2a6d-2391-f9fa-cf34851d5977"
#     }

# conn.request("POST", "/marketplace/marketplace/configPrice/", payload, headers)

# res = conn.getresponse()
# data = res.read()
# print">>>>>>>>>",data
