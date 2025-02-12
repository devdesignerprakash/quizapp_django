# from django.db import models         
# from django.contrib.auth.models  import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Create your models here.
# class CustomUserManager(BaseUserManager):
#     """Manager for CustomUser model."""

#     def create_user(self, email, password=None, **extra_fields):
#         """Create and return a regular user with an email and password."""
#         if not email:
#             raise ValueError("The Email field must be set")

#         email = self.normalize_email(email)
#         extra_fields.setdefault('is_active', True)  # Default to active user
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """Create and return a superuser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that uses email instead of username."""
    
#     email = models.EmailField(unique=True, verbose_name="Email Address")
#     first_name = models.CharField(max_length=30, verbose_name="First Name")
#     last_name = models.CharField(max_length=30, verbose_name="Last Name")
#     is_admin=models.BooleanField(default=False,verbose_name="Admin")
#     is_active = models.BooleanField(default=True, verbose_name="Active")
#     is_staff = models.BooleanField(default=False, verbose_name="Staff Status")  # Admin user but not superuser
#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'  # Email is used as the unique identifier
#     REQUIRED_FIELDS = ['first_name', 'last_name']  # Required fields when creating a superuser

#     def __str__(self):
#         return self.email