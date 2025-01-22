from django.db import models

# Create your models here.

class Admin(models.Model):
	admin_name = models.CharField(max_length=100)

class Mobile(models.Model):
	m_id = models.AutoField(primary_key="true")
	m_name = models.CharField(max_length=50)
	m_price = models.CharField(max_length=50)
	m_photo_link = models.CharField(max_length=50)
	m_content_link = models.CharField(max_length=50)
	m_feedback_link = models.CharField(max_length=50)

class Laptop(models.Model):
	l_id = models.AutoField(primary_key="true")
	l_name = models.CharField(max_length=50)
	l_price = models.CharField(max_length=50)
	l_photo_link = models.CharField(max_length=50)
	l_content_link = models.CharField(max_length=50)
	l_feedback_link = models.CharField(max_length=50)

class Cameras(models.Model):
	c_id = models.AutoField(primary_key="true")
	c_name = models.CharField(max_length=50)
	c_price = models.CharField(max_length=50)
	c_photo_link = models.CharField(max_length=50)
	c_content_link = models.CharField(max_length=50)
	c_feedback_link = models.CharField(max_length=50)

class Smart_Watches(models.Model):
	s_id = models.AutoField(primary_key="true")
	s_name = models.CharField(max_length=50)
	s_price = models.CharField(max_length=50)
	s_photo_link = models.CharField(max_length=50)
	s_content_link = models.CharField(max_length=50)
	s_feedback_link = models.CharField(max_length=50)

class Electronic_Accessory(models.Model):
	e_id = models.AutoField(primary_key="true")
	e_name = models.CharField(max_length=50)
	e_price = models.CharField(max_length=50)
	e_photo_link = models.CharField(max_length=50)
	e_content_link = models.CharField(max_length=50)
	e_feedback_link = models.CharField(max_length=50)

class Computer_Hardware(models.Model):
	h_id = models.AutoField(primary_key="true")
	h_name = models.CharField(max_length=50)
	h_price = models.CharField(max_length=50)
	h_photo_link = models.CharField(max_length=50)
	h_content_link = models.CharField(max_length=50)
	h_feedback_link = models.CharField(max_length=50)

class Users(models.Model):
	u_id = models.AutoField(primary_key="true")
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	uname = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mnumber = models.CharField(max_length=50)