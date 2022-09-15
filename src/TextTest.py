from etext import send_sms_via_email

phone_number = "336-486-1273"
message = "Baylor"
provider = "Verizon"
sender_credentials = ("uberskier@yahoo.com", "oafviksrbnkhsmnm")

send_sms_via_email(
    phone_number, message, provider, sender_credentials, smtp_server="smtp.mail.yahoo.com", subject="hello"
)
