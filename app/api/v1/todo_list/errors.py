from app import models


TITLE_DUPLICATE_CONSTRAINT = {
    'title': 'Title duplicate.'
}
TITLE_LENGTH_CONSTRAINT = {
    'title': f'Length constraint {models.TODO_LIST_TITLE_LENGTH_CONSTRAINT}'
}
