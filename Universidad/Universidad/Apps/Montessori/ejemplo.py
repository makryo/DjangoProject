from django.db import models
from comun.models import Persona
from django.core.exceptions import ValidationError

class Cliente(Persona):
	nit = models.Charfield('NIT', max_length=10)
	Correo = models.EmailField('email', null=True, blank=True)
	activo = models.BooleanField(default=True)

	def Clean(self):
		super(Cliente, self).clean()

		if (self.nombre == 'Vinicio Arturo' and self.apellido == 'Arango Giron'):
			raise ValidationError('usted no es permitido')

	def save(self, **kwargs):
		if self.activo:
		self.nombre = self.nombre.upper()
		self.apellido = self.apellido.upper()

		else :
		self.nombre = self.nombre.lower()
		self.apellido = self.apellido.lower()
		super(Cliente, self).save()

	class Meta():
        abstract = True
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes' 
        unique_togrther = ['nombre','apellido']

