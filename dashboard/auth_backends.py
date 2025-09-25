from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db import connection
import hashlib
import hmac

class AdminTableBackend(BaseBackend):
    def authenticate(self, request, username =None, password = None):
        with connection.cursor() as cursor:
            cursor.execute("select id,username,password from admin where username = %s",[username])
            row = cursor.fetchone()

            if row:
                admin_id, db_username, db_password_hash = row

                # Konversi memoryview ke bytes
                if isinstance(db_password_hash, memoryview):
                    db_password_hash = db_password_hash.tobytes()

                # Hitung sha256 dari input password
                input_hash = hashlib.sha256(password.encode()).digest()

                # Gunakan hmac.compare_digest untuk keamanan timing attack
                if hmac.compare_digest(input_hash, db_password_hash):
                    user, created = User.objects.get_or_create(username=db_username)
                    return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None