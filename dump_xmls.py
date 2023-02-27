import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-posts-page-1.xml")
pageSource = driver.page_source
fileToWrite = open("page-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-posts-post-1.xml")
pageSource = driver.page_source
fileToWrite = open("post-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-posts-post-2.xml")
pageSource = driver.page_source
fileToWrite = open("post-2.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-posts-post-3.xml")
pageSource = driver.page_source
fileToWrite = open("post-3.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-posts-draft_policy-1.xml")
pageSource = driver.page_source
fileToWrite = open("draft_policy-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-category-1.xml")
pageSource = driver.page_source
fileToWrite = open("taxonomies-category-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-post_tag-1.xml")
pageSource = driver.page_source
fileToWrite = open("taxonomies-post_tag-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-post_format-1.xml")
pageSource = driver.page_source
fileToWrite = open("taxonomies-post_format-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-media_notification_types-1.xml")
pageSource = driver.page_source
fileToWrite = open("taxonomies-media_notification_types-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()

driver = uc.Chrome()
driver.get("https://home.chicagopolice.org/wp-sitemap-users-1.xml")
pageSource = driver.page_source
fileToWrite = open("users-1.xml", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.quit()
