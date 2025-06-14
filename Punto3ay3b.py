from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier
from fhir.resources.reference import Reference
import requests

# Crear el recurso FHIR de paciente
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_number=None):
    patient = Patient()
    
    # Agregar el nombre del paciente
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    # Agregar la fecha de nacimiento
    if birth_date:
        patient.birthDate = birth_date

    # Agregar el género
    if gender:
        patient.gender = gender

    # Agregar información de contacto
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]
    
    # Agregar DNI como identifier
    if document_number:
        id = Identifier()
        id.value = document_number
        id.use = "official"
        id.system = "https://www.argentina.gob.ar/interior/renaper"
        id.assigner = Reference(display="Renaper")
        id.type = {
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                "code": "NI",
                "display": "National unique individual identifier"
            }]
        }
        patient.identifier = [id]

    return patient

# Función para subir un recurso FHIR al servidor HAPI
def upload_patient_to_server(patient):
    url = "http://hapi.fhir.org/baseR4/Patient"
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(url, data=patient.json(), headers=headers)

    if response.status_code == 201:
        print("Paciente subido correctamente.")
    else:
        print("Error al subir el paciente:", response.status_code)
        print(response.text)

# Función para buscar un paciente por documento
def search_patient_by_document(document_number):
    base_url = "http://hapi.fhir.org/baseR4/Patient"
    system = "https://www.argentina.gob.ar/interior/renaper"
    params = {
        "identifier": f"{system}|{document_number}"
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        bundle = response.json()
        entries = bundle.get("entry", [])
        if entries:
            print(f"Se encontraron {len(entries)} paciente(s):")
            for entry in entries:
                patient = entry["resource"]
                patient_id = patient["id"]
                name = patient.get("name", [{}])[0]
                full_name = " ".join(name.get("given", []) + [name.get("family", "")])
                print(f"- ID: {patient_id} | Nombre: {full_name}")
            return patient_id  # Devolver el ID para usarlo en el punto c
        else:
            print(" No se encontró ningún paciente con ese documento.")
    else:
        print(" Error en la búsqueda:", response.status_code)

# ----------- Ejecución -----------

# Crear el paciente
paciente = create_patient_resource(
    "Nespola", "Maria Victoria", "2002-10-04", "female", "1150640223", "44452287"
)

# Subir al servidor
upload_patient_to_server(paciente)

# Buscar al paciente por DNI
search_patient_by_document("44452287")
