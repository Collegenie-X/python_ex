# register.py

from members import get_members

def register_member(member_info):
    name = member_info.get('name')
    email = member_info.get('email')
    phone = member_info.get('phone')

    members = get_members()
    members.append({'name': name, 'email': email, 'phone': phone})
    print(f"{name}님의 회원 가입이 완료되었습니다.")
