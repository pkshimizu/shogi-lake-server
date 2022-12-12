from functools import wraps

from app.api.database import db


def transaction(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if "in_transaction" in db.session.info and db.session.info["in_transaction"]:
            return func(*args, **kwargs)
        else:
            db.session.info["in_transaction"] = True
            try:
                result = func(*args, **kwargs)
                db.session.commit()
                return result
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.info["in_transaction"] = False

    return decorator
