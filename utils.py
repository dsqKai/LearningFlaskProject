def items_to_dict(items, rules=None, only=None):
    return [i.to_dict(rules=rules, only=only) for i in items]
