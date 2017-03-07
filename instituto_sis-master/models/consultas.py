from openerp.osv import fields, osv

class consultas(osv.osv):
	_name = 'sis.consultas'
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	   'partner_id': fields.many2one('res.partner', 'Estudiante', ondelete='restrict'),
	   'asignaturas': fields.many2one('sis.asignaturas', 'Asignaturas', ondelete='restrict'),	   
	}

consultas();
