from fhir.resources.careteam import CareTeam, CareTeamParticipant
from fhir.resources.reference import Reference
from fhir.resources.period import Period
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
import datetime
import requests

def create_careteam(patient_id):
    careteam = CareTeam()

    # Nombre del equipo de atención
    careteam.name = "Equipo de atención cardiovascular"

    # Estado del equipo
    careteam.status = "active"

    # Referencia al paciente
    careteam.subject = Reference(reference=f"Patient/{patient_id}", display="Maria Victoria Nespola")

    # Período de actividad (comienza hoy)
    period = Period()
    period.start = datetime.date.today().isoformat()
    careteam.period = period

    # Participante del equipo: una cardióloga
    participant = CareTeamParticipant()
    participant.role = [
        CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/participant-role",
                code="practitioner",
                display="Cardióloga"
            )]
        )
    ]
    participant.member = Reference(display="Dra. Carla Gómez")
    careteam.participant = [participant]

    return careteam

# Crear el recurso usando el ID real del paciente cargado
careteam = create_careteam("47886789")

# Imprimir JSON
print(careteam.json(indent=2))

# Subir al servidor HAPI
url = "http://hapi.fhir.org/baseR4/CareTeam"
headers = {"Content-Type": "application/fhir+json"}
response = requests.post(url, data=careteam.json(), headers=headers)

# Mostrar resultado
print("Status:", response.status_code)
print("Respuesta del servidor:", response.text)
