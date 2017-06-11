from django.contrib.auth.models import User

def save_profile(backend, user, response, *args, **kwargs):
    # UserProfile.objects.create(
    #     user=user, website=response['user']['website'],
    #     instagram_username=response['user']['username'])
    print "response",response
    return response