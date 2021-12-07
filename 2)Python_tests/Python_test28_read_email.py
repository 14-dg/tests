# msg_template = """Hello {name},
# Thank you for joining {website}. We are very
# happy to have you with us.
# """ # .format(name="Justin", website='cfe.sh')

# def format_msg(my_name="Justin", my_website="cfe.sh"):
#     my_msg = msg_template.format(name=my_name, website=my_website)
#     return my_msg

# import email 
# import imaplib 

# host = 'imap.gmail.com'
# username = "daniel.graef14@gmail.com" 
# password = "entensuppe2020"


# def get_inbox():
#     mail = imaplib.IMAP4_SSL(host)
#     mail.login(username, password)
#     mail.select("inbox")
#     _, search_data = mail.search(None, 'UNSEEN')
#     my_message = []
#     for num in search_data[0].split():
#         email_data = {}
#         _, data = mail.fetch(num, '(RFC822)')
#         # print(data[0])
#         _, b = data[0]
#         email_message = email.message_from_bytes(b)
#         for header in ['subject', 'to', 'from', 'date']:
#             print("{}: {}".format(header, email_message[header]))
#             email_data[header] = email_message[header]
#         for part in email_message.walk():
#             if part.get_content_type() == "text/plain":
#                 body = part.get_payload(decode=True)
#                 email_data['body'] = body.decode()
#             elif part.get_content_type() == "text/html":
#                 html_body = part.get_payload(decode=True)
#                 email_data['html_body'] = html_body.decode()
#         my_message.append(email_data)
#     return my_message


# if __name__ == "__main__":
#     my_inbox = get_inbox()
#     print(my_inbox)
# # print(search_data)

# import sys
# import requests
# from datetime import datetime

# from send_mail import SendMail
# from formatting import format_msg


# def send(name, website=None, to_email=None, verbose=False):
#     assert to_email != None
#     if website != None:
#         msg = format_msg(my_name=name, my_website=website)
#     else:
#         msg = format_msg(my_name=name)
#     if verbose:
#         print(name, website, to_email)
#     # send the message
#     try:
#         send_mail(text=msg, to_emails=[to_email], html=None)
#         sent = True
#     except:
#         sent = False
#     return sent

# if __name__ == "__main__":
#     print(sys.argv)
#     name = "Unknown"
#     if len(sys.argv) > 1:
#         name = sys.argv[1]
#     email = None
#     if len(sys.argv) > 2:
#         email = sys.argv[2]
#     response = send(name, to_email=email, verbose=True)
#     print(response)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # environment variables
# host = 'imap.gmail.com'
# username = "daniel.graef14@gmail.com" 
# password = "entensuppe2020"

# text="hi, ich habe vergessen etwas zu schreiben. UPS"

# def send_mail(text='Email Body', subject='Hello World', from_email='Daniel Gräf <daniel.graef14@gmail.com>', to_emails="adina.graef@gmx.de", html=text):
#     assert isinstance(to_emails, list)
#     msg = MIMEMultipart('alternative')
#     msg['From'] = from_email
#     msg['To'] = ", ".join(to_emails)
#     msg['Subject'] = subject
#     txt_part = MIMEText(text, 'plain')
#     msg.attach(txt_part)
#     if html != None:
#         html_part = MIMEText(html, 'html')
#         msg.attach(html_part)
#     msg_str = msg.as_string()
#     # login to my smtp server
#     server = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     server.ehlo()
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(from_email, to_emails, msg_str)
#     server.quit()
#     # with smtplib.SMTP() as server:
#     #     server.login()
#     #     pass

# send_mail(text='HI', subject='hallo Mama', from_email='daniel graef <daniel.graef14@gmail.com>', to_emails=["adina.graef@gmx.de"], html="ES FUNKTIONIERT WHOOOOOOOOOHOOOOO!!!!!!")












# import email
# import imaplib

# username = "daniel.graef14@gmail.com"
# password = "entensuppe2020"

# mail = imaplib.IMAP4_SSL("imap.gmail.com") # https://myaccount.google.com/lesssecureapps muss aktiviert werden
# mail.login(username, password)

# mail.select("inbox")

# #Create new folder
# mail.create("item2")

# #list Folders
# folders=mail.list()
# print(folders)

# result, data = mail.uid("search", None, "ALL")

# inbox_item_list = data[0].split()

# for item in inbox_item_list:    
#     result2, email_data = mail.uid("fetch", item, "(RFC822)")
#     raw_email = email_data[0][1].decode("utf-8")
#     email_message = email.message_from_string(raw_email)

#     to_ = email_message["To"]
#     from_ = email_message["From"]
#     subject_ = email_message["Subject"]

#     counter = 1

#     for part in email_message.walk():
#         if part.get_content_maintype() == "multipart":
#             continue
#         filename = part.get_filename()
#         if not filename:
#             ext = ".html"
#             filename = "msg-part-%08d%s" % (counter, ext)
#         counter += 1
    
#     "save file"
#     content_type = part.get_content_type()
#     # print(subject_)
#     # print(content_type)

#     if "plain" in content_type:
#         print(part.get_payload)
#     elif "html" in content_type:
#         pass
#     else:
#         pass










# import imaplib
# import email
# from email.header import decode_header
# import webbrowser
# import os

# import time

# #acount creditinials
# username = "daniel.graef14@gmail.com" 
# password = "entensuppe2020"

# def clean(text):
#     # clean text for creating a folder
#     return "".join(c if c.isalnum() else "_" for c in text)


# # create an IMAP4 class with SSL 
# imap = imaplib.IMAP4_SSL("imap.gmail.com")
# # authenticate
# imap.login(username, password)


# status, messages = imap.select("INBOX")
# # number of top emails to fetch
# N = 1
# # total number of emails
# messages = int(messages[0])
# print(messages)


# #   s=messages

# #   timer_start = time.time()
# #   while s==messages:
# #       status, messages = imap.select("INBOX")
# #       messages = int(messages[0])
# #       time.sleep(10)
# #       print("nothing")

# #   print(time.time()-timer_start)
# #   print("Neue Emails:"+str(messages-s))



# for i in range(messages, messages-N, -1):
#     # fetch the email message by ID
#     res, msg = imap.fetch(str(i), "(RFC822)")
#     for response in msg:
#         try:
#             if isinstance(response, tuple):
#                 # parse a bytes email into a message object
#                 msg = email.message_from_bytes(response[1])
#                 # decode the email subject
#                 subject, encoding = decode_header(msg["Subject"])[0]
#                 if isinstance(subject, bytes):
#                     # if it's a bytes, decode to str
#                     subject = subject.decode(encoding)
#                 # decode email sender
#                 From, encoding = decode_header(msg.get("From"))[0]
#                 if isinstance(From, bytes):
#                     From = From.decode(encoding)
#                 print("Subject:", subject)
#                 print("From:", From)
#                 # if the email message is multipart
#                 if msg.is_multipart():
#                     # iterate over email parts
#                     for part in msg.walk():
#                         # extract content type of email
#                         content_type = part.get_content_type()
#                         content_disposition = str(part.get("Content-Disposition"))
#                         try:
#                             # get the email body
#                             body = part.get_payload(decode=True).decode()
#                         except:
#                             pass
#                         if content_type == "text/plain" and "attachment" not in content_disposition:
#                             # print text/plain emails and skip attachments
#                             print(body)
#                         elif "attachment" in content_disposition:
#                             # download attachment
#                             filename = part.get_filename()
#                             if filename:
#                                 folder_name = clean(subject)
#                                 if not os.path.isdir(folder_name):
#                                     # make a folder for this email (named after the subject)
#                                     os.mkdir(folder_name)
#                                 filepath = os.path.join(folder_name, filename)
#                                 # download attachment and save it
#                                 open(filepath, "wb").write(part.get_payload(decode=True))
#                 else:
#                     # extract content type of email
#                     content_type = msg.get_content_type()
#                     # get the email body
#                     body = msg.get_payload(decode=True).decode()
#                     if content_type == "text/plain":
#                         # print only text email parts
#                         print(body)
#                 if content_type == "text/html":
#                     # if it's HTML, create a new HTML file and open it in browser
#                     folder_name = clean(subject)
#                     if not os.path.isdir(folder_name):
#                         # make a folder for this email (named after the subject)
#                         os.mkdir(folder_name)
#                     filename = "index.html"
#                     filepath = os.path.join(folder_name, filename)
#                     # write the file
#                     open(filepath, "w").write(body)
#                     # open in the default browser
#                     webbrowser.open(filepath)
#                 print("="*100)
#         except Exception:
#             pass
# # close the connection and logout
# imap.close()
# imap.logout()














#TODO to read all your unread messages in gmail (just change N to how far you have to look for unread messages) 
#FIXME DOESN'T WORK YET
#! https://myaccount.google.com/lesssecureapps muss aktiviert werden


# import imaplib
# import email
# from email.header import decode_header
# import webbrowser
# import os

# import time

# #acount creditinials
# username = "daniel.graef14@gmail.com" 
# password = "entensuppe2020"

# def clean(text):
#     # clean text for creating a folder
#     return "".join(c if c.isalnum() else "_" for c in text)


# # create an IMAP4 class with SSL 
# imap = imaplib.IMAP4_SSL("imap.gmail.com")
# # authenticate
# imap.login(username, password)


# status, messages = imap.select("INBOX")
# # number of top emails to fetch
# N = 70
# # total number of emails
# messages = int(messages[0])
# print(messages)

# for i in range(messages, messages-N, -1):
#     # fetch the email message by ID
#     res, msg = imap.fetch(str(i), "(RFC822)")
#     for response in msg:
#         if isinstance(response, tuple):
#             # parse a bytes email into a message object
#             msg = email.message_from_bytes(response[1])