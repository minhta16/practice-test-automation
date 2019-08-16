from features.fixtures import chrome_browser, take_screenshot


def before_scenario(context, scenario):
    chrome_browser(context)


def after_step(context, step):
    if step.status == "failed":
        take_screenshot(
            context.browser,
            "[FAILED] " + context.scenario.name + "_" + step.name,
        )
