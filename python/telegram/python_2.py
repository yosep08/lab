import http.client
import ssl

conn = http.client.HTTPSConnection("172.18.140.38", context = ssl._create_unverified_context())
payload = ''
headers = {
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='
}
conn.request("POST", "/api/v2/job_templates/15/launch/", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))

