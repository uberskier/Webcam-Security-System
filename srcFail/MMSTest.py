from etext import send_mms_via_email

file_path = "..\Camera-Pictures\BandFam.jpg"

mime_maintype = "image"
mime_subtype = "jpeg"

phone_number = "(336) 486-1273"

message = "Baylor Matney test 3"
provider = "Verizon"

sender_credentials = ("baylormatney@gmail.com", "tsdbioyqthfsgbje")

send_mms_via_email(
    phone_number,
    message,
    file_path,
    mime_maintype,
    mime_subtype,
    provider,
    sender_credentials,
)