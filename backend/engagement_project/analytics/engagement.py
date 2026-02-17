def calculate_engagement(user):
    score = (
        user.session_time * 0.5 +
        user.pages_visited * 2 +
        user.clicks * 0.1 -
        user.last_login_gap * 1.5
    )
    return max(score, 0)
