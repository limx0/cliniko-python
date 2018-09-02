
def test_get_invoices(client):
    resp = client.get_invoice()
    assert resp


def test_get_appointment_type(client):
    resp = client.get_appointment_types()
    assert resp
