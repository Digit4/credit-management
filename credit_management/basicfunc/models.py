from django.db import models


# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=264)
	email = models.CharField(max_length=264, primary_key=True)
	credit_points = models.PositiveIntegerField()
	link = models.CharField(max_length=100)

	def __str__(self):
		return "Object: " + self.email + ""
		
	def __len__(self):
		return Participant.objects.count()


# Transaction history table
class TransferHistory(models.Model):
	donor = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="donor")
	target = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="target")
	weight = models.IntegerField()

	def __str__(self):
		return str(self.target + " < " + str(self.donor) + str(self.weight) + ";")