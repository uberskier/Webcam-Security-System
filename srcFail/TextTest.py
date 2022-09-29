from etext import send_sms_via_email

phone_number = "336-486-1273"
message = "Baylor"
provider = "Verizon"
sender_credentials = ("baylormatney@gmail.com", "bmeprefpbnyelmga")

send_sms_via_email(
    phone_number, message, provider, sender_credentials, subject="hello"
)
