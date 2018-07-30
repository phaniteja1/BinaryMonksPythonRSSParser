from bs4 import BeautifulSoup

def format_feed_data(data, channel):
  if channel == 'tech_meme':
    return format_tech_meme_content(data)
  if channel == 'snook':
    return format_snook_content(data)
  return data

def format_tech_meme_content(data):
  return BeautifulSoup(data, 'html5lib').get_text()

def format_snook_content(data):
  paragraph_data = BeautifulSoup(data, 'html5lib').find('p')
  if paragraph_data:
    return paragraph_data.get_text()
  return ''