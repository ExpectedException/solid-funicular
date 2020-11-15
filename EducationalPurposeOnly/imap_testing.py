import imaplib, email, os, time
from bs4 import BeautifulSoup


class MailRuImap:

    def __init__(self, imap_user, imap_pass):
        self.box = imaplib.IMAP4_SSL(
            host='imap.mail.ru',
            port=993,
        )
        self.box.login(imap_user, imap_pass)
        print('logged in')

    def _getIdListOfMails(self):
        self.box.select()
        typ, data = self.box.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        return reversed(id_list)

    def _getMsgById(self, id):
        typ, data = self.box.fetch(id, '(RFC822)')
        msg_inner = email.message_from_bytes(data[0][1])
        return msg_inner

    def _getHTMLFromMSG(self, msg):
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                return part.get_payload()

    def _getLastLetterFromSteamWithSubject(self):  # , subject
        msg = False

        self.box.select()
        id_list = self._getIdListOfMails()

        for id in id_list:
            msg_inner = self._getMsgById(id)

            try:
                if ("noreply@steampowered.com" in str(msg_inner["From"])):
                    # if subject in str(msg_inner["Subject"]):
                    msg = msg_inner
                    break
            except:
                pass

        self.box.close()

        return msg

    def GetAccessCode(self):
        # sbj = "Access from new web or mobile device"
        # sbj = ""

        for n in range(5):
            os.system("echo .")
            time.sleep(1)

        msg = self._getLastLetterFromSteamWithSubject()
        if msg == False: return False

        soup = BeautifulSoup(
            self._getHTMLFromMSG(msg),
            features="html.parser"
        )
        return soup.find_all("span")[2].get_text()



imap_user = ''
imap_pass = ''
ms = MailRuImap(imap_user, imap_pass)
print(ms.GetAccessCode())
