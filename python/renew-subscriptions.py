from datetime import datetime, timedelta


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
    return [
        {
            **s,
            'expiresAt': s.get('expiresAt') + timedelta(days=30),
            'renewedAt': datetime.now()
        }
        for s in filter(
            lambda s: s.get('paid') and s.get('expiresAt') < datetime.now(),
            subscriptions
        )
    ]


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
