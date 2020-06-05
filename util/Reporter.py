import allure


def attachtext(text):
    allure.attach(text, name="Text Attachment", attachment_type=allure.attachment_type.TEXT)


def attachscreenshot(driver, text):
    allure.attach(driver.get_screenshot_as_png(), name="PNG Attachment", attachment_type=allure.attachment_type.PNG)


def passed(driver, text):
    attachtext(text)
    attachscreenshot(driver, text)
    assert True, text


def failed(driver, text):
    attachtext(text)
    attachscreenshot(driver, text)
    assert False, text


def info(text):
    attachtext(text)



