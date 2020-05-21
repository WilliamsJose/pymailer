import smtplib
from email.message import EmailMessage


class Pymailer(object):

	def __init__(self):
		self.msg = EmailMessage()
		self.service = "smtp.gmail.com"
		self.subject = None
		self.sender = None
		self.sender_key = None
		self.remitter = None
		self.body = None
		self.attachment_type = None
		self.attachment_path = None

	def prepare_email(self, sender, remitter, sender_key):
		self.sender = sender
		self.remitter = remitter
		self.sender_key = sender_key

	def set_attachment(self, attachment_path, attachment_type):
		self.attachment_path = attachment_path
		self.attachment_type = attachment_type

		# assuming it's a txt for now
		with open(self.attachment_path, "r") as f:
			atch = f.read()
			self.msg.add_attachment(atch, subtype=self.attachment_type, filename=attachment_path)

	def set_content(self, subject, body):
		self.subject = subject
		self.body = body

	def send(self):
		self.msg["Subject"] = self.subject
		self.msg["From"] = self.sender
		self.msg["To"] = self.remitter
		self.msg.set_content(self.body)

		with smtplib.SMTP_SSL(self.service, 465) as smtp:
			smtp.login(self.sender, self.sender_key)
			smtp.send_message(self.msg)


