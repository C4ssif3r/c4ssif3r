import requests
import threading

def get_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def check_proxy(proxy):
    try:
        ip_before = get_ip()
        proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
        response = requests.get('https://api.ipify.org', proxies=proxies)
        ip_after = response.text
        if ip_before != ip_after:
            with open('working_proxies.txt', 'a') as f:
                f.write(proxy + '\n')
    except:
        pass

if __name__ == '__main__':
    ip_before = get_ip()
    print('Your IP before:', ip_before)

    proxy_file = input('Enter the path to the proxy file: ')
    print ("running ...")
    with open(proxy_file, 'r') as f:
        proxies = [line.strip() for line in f]

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    ip_after = get_ip()
    print('Your IP after:', ip_after)
