import imaplib

class EmailServer_Service:
    def __init__(self):
        self.email_server = None
        self.default_mailbox = 'inbox'

    def connect(self) -> None:
        if not self.email_server:
            self.email_server = imaplib.IMAP4_SSL('imap.gmail.com')
        
    def login(self, email_address: str, password: str) -> None:
        self.connect()
        self.email_server.login(email_address, password)
        self.set_mailbox(self.default_mailbox)
        
    def set_mailbox(self, mailbox: str) -> None:
        self.email_server.select(mailbox)

    def close_connection(self) -> None:
        if self.email_server:
            self.email_server.logout()