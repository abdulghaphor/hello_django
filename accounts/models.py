from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError("Email address required.")
		if not password:
			raise ValueError("Password required.")			
		user_obj = self.model(
			email = self.normalize_email(email),
			)
		print(password)
		user_obj.set_password(password)
		user_obj.save(using=self._db)
		return user_obj
	
	def create_staffuser(self, email, password):
		user_obj = self.model(
			email = self.normalize_email(email),
			password = password,
			staff = True,
			)
		user_obj.save(using=self._db)
		return user_obj
	def create_superuser(self, email, password):
		user_obj = self.model(
			email = self.normalize_email(email),
			password = password,
			staff = True,
			admin = True,
			)
		user_obj.save(using=self._db)
		return user_obj


class User(AbstractBaseUser):
	email = models.EmailField(max_length=255,unique=True)
	active = models.BooleanField(default=True) # can login
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	first_name = models.CharField(max_length=255,null=True,blank=True)
	last_name = models.CharField(max_length=255,null=True,blank=True)	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return "%s %s" % (self.first_name, self.last_name)

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		# "Is the user active?"
		return self.active
	
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin