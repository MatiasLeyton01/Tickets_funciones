from django.test import TestCase
from rest_framework_simplejwt.tokens import AccessToken

# Decode and inspect an example token
token = AccessToken("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwOTA1MTg3LCJpYXQiOjE3MzA5MDE1ODcsImp0aSI6Ijc3NjFjOTVmZTA5ODQyMDI4OWZiOWI4ZDkzMTIyNTFmIiwidXNlcl9pZCI6MjIzNDU2NzgsIm5vbV91c3VhcmlvIjoiSnVhbiBGcmFuY2lzY28gR2FyY1x1MDBlZGEgRmxvcmVzIiwicm9sZSI6ImFkbWluIn0.DI3djl8uvr6nLSwfG_38qIXUnexCWden_BnCBxq6l3s")
print(token.payload)
# Create your tests here.
