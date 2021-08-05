import phonenumbers
from phonenumbers import timezone,geocoder,carrier

num = input("Input the phone number: ")
final = "+1" + num
print(final)
phoneNum = phonenumbers.parse(final)

timeZone = timezone.time_zones_for_number(phoneNum)

carrier = carrier.name_for_number(phoneNum, 'en')

region = geocoder.description_for_number(phoneNum, 'en')

print(phoneNum)
print(timeZone)
print(carrier)
print(region)
