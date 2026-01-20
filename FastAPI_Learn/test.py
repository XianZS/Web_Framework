from types import ClassMethodDescriptorType
import jwt
from datetime import datetime, time, timedelta
from pwdlib import PasswordHash
import copy

pwd_obj = PasswordHash.recommended()


# $argon2id$v=19$m=65536,t=3,p=4$fOL6/2fsaoedGaxRRwac3Q$3qjZEtksoZkGckkxd9H1trxWr1iblru7s8rR7fN5EFo
def my_hash(data):
    return pwd_obj.hash(data)


res = my_hash("123")
print(res)


# 将用户输入的明文密码 【比较】 数据库存储的加密密码进行比较
def check(user_input, sql_download):
    judge = pwd_obj.verify(user_input, sql_download)
    print(judge)
    return judge


print(f"假设密码为456,{check('456', res)}")
print(f"假设密码为123,{check('123', res)}")

print("=" * 30)
now_time = datetime.now()

"""
    {
        username:字段信息
    }
"""

KEY = "23a6881d4ad6d43395cbd52967b50f718fd42aff32564f547eb19e0ccb9715be"
ALGORITHM = "HS256"


def create_token_user_jwt(data: dict):
    to_encode = copy.deepcopy(data)
    # 假设有效期是30分钟
    past_time = datetime.now() + timedelta(minutes=30)
    print(f"past_time:{past_time}")
    to_encode["past_time"] = str(past_time)[:-7]
    print("=" * 40)
    print("jwt编码之前的结果：", to_encode)
    to_encode_jwt = jwt.encode(to_encode, key=KEY, algorithm=ALGORITHM)
    return to_encode_jwt


cho = create_token_user_jwt({"username": "root"})
print("=" * 40)
print("jwt编码之后的结果:", cho)
print("=" * 40)
print("jwt解密之后的记过:", jwt.decode(cho, KEY, algorithms=[ALGORITHM]))
to_encode_jwt = jwt.decode(cho, KEY, algorithms=[ALGORITHM])
format_str = "%Y-%m-%d %H:%M:%S"
past_time = datetime.strptime(to_encode_jwt["past_time"], format_str)
print("过期时间是:", past_time)
if past_time > datetime.now():
    print("未过期")
else:
    print("过期")
