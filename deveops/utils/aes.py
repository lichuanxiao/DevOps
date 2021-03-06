# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-12
# Author Yo
# Email YoLoveLife@outlook.com
from deveops.settings import SECRET_KEY
KEY = SECRET_KEY
KEY_LENGTH = 16
from itsdangerous import JSONWebSignatureSerializer, BadSignature, SignatureExpired

def encrypt(text):
    s = JSONWebSignatureSerializer(SECRET_KEY)
    return s.dumps(text)


def decrypt(text):
    s = JSONWebSignatureSerializer(SECRET_KEY)
    try:
        return s.loads(text)
    except BadSignature:
        return {}
