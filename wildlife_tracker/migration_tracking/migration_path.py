from typing import Optional
from ..habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, path_id: int, species: str, start_location: Habitat, destination: Habitat, 
                 duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass

    def get_migration_path_details(self, path_id) -> dict:
        pass