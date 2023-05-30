import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor should be vaccinated")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear the mask")
        else:
            return f"Welcome to {self.name}"