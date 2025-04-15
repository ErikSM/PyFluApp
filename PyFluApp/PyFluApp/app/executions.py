from app.web_actions import access_website_on_browser
from data.content_but_other import other_buts_dict


def processing_but_other(selected):
    action = None
    string = other_buts_dict[selected]

    if selected == 'Acesse o Site Oficial':
        more_action = True
        action = lambda: access_website_on_browser('https://pythonfluente.com/')
    else:
        more_action = False

    return string, more_action, action
