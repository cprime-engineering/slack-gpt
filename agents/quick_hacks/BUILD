load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "cprime_clients",
    srcs = [
        "cprime_clients.py",
    ],
    deps = [
        requirement("langchain"),
        requirement("openai"),
    ],
)

py_binary(
    name = "cprime_openai",
    srcs = [
        "cprime_openai.py",
    ],
    deps = [
        requirement("openai"),
    ],
)

py_binary(
    name = "llm_chain",
    srcs = [
        "llm_chain.py",
    ],
    deps = [
        requirement("langchain"),
        requirement("openai"),
    ],
)

py_binary(
    name = "tdd_langchain",
    srcs = [
        "tdd_langchain.py",
    ],
    deps = [
        requirement("langchain"),
        requirement("openai"),
    ],
)
