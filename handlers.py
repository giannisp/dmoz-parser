import copy
import json

class JSONWriter:
  def __init__(self, name):
    self._file = open(name, 'w')

  def page(self, page, content):
    if page != None and page != "":
      newcontent = copy.copy(content)
      newcontent["url"] = page

      self._file.write(json.dumps(newcontent) + "\n")
    else:
      print "Skipping page %s, page attribute is missing" % page

  def finish(self):
    self._file.close()