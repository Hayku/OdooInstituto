from openerp.osv import fields, osv

class instituto(osv.osv):
	_name = 'sis.instituto'
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	   'country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
	}

instituto();
