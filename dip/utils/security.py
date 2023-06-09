import os
import hmac
import hashlib
import pathlib
import subprocess
import string, random

from flask import Blueprint, current_app


ALLOWED_IMAGE_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def generate_password_hash(password, salt):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()


def is_correct_password(plain_password, hashed_password, salt):

    return generate_password_hash(plain_password, salt) == hashed_password


def is_valid_signature(identity, secret_key):

    username = identity.get('username', '')
    role = identity.get('role', '')

    signature = identity.get('signature', '')

    return hmac.compare_digest(
        signature,
        create_signature(username, role, secret_key)
    )


def create_signature(username, role, secret_key):
    msg = username + role

    signature = hmac.new(
        secret_key.encode('utf-8'),
        msg.encode('utf-8'), hashlib.sha256
    ).hexdigest()

    return signature


# def remove_image_metadata(filename):
#     filepath = pathlib.Path(current_app.root_path).parent / \
#         current_app.config["PATHS"]["user_images"] / filename
#     command = f'exiftool -EXIF= { filepath }'
#     os.system(command)


def remove_image_metadata(filename):
    filepath = pathlib.Path(current_app.root_path).parent / \
        current_app.config["PATHS"]["user_images"] / filename
    command = ['exiftool', '-EXIF=', str(filepath)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise Exception(f"Извините, абонент временно недоступен")
    return output.decode().strip()


def generate_random_string():
    length = 64
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for iter in range(length))
