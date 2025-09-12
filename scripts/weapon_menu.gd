
extends Panel

var weapon: Dictionary
var points: float

func _ready() -> void:
	pass#damage upgrade_cost = WeaponManager.get_data()

func _process(delta: float) -> void:
	weapon = WeaponManager.get_data()
	points = PointsManager.get_points()

func _on_upgrade_pressed() -> void:
	if points >= weapon.upgrade_cost:
		PointsManager.spend_points(weapon.upgrade_cost)
		WeaponManager.add_damage(15)
		WeaponManager.add_upgrade_cost()
