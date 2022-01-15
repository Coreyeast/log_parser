import re


def read_document():
    valid_ip_counter = 0
    valid_url_counter = 0
    log = open("task.log", "rt")

    for line in log:
        ipv4_regex = re.match(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        if ipv4_regex != None:
            add_ips(ipv4_regex.group(0))
            valid_ip_counter += 1

        try:
            log_word_list = line.split()
            add_urls(log_word_list[log_word_list.index('"GET') + 1])
            valid_url_counter += 1
        except:
            print("No valid GET request on this line")

    log.close()
    validate(valid_ip_counter, valid_url_counter)


def add_ips(ipv4_regex):
    if ips.get(ipv4_regex):
        ips[ipv4_regex] = ips[ipv4_regex] + 1
    else:
        ips[ipv4_regex] = 1


def add_urls(url):
    if urls.get(url):
        urls[url] = urls[url] + 1
    else:
        urls[url] = 1


def validate(valid_ip_count, valid_url_count):
    # validation between valid ips/urls found on each line vs total sum of counter values in ips/urls dict
    ip_values = ips.values()
    url_values = urls.values()

    # notifies if there's an issue
    if sum(ip_values) != valid_ip_count:
        print(f"The number of valid IPs ({valid_ip_count}) read and the sum value of IPs ({sum(ip_values)}) don't "
              f"match.")
    if sum(url_values) != valid_url_count:
        print(
            f"The number of valid URLs ({valid_url_count}) read and the sum value of URLs ({sum(url_values)}) don't "
            f"match.")


def print_results():
    print("Number of unique IPs:", len(ips))
    print("Top 3 IPs:", ips[:3])
    print("Top 3 URLs:", urls[:3])


if __name__ == '__main__':
    # Dictionary variable declaration
    ips = {}
    urls = {}

    read_document()

    # Sorts the dict by value
    # Reverse set to True - values appear in descending order
    ips = sorted(ips.items(), key=lambda item: item[1], reverse=True)
    urls = sorted(urls.items(), key=lambda item: item[1], reverse=True)

    print_results()
