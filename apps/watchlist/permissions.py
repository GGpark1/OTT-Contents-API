from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    # 개별 개체에 접근하기 전에 view에 대한 권한을 확인함
    # view 내부에서 개별 개체에 대한 접근 권한은 has_object_permission을 사용함
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_admin)
        # return A or B
        ## A와 B 둘 다 참 -> A 출력
            ## admin이 읽기 권한만 요청한 것이므로 GET만 허용
        ## A와 B 둘 중 하나가 참 -> 참인 값 출력
            ## GET이 참 -> 읽기만 허용
            ## admin이 참 -> admin 권한 허용
        ## A, B 둘 다 거짓 -> B 출력
            ## view에 false를 반환 -> 인증 받은 사용자가 아님을 전달 
        return request.method == "GET" or admin_permission