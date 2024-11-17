from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

btn_guest_log_in = driver.find_element(By.XPATH, '//button[contains(@class,"header-link -guest")]')
btn_sign_in = driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-outline-white header_signin")]')
btn_home = driver.find_element(By.XPATH, "//a[contains(text(), 'Home')]")
btn_logo = driver.find_element(By.XPATH, '//a[@class="header_logo"]')
btn_about = driver.find_element(By.XPATH, "//button[contains(text(), 'About')]")
btn_contacts = driver.find_element(By.XPATH, "//button[contains(text(), 'Contacts')]")
title_display = driver.find_element(By.XPATH, "//h1[contains(text(), 'Do more!')]")
frame_element = driver.find_element(By.XPATH, "//iframe")

driver.switch_to.frame(frame_element)

link_yt_title_logo = driver.find_element(By.XPATH, '//a[contains(@class, "ytp-title-channel-l")]')
link_yt_title_chan_name = driver.find_element(By.XPATH, '//a[contains(@class, "ytp-title-channel-n")]')
link_yt_title_link = driver.find_element(By.XPATH, '//a[contains(@class, "ytp-title-l")]')
link_yt_watch_later_icon = driver.find_element(By.XPATH, '//div[contains(@class, "ytp-watch-later-icon")]')
link_yt_watch_later_title = driver.find_element(By.XPATH, '//div[contains(@class, "ytp-watch-later-title")]')
link_yt_share_icon = driver.find_element(By.XPATH, '//div[contains(@class, "ytp-share-icon")]')
link_yt_share_title = driver.find_element(By.XPATH, '//div[contains(@class, "ytp-share-title")]')
btn_start_yt = driver.find_element(By.XPATH, '//button[contains(@class, "ytp-large")]')
link_yt_watermark = driver.find_element(By.XPATH, '//a[contains(@href, "youtube") and contains(@class, "ytp-watermark")]')

driver.switch_to.default_content()

image_display = driver.find_element(By.XPATH, '//div[@id="aboutSection"]')
title2_display = driver.find_element(By.XPATH, "//h2[contains(text(), 'Contacts')]")
link_social_fb = driver.find_element(By.XPATH, '//a[contains(@href, "facebook")]')
link_social_tm = driver.find_element(By.XPATH, '//a[contains(@href, "t.me")]')
link_social_yt = driver.find_element(By.XPATH, '//a[contains(@href, "youtube") and contains(@class, "socials_link")]')
link_social_inst = driver.find_element(By.XPATH, '//a[contains(@href, "instagram")]')
link_social_in = driver.find_element(By.XPATH, '//a[contains(@href, "linkedin")]')
link_to_site = driver.find_element(By.XPATH, '//a[contains(@href, "//ithillel")]')
link_to_email = driver.find_element(By.XPATH, '//a[contains(@href, "@ithillel")]')

header_logo = driver.find_element(By.CSS_SELECTOR, "a.header_logo")
home_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.header-link")
about_btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.header-link[appscrollto="aboutSection"]')
contacts_btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.header-link[appscrollto="contactsSection"]')
guest_log_in_btn = driver.find_element(By.CSS_SELECTOR, 'button.header-link.-guest')
sign_in_btn = driver.find_element(By.CSS_SELECTOR, 'button.header_signin')
title_display_css = driver.find_element(By.CSS_SELECTOR, 'h1.hero-descriptor_title')
sign_up_btn_css = driver.find_element(By.CSS_SELECTOR, '.btn-primary')

frame_element = driver.find_element(By.CSS_SELECTOR, "iframe")

driver.switch_to.frame(frame_element)
yt_css = driver.find_element(By.CSS_SELECTOR, 'div.ytp-cued-thumbnail-overlay')
yt_channel_logo_css = driver.find_element(By.CSS_SELECTOR, 'a.ytp-title-channel-logo')
yt_title_link_css = driver.find_element(By.CSS_SELECTOR, 'a.ytp-title-link')
yt_watch_later_icon_css = driver.find_element(By.CSS_SELECTOR, 'div.ytp-watch-later-icon')
yt_watch_later_title_css = driver.find_element(By.CSS_SELECTOR, 'div.ytp-watch-later-title')
yt_share_icon_css = driver.find_element(By.CSS_SELECTOR, 'div.ytp-share-icon')
yt_share_title_css = driver.find_element(By.CSS_SELECTOR, 'div.ytp-share-title')
btn_start_yt_css = driver.find_element(By.CSS_SELECTOR, 'button.ytp-large-play-button')
link_yt_watermark_css = driver.find_element(By.CSS_SELECTOR, 'a.ytp-watermark')

driver.switch_to.default_content()

image_display_css = driver.find_element(By.CSS_SELECTOR, 'div.section.about')
title2_display_css = driver.find_element(By.CSS_SELECTOR, "#contactsSection h2")
link_social_fb_css = driver.find_element(By.CSS_SELECTOR, 'a.socials_link[href*="facebook"]')
link_social_tm_css = driver.find_element(By.CSS_SELECTOR, 'a.socials_link[href*="t.me"]')
link_social_yt_css = driver.find_element(By.CSS_SELECTOR, 'a.socials_link[href*="youtube"]')
link_social_inst_css = driver.find_element(By.CSS_SELECTOR, 'a.socials_link[href*="instagram"]')
link_social_in_css = driver.find_element(By.CSS_SELECTOR, 'a.socials_link[href*="linkedin"]')
link_link_to_site_css = driver.find_element(By.CSS_SELECTOR, 'a.contacts_link[href*="ithillel"]')
link_link_to_email_css = driver.find_element(By.CSS_SELECTOR, 'a.contacts_link[href*="mailto"]')

