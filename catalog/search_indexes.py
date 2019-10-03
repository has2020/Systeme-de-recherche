from haystack import indexes
from haystack.inputs import Raw
from haystack.inputs import AutoQuery
from catalog.models import Document
from haystack.query import SearchQuerySet

 
class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    def get_model(self):
        return Document
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
