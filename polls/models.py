from django.db import models
import pprint

# -------------------------------------------------------------------- #

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		s = []
		
		d = self.__dict__
		for k in tuple(d.keys()):
			if k.startswith('_'):
				d.pop(k)
		
		s += [ '%s:' % self.__class__.__name__ ]
		s += [ pprint.pformat(d, indent=2, compact=False) ]
		return '\n'.join(s)
	
# -------------------------------------------------------------------- #

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		s = []
		
		d = self.__dict__
		for k in tuple(d.keys()):
			if k.startswith('_'):
				d.pop(k)
		
		s += [ '%s:' % self.__class__.__name__ ]
		s += [ pprint.pformat(d, indent=2, compact=False) ]
		return '\n'.join(s)
	
# -------------------------------------------------------------------- #
