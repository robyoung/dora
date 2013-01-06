import pymongo

DATABASE_NAME = "dora"

class Model(object):
  def __init__(self, collection, id_field=None):
    self._collection = self.create_collection(collection)
    self._id_field = id_field

  def create_collection(self, name):
    return pymongo.Connection()[DATABASE_NAME][name]

  def save(self, document):
    if self._id_field:
      document["_id"] = document[self._id_field]
    self._collection.save(document)

  def __getattr__(self, name):
    return getattr(self._collection, name)


artefacts = Model("artefacts", id_field="id")