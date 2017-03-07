from openerp.osv import fields, osv

class asignaturas(osv.osv):
	_name = 'sis.asignaturas'
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	}

asignaturas();
