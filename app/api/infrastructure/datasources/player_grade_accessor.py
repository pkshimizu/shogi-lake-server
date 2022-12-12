from app.api.database import db
from app.api.domain.models import PlayerGradeRecord
from app.api.domain.repositories import PlayerGradeRepository
from app.api.infrastructure.datasources.entities import PlayerGradeEntity


class PlayerGradeAccessor(PlayerGradeRepository):
    def save_from_records(self, player_grade_records: list[PlayerGradeRecord]):
        player_grade_entities = PlayerGradeEntity.query.all()
        player_grades = []
        for player_grade_record in player_grade_records:
            player_grade_entity = next(
                filter(
                    lambda entity: entity.name == player_grade_record.name,
                    player_grade_entities,
                ),
                None,
            )
            if player_grade_entity is None:
                player_grade_entity = PlayerGradeEntity()
            player_grade_entity.name = player_grade_record.name
            player_grade_entity.number = player_grade_record.number
            player_grade_entity.category = player_grade_record.category.value
            player_grades.append(player_grade_entity)
        db.session.add_all(player_grades)
