from django import urls

# Test verify that the site renders as expected
def test_quantum_site(client):
    url = urls.reverse('quantummanagementapp:landing_page')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Quantum Management' in resp.content
