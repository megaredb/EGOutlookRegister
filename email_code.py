from imap_tools import MailBox, A
from bs4 import BeautifulSoup


def get_code(name) -> str:
    with MailBox('imap-mail.outlook.com', port=993).login(name,
                                                          'PASSr544bb1', 'INBOX') as mailbox:
        to_return = None
        for message in mailbox.fetch(A(from_="help@accts.epicgames.com")):
            soup = BeautifulSoup(message.html, "html.parser")
            elements = soup.find_all('div', attrs={'style': "font-family: sans-serif; mso-line-height-rule: exactly; "
                                                            "color:#202020; text-align: center; font-size: 26px; "
                                                            "line-height: 32px; line-height: 100%; letter-spacing: 2px;"})
            if elements[1].get_text().strip() is not None:
                to_return = elements[1].get_text().strip()
        return to_return
