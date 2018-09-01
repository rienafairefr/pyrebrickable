from sqlalchemy import func

from rebrickable_data.models import InventoryPart
from rebrickable_data.database import Session

session = Session()

max_parts = session.query(func.max(InventoryPart.quantity)).filter(InventoryPart.quantity > 1).group_by(InventoryPart.part_num).all()

