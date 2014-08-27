import copy
import json

class JSONWriter:
  def __init__(self, name):
    self._file = open(name, 'w')

  def page(self, page, content):
    if page != None and page != "":
      entry = dict()
      entry['url'] = page
      entry['topic'] = content['topic'] if 'topic' in content else None
      entry['title'] = content['d:Title'] if 'd:Title' in content else None
      entry['description'] = content['d:Description'] if 'd:Description' in content else None
      entry['priority'] = int(content['priority']) if 'priority' in content else None

      self._file.write(json.dumps(entry) + "\n")
    else:
      print "Skipping page %s, page attribute is missing" % page

  def finish(self):
    self._file.close()