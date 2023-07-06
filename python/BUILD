py_library(
    name = "console_prompt_templates",
    srcs = [
        "console/prompt_templates/rfp_copilot_template.py",
    ]
)

py_test(
    name = "rfp_copilot_template_testcase",
    srcs = ["tests/rfp_copilot_template_testcase.py"],
    deps = ["//python:console_prompt_templates"]
)
