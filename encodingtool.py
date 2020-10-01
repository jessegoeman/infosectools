string = '5YK%2F5YK65YK45YOs5YK95YK%2B5YOs5YOr5YOs5YK%2B5YK95YK%2B5YOt5YK95YOr5YOi5YOs5YOs5YOr5YOv5YOj5YK45YOp5YK65YK55YOv5YOi5YOs5YOq5YK%2F5YK%2F5YOr'
stripped = string.split('5YK')
stripped2 = [x.split('5YO') for x in stripped]
print(stripped2)

lowerstring = ''
for char in string:
    if char.islower():
        lowerstring+=char

print(lowerstring)
