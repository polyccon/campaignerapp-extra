"""Various utils"""


def mask_email(email):
    """Returns masked email for example o***g@example.local

    :param email: email address
    :return: str Masked email
    """
    name, domain = email.split("@") if "@" in email else [email, ""]
    name_length = len(name)
    if name_length > 2:
        name = "{}{}{}".format(name[0], (name_length - 2) * "*", name[-1])
    else:
        name = "**"

    return "{}@{}".format(name, domain)


def snake_case_to_title_human(value):
    """Convert `snake_case` to `Human Readable Value`"""
    return value.replace("_", " ").title()
