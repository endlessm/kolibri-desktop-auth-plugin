option_spec = {
    "DesktopAuth": {
        "FORCE_SUPERUSER": {
            "type": "boolean",
            "default": True,  # FIXME default false
            "description": (
                "Whether to force superuser permissions ",
                "even when the system user is not an administrator.",
            ),
        },
    },
}
