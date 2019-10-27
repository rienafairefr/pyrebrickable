from sqlalchemy import func

from rebrickable.data.models import InventoryPart
from rebrickable.data.database import Session

session = Session()

max_parts = session.query(func.max(InventoryPart.quantity)).filter(InventoryPart.quantity > 1).group_by(InventoryPart.part_num).all()

