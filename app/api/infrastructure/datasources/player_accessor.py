from app.api.database import db
from app.api.domain.models import PlayerRecord
from app.api.domain.repositories import PlayerRepository
from app.api.infrastructure.datasources.entities import PlayerEntity, PlayerGradeEntity


class PlayerAccessor(PlayerRepository):
    def save_from_records(self, player_records: list[PlayerRecord]):
        player_entities = PlayerEntity.query.all()
        grade_entities = PlayerGradeEntity.query.all()
        for player_record in player_records:
            grade_record = player_record.grade
            player_entity = next(
                filter(
                    lambda entity: entity.number == player_record.number,
                    player_entities,
                ),
                None,
            )
            if player_entity is None:
                player_entity = PlayerEntity()
            player_entity.name = player_record.name
            player_entity.number = player_record.number
            player_entity.birthday = player_record.birthday
            player_entity.birthplace = player_record.birthplace
            player_entity.grade = next(
                filter(
                    lambda entity: entity.number == grade_record.number
                    and entity.category == grade_record.category.value,
                    grade_entities,
                )
            )
            player_entity.title = player_record.title
