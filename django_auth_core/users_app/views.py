from django.shortcuts import render
#
# import requests
# from django.contrib.auth.models import User
# from allauth.socialaccount.models import SocialToken, SocialAccount
#
#
# def get_github_profile(user):
#     # Получаем токен
#     token = SocialToken.objects.get(account__user=user, account__provider='github')
#
#     # Делаем запрос к API GitHub
#     response = requests.get(
#         'https://api.github.com/user',
#         headers={'Authorization': f'token {token.token}'}
#     )
#
#     if response.status_code == 200:
#         profile_data = response.json()
#         # Здесь вы можете добавить логику для создания или обновления пользователя
#         # Например, обновление информации о пользователе
#         user.username = profile_data['login']
#         user.email = profile_data['email']  # Убедитесь, что email доступен
#         user.save()
#
