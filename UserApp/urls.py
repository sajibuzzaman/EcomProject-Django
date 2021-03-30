from django.urls import path
from UserApp.views import (user_logout, user_login, user_signup,
                            user_profile, user_update, user_password,
                            usercomment, comment_delete)

urlpatterns = [
    path('logout/',user_logout,name='user_logout' ),
    path('login/',user_login,name='user_login' ),
    path('register/',user_signup,name='user_signup' ),
    path('profile/',user_profile,name='user_profile' ),
    path('user_update/',user_update,name='user_update' ),
    path('password_update/',user_password,name='user_password' ),
    path('user_comment/',usercomment,name='usercomment' ),
    path('user_comment_delete/<int:id>/', comment_delete, name="comment_delete")
]