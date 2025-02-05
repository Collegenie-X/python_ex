# update.py

from members import get_members

def update_member(old_email, updated_info):
    members = get_members()
    for member in members:
        if member['email'] == old_email:
            member.update(updated_info)
            print(f"{old_email}의 정보가 수정되었습니다.")
            return
    print(f"{old_email}에 해당하는 회원을 찾을 수 없습니다.")
