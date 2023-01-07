from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):

    # 개별 개체에 접근하기 전에 view에 대한 권한을 확인함
    # view 내부에서 개별 개체에 대한 접근 권한은 has_object_permission을 사용함
    def has_permission(self, request, view):
        # admin_permission = bool(request.user and request.user.is_staff)
        # # return A or B
        # # A와 B 둘 다 참 -> A 출력
        # # admin이 읽기 권한만 요청한 것이므로 GET만 허용
        # # A와 B 둘 중 하나가 참 -> 참인 값 출력
        # # GET이 참 -> 읽기만 허용
        # # admin이 참 -> admin 권한 허용
        # # A, B 둘 다 거짓 -> B 출력
        # # view에 false를 반환 -> 인증 받은 사용자가 아님을 전달
        # return request.method == "GET" or admin_permission

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class IsReviewUserOrReadOnly(permissions.BasePermission):

    # object 단위의 데이터에 접근 가능 여부를 확인
    def has_object_permission(self, request, view, obj):

        # 요청이 안전한지 확인(SAFE_METHODS = 'GET', 'OPTIONS', 'HEAD')
        if request.method in permissions.SAFE_METHODS:
            # 안전한 요청이 들어왔다면 사용자 신원을 확인하지 않고 True를 반환함
            return True
        else:
            # DB 접근이 필요한 요청이 들어왔다면 obj의 작성자(obj.review_user)와 요청자(request.user)가 같은지 확인
            return obj.review_user == request.user or request.user.is_staff
