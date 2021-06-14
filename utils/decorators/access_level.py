from django.shortcuts import render
from functools import wraps

# ------------------------------------------------------------------------------------------------------------------------------------

def user_passes_test(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return render(request, '403.html')
        return _wrapped_view
    return decorator


def is_superuser(function = None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_governor(function = None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_governor,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_deputy(function = None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_deputy,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_governor_or_deputy(function = None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_governor or u.is_deputy,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator