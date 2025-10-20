JAZZMIN_SETTINGS = {
    "site_title": "MedWay Admin",
    "site_header": "MedWay Admin",
    "site_brand": "MedWay Admin",
    "welcome_sign": "Bem-vindo ao MedWay Admin",
    "copyright": "MedWay",
    "user_avatar": None,

    "site_logo": "images/logo-medway.png",
    "site_logo_small": "images/logo-medway-small.png", 

    "topmenu_links": [
        {"name": "Home", "url": "/admin", "new_window": False},
        {"app": "medway"},
    ],

    "usermenu_links": [
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": False,
    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": [
        "student", 
        "exam", 
        "question", 
        "answers"
    ],

    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "icons": {
        "student": "fas fa-users-cog",
        "student.Student": "fas fa-user",
        "student.Group": "fas fa-users",
        "student.permission": "fas fa-user-lock",
        "exam": "fas fa-file-alt",
        "question": "fas fa-question-circle",
        "answers": "fas fa-pencil-alt",
        "answers.ExamResponse": "fas fa-clipboard-list",
        "answers.QuestionResponse": "fas fa-check-square",
        "django_celery_results": "fas fa-tasks",
        "django_periodic_tasks": "fas fa-tasks",
        "django_celery_results.groupresult": "fas fa-tasks",
        "django_celery_results.taskresult": "fas fa-tasks",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },
}
