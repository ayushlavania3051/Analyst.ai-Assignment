#!/usr/bin/env python
# coding: utf-8

# In[8]:


from autoscraper import AutoScraper


# In[9]:


amazon_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"


# In[15]:


wanted_list={"EUME Alexis 31 Ltrs Laptop Backpack for Office & Travel Use for Men & Women | Water Resistance Bag | Fit Up to 15.6-inch Laptop", "₹2199", "131"}


# In[16]:


scraper = AutoScraper()
result=scraper.build(amazon_url, wanted_list)
print(result)


# In[21]:


scraper.get_result_similar(amazon_url,grouped=True)


# In[23]:


scraper.set_rule_aliases({'rule_1t1v':'Title','rule_xg0b':'Price'})
scraper.keep_rules(['rule_1t1v','rule_xg0b'])
scraper.save('amazon-search')


# In[24]:


results=scraper.get_result_similar('https://www.amazon.in/s?k=mi+p
results['Price','Title']


# In[ ]:




