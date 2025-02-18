# view.py

from members import get_members

def view_members():
    members = get_members()
    if not members:
        print("회원 목록이 비어 있습니다.")
    else:
        print("*** 회원 목록 ***")
        for member in members:
            print(f"이름: {member['name']}, \
                    이메일: {member['email']}, \
                    전화번호: {member['phone']}")
