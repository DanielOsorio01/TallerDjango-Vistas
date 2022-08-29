from ..models import Measurement
from variables.logic import variables_logic as vl

#GET ALL
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

#GET
def get_measurement(ms_pk):
    measurement = Measurement.objects.get(pk=ms_pk)
    return measurement

#PUT/PATCH/UPDATE
def update_measurement(ms_pk, new_ms):
    measurement = get_measurement(ms_pk)
    measurement.variable= vl.get_variable(new_ms["variable"])
    measurement.value = new_ms["value"]
    measurement.unit = new_ms["unit"]
    measurement.place = new_ms["place"]
    measurement.save()
    return measurement

#CREATE
def create_measurement(ms):
    measurement = Measurement(  variable= vl.get_variable(ms["variable"]),
                                value = ms["value"],
                                unit = ms["unit"],
                                place = ms["place"])
    measurement.save()
    return measurement

#DELETE
def delete_measurement(ms_pk):
    measurement = get_measurement(ms_pk)
    measurement.delete()
    return measurement