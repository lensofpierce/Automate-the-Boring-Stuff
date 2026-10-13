import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')      # 415-555-4242
print('Input your message to tell your number: ')
text = input()
mo = phoneNumberRegex.search(text)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

phoneNumberRegexPar = re.compile(r'(\(\d\d\d\)) (\d\d\d)-(\d\d\d\d)')      #(415) 555-4242
print('Input your message to tell your number with parenthesis: ')
textp = input()
mop = phoneNumberRegexPar.search(textp)
print(mop.group())
print(mop.group(1))
print(mop.group(2))
print(mop.group(3))

batRegex = re.compile(r'Bat(man|mobile|copter|arang)')
print('Input your message to tell something bat-related (Batman, Batmobile, Batcopter, Batarang: ')
textb = input()
mob = batRegex.search(textb)
print(mob.group())
print(mob.group(1))
print(mob.group(2))
print(mob.group(3))
print(mob.group(4))

