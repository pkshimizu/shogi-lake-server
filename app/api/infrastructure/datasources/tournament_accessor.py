from app.api.database import db
from app.api.domain.models import TournamentTermRecord
from app.api.domain.repositories import TournamentRepository
from app.api.infrastructure.datasources.entities import (
    TournamentEntity,
    TournamentTermEntity,
    PlayerEntity,
)


class TournamentAccessor(TournamentRepository):
    def save_from_records(self, tournament_term_records: list[TournamentTermRecord]):
        tournament_entities = TournamentEntity.query.all()
        player_entities = PlayerEntity.query.all()
        for tournament_term_record in tournament_term_records:
            tournament_entity = next(
                filter(
                    lambda entity: entity.name == tournament_term_record.name,
                    tournament_entities,
                ),
                None,
            )
            if tournament_entity is None:
                tournament_entity = TournamentEntity()
                tournament_entity.name = tournament_term_record.name
                tournament_entity.is_official = tournament_term_record.is_official
                db.session.add(tournament_entity)
            tournament_term_entity = next(
                filter(
                    lambda entity: entity.term == tournament_term_record.term,
                    tournament_entity.terms,
                ),
                None,
            )
            if tournament_term_entity is None:
                tournament_term_entity = TournamentTermEntity()
                tournament_term_entity.tournament = tournament_entity
                tournament_term_entity.term = tournament_term_record.term
                db.session.add(tournament_term_entity)
            title_holder_player = next(
                filter(
                    lambda entity: entity.name
                    == tournament_term_record.title_holder_player_name,
                    player_entities,
                ),
                None,
            )
            if title_holder_player is not None:
                tournament_term_entity.title_holder_player_id = title_holder_player.id
