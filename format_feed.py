from bs4 import BeautifulSoup

def truncate_text(text, max_chars):
  return (text[:max_chars] + '...') if len(text) > max_chars else text

def format_feed_data(data, channel):
  if channel == 'tech_meme':
    return format_tech_meme_content(data)
  if channel == 'snook':
    return format_snook_content(data)
  if channel == 'slash_dot':
    return format_slash_dot_content(data)
  if channel == 'site_point':
    return format_site_point_content(data)
  if channel == 'javascript_weekly':
    return format_javascript_weekly_content(data)
  if channel == 'adactio':
    return format_adactio_content(data)
  if channel == 'functioning_form':
    return format_functioning_form_content(data)
  if channel == 'a_list_apart':
    return format_a_list_apart_content(data)
  if channel == 'david_walsh':
    return format_david_walsh_content(data)
  return data

def format_tech_meme_content(data):
  return BeautifulSoup(data).get_text()

def format_snook_content(data):
  paragraph_data = BeautifulSoup(data).find('p')
  if paragraph_data:
    return paragraph_data.get_text()
  return ''

def format_slash_dot_content(data):
  text = BeautifulSoup(data).get_text()
  return truncate_text(text, 500)

def format_site_point_content(data):
  text = BeautifulSoup(data).get_text()
  return truncate_text(text, 500)

def format_javascript_weekly_content(data):
  text = BeautifulSoup(data).get_text()
  return truncate_text(text, 500)

def format_adactio_content(data):
  return truncate_text(data, 600)

def format_functioning_form_content(data):
  text = BeautifulSoup(data).get_text()
  return truncate_text(text, 300)

def format_a_list_apart_content(data):
  return truncate_text(data, 400)

def format_david_walsh_content(data):
  text = BeautifulSoup(data).get_text()
  return truncate_text(text, 400)
