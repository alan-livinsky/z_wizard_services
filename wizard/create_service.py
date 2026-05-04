from trytond.model import ModelView, fields
from trytond.pool import Pool
from trytond.wizard import Button, StateAction, StateView, Wizard


class CreateServiceStart(ModelView):
    "Inicio de creación de servicio"
    __name__ = "gnuhealth.create_service.start"

    name = fields.Char('Nombre', required=True, help='Nombre del servicio')
    list_price = fields.Numeric(
        'Precio de lista', required=True, help='Precio de venta del servicio')
    active = fields.Boolean('Activo', help='Indica si el servicio está activo')
    is_copago_service = fields.Boolean(
        'Servicio de copago',
        help='Marca el servicio para que aparezca en el selector de copagos')
    copago_individual_ticket = fields.Boolean(
        'Generar ticket individual',
        help='Si está marcado, el servicio se factura en un ticket separado')

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_list_price():
        return 0


class CreateServiceWizard(Wizard):
    "Asistente de creación de servicio"
    __name__ = "gnuhealth.create_service.wizard"

    start = StateView(
        'gnuhealth.create_service.start',
        'z_wizard_services.gnuhealth_create_service_start_view', [
            Button('Crear', 'create_', 'tryton-ok', default=True),
            Button('Cancelar', 'end', 'tryton-cancel'),
        ])
    create_ = StateAction('z_wizard_services.action_view_service_created')

    def do_create_(self, action):
        pool = Pool()
        Template = pool.get('product.template')
        Product = pool.get('product.product')
        UOM = pool.get('product.uom')

        try:
            uom, = UOM.search([('name', '=', 'Unit')], limit=1)
        except ValueError:
            uom, = UOM.search([('name', '=', 'Unidad')], limit=1)

        template = Template()
        template.name = self.start.name
        template.default_uom = uom.id
        template.list_price = self.start.list_price
        template.type = 'service'
        template.active = self.start.active
        template.save()

        product = Product()
        product.template = template.id
        product.active = self.start.active
        product.is_medicament = False
        product.is_copago_service = self.start.is_copago_service
        product.copago_individual_ticket = self.start.copago_individual_ticket
        product.save()

        data = {'res_id': [product.id]}
        action['views'].reverse()
        return action, data
