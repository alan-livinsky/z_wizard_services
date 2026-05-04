from trytond.pool import Pool

from .wizard import create_service


def register():
    Pool.register(
        create_service.CreateServiceStart,
        module='z_wizard_services', type_='model')
    Pool.register(
        create_service.CreateServiceWizard,
        module='z_wizard_services', type_='wizard')
