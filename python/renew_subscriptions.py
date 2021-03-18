'''

    Below is some test data representing an imaginary subscription service.
    Once a day, the subscriptions are passed to the get_renewed_subscriptions function.
    If the 'expiresAt' date is in the past AND the subscription has been paid, the
    subscription is renewed and included in the list returned by get_renewed_description.

    Task:
    - Compare the two implementations of get_renewed_subscriptions. Which one seems better, and why?
    - For the test data below, both implementations return the same value. But does either
      implementation potentially have an unintended side effect?

'''
from datetime import datetime, timedelta

unrenewed_subscriptions = [
    {
        'id': 1,
        'paid': False,
        'expiresAt': datetime.now() - timedelta(days=1)
    },
    {
        'id': 2,
        'paid': True,
        'expiresAt': datetime.now() + timedelta(days=1)
    },
    {
        'id': 3,
        'paid': True,
        'expiresAt': datetime.now() - timedelta(days=1)
    }
]


def get_renewed_subscriptions_1(subscriptions):
    renewed_subscriptions = []
    for subscription in subscriptions:
        if subscription.get('paid') == True:
            if subscription.get('expiresAt') < datetime.now():
                subscription['expiresAt'] = subscription.get(
                    'expiresAt') + timedelta(days=30)
                subscription['renewedAt'] = datetime.now()
                renewed_subscriptions.append(subscription)

    return renewed_subscriptions


def get_renewed_subscriptions_2(subscriptions):
    now = datetime.now()
    return [
        {
            **s,
            'expiresAt': s.get('expiresAt') + timedelta(days=30),
            'renewedAt': now
        }
        for s in filter(
            lambda s: s.get('paid') and s.get('expiresAt') < now,
            subscriptions
        )
    ]
