import re

sentence="Hello my name is rohan paris and my phone number is 02367-245397"

phonenumberRegex=re.compile(r"\d\d\d\d\d-\d\d\d\d\d\d")
result=phonenumberRegex.search(sentence)
result.group()          #result= 02367-245397

phonenumberRegex=re.compile(r"{\d\d\d\d\d}-{\d\d\d\d\d\d}")
result=phonenumberRegex.search(sentence)
result.group(1)         #result= 02367
result.group(2)         #result= 245397
