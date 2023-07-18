load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "slackbot.py",
    ],
    data = [
        "pre_prompts/date",
        "pre_prompts/footer",
        "pre_prompts/persona",
        "pre_prompts/personalized",
        "pre_prompts/version",
    ],
    deps = [
        "//domain:domain",
        requirement("slack-bolt"),
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
    ],
)
