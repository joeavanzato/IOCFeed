import requests
def get_remote_text(url):
    """
    Receive a text file from a remote location containing IOCs
    :param url:
    :return:
    """
    try:
        data = requests.get(url)
    except:
        print(f"Error Contacting {url}")
        return None
    return data