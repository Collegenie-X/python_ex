# delete.py

from members import get_members

def delete_member(email):
    members = get_members()
    for member in members:
        if member['email'] == email:
            members.remove(member)
            print(f"{email}님의 회원 정보가 삭제되었습니다.")
            return
    print(f"{email}에 해당하는 회원을 찾을 수 없습니다.")
