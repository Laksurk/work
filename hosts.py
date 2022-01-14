import requests
import sys

def get_ip(domain):
    r = requests.get("https://ipaddress.com/website/" + domain)
    assert r.status_code == 200, "Failed to get " + domain
    text = r.text
    s = '<ul class="comma-separated"><li>'
    i = text.find(s) + len(s)
    ip = text[i:text.find('<', i)]
    return ip


t = ''
domains = ['github.com', 'api.github.com', 'github.global.ssl.fastly.net']
for domain in domains:
    print(domain, end=' ')
    sys.stdout.flush()
    ip = get_ip(domain)
    print(ip)
    t += ip + ' ' + domain + '\n'

file = open('C:/Windows/System32/drivers/etc/HOSTS', 'r')
f = file.read()
file.close()
s = '# GitHub Start\n'
i = f.find(s) + len(s)
j = f.find('# GitHub End')
f = f[:i] + t + f[j:]
file = open('C:/Windows/System32/drivers/etc/HOSTS', 'w')
file.write(f)
file.close()