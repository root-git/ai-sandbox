from pydantic import BaseModel, ValidationError
import logging

logger = logging.getLogger(__name__)

def parse_json[T: BaseModel](raw_str: str, model_cls: type[T]) -> T | None:
    try:
        return model_cls.model_validate_json(raw_str)
    except ValidationError as e:
        logger.error(f"JSON validation failed: {e}")
        return None 
    