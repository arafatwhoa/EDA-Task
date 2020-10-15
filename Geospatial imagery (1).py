#!/usr/bin/env python
# coding: utf-8
# Installing jupyter-gmaps with pip
Make sure that you have enabled ipywidgets widgets extensions:
$ jupyter nbextension enable –py widgetsnbextension
You can then install gmaps with:
$ pip install gmaps
Then tell Jupyter to load the extension with:
$ jupyter nbextension enable –py gmaps
#  list that offer open source(free to use) remote sensing satellites that offers the data - https://www.geoawesomeness.com/list-of-top-10-sources-of-free-remote-sensing-data/
# Create API key credentials on google maps console (creating a new project)# Generating API key and enableing  Maps Javascript API.
# In[ ]:


import gmaps
import gmaps.datasets


# In[9]:


gmaps.configure(api_key='AIzaSyDh-4GhzI0J7KzGjLdmZSQY8GKnEitoEC0')


# In[10]:


import gmaps
import gmaps.datasets
gmaps.configure(api_key='AIzaSyDh-4GhzI0J7KzGjLdmZSQY8GKnEitoEC0')
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()


# In[11]:


locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig


# In[13]:


fig = gmaps.figure(map_type = 'SATELLITE')
fig


# In[15]:


new_delhi_coordinates = (28.61, 77.20)
gmaps.figure(center=new_delhi_coordinates, zoom_level=12, map_type='HYBRID')


# In[16]:


new_delhi_coordinates = (28.61, 77.20)
gmaps.figure(center=new_delhi_coordinates, zoom_level=12, map_type='TERRAIN')


# In[ ]:





# In[ ]:




