load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "slackbot.py",
    ],
    deps = [
        requirement("flask"),
        requirement("slack-sdk"),
        requirement("slack-bolt"),
        requirement("python-dotenv"),
    ],
)
