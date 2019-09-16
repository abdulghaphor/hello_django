from django.db import models



# Create your models here.
class Car(models.Model):
	# owner = models.ForeignKey(User, on_delete=models.CASCADE)

	GEAR_CHOICES = [
		('AUTOMATIC', 'Automatic'),
		('MANUAL', 'Manual'),
	]
	CAR_CHOICES = [
		('ACURA', 'Acura'),
		('ALFAROMEO', 'Alfa Romeo'),
		('ASTONMARTIN', 'Aston Martin'),
		('AUDI', 'Audi'),
		('BENTLEY', 'Bentley'),
		('BMW', 'BMW'),
		('BUICK', 'Buick'),
		('CADILLAC', 'Cadillac'),
		('CHEVROLET', 'Chevrolet'),
		('CHRYSLER', 'Chrysler'),
		('DODGE', 'Dodge'),
		('FERRARI', 'Ferrari'),
		('FIAT', 'FIAT'),
		('FORD', 'Ford'),
		('GENESIS', 'Genesis'),
		('GMC', 'GMC'),
		('HONDA', 'Honda'),
		('HYUNDAI', 'Hyundai'),
		('INFINITI', 'INFINITI'),
		('JAGUAR', 'Jaguar'),
		('JEEP', 'Jeep'),
		('KIA', 'Kia'),
		('LAMBORGHINI', 'Lamborghini'),
		('LANDROVER', 'Land Rover'),
		('LEXUS', 'Lexus'),
		('LINCOLN', 'Lincoln'),
		('LOTUS', 'Lotus'),
		('MASERATI', 'Maserati'),
		('MAZDA', 'Mazda'),
		('MCLAREN', 'McLaren'),
		('MERCEDESBENZ', 'Mercedes-Benz'),
		('MINI', 'MINI'),
		('MITSUBISHI', 'Mitsubishi'),
		('NISSAN', 'Nissan'),
		('PORSCHE', 'Porsche'),
		('RAM', 'RAM'),
		('ROLLSROYCE', 'Rolls-Royce'),
		('SCION', 'Scion'),
		('SMART', 'smart'),
		('SUBARU', 'Subaru'),
		('TESLA', 'Tesla'),
		('TOYOTA', 'Toyota'),
		('VOLKSWAGEN', 'Volkswagen'),
		('VOLVO', 'Volvo'),
	]
	maker = models.CharField(max_length=255,choices=CAR_CHOICES)
	model = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	gear = models.CharField(max_length=255,choices=GEAR_CHOICES)
	year = models.PositiveIntegerField()
	milage = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=20, decimal_places=3)
	image = models.ImageField(null=True,blank=True)
	create_date = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.maker


# class Region(models.Model):
# 	name = models.CharField(max_length=255)

# class Size(models.Model):
# 	name = models.CharField(max_length=255)
