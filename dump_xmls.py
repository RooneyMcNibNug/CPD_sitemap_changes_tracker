import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

a = open("page-1.xml", "w") # w is for truncating files (we want diffs between commits)
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-posts-page-1.xml").text), file=a)
a.close()

b = open("post-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-posts-post-1.xml").text), file=b)
b.close()

c = open("post-2.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-posts-post-2.xml").text), file=c)
c.close()

d = open("post-3.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-posts-post-3.xml").text), file=d)
d.close()

e = open("draft_policy-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-posts-draft_policy-1.xml").text), file=e)
e.close()

f = open("taxonomies-category-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-category-1.xml").text), file=f)
f.close()

g = open("taxonomies-post_tag-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-post_tag-1.xml").text), file=g)
g.close()

h = open("taxonomies-post_format-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-post_format-1.xml").text), file=h)
h.close()

i = open("taxonomies-media_notification_types-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-taxonomies-media_notification_types-1.xml").text), file=i)
i.close()

j = open("users-1.xml", "w")
print((scraper.get("https://home.chicagopolice.org/wp-sitemap-users-1.xml").text), file=j)
j.close()
