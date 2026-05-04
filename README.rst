z_wizard_services
=================

Propósito
---------

``z_wizard_services`` agrega un asistente independiente para dar de alta
servicios como productos de tipo ``service`` en GNU Health.

Motivación
----------

El módulo toma como referencia el uso de productos dentro de
``z_001_copago_services``, donde los servicios se seleccionan como
``product.product`` y se utilizan para crear líneas de
``gnuhealth.health_service.line`` y facturación de copagos.

Funcionalidad incluida
----------------------

* Asistente ``gnuhealth.create_service.wizard``.
* Formulario simple para crear servicios facturables.
* Creación encadenada de ``product.template`` y ``product.product``.
* Marcado opcional de ``copago_individual_ticket``.

Dependencias
------------

* ``health``
* ``health_services``
* ``z_001_copago_services``

Campos y comportamiento relevante
---------------------------------

* El asistente pide nombre, precio de lista y estado activo.
* El template siempre se crea con ``type = 'service'``.
* El producto queda listo para usarse en dominios como
  ``('type', '=', 'service')``.
* Puede marcarse para generar ticket individual de copago.
