def profile_context(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        return {'profile': profile}
    return {'profile': None}