
extends Panel

var weapon: Dictionary
var points: float

func _process(delta: float) -> void:
	weapon = WeaponManager.get_data()
	points = PointsManager.get_points()

func _on_upgrade_pressed() -> void:
	$click_sound.play()
	if points >= weapon.upgrade_cost:
		PointsManager.spend_points(weapon.upgrade_cost)
		WeaponManager.add_damage(15)
		WeaponManager.add_crit_chance(0.5)
		WeaponManager.add_upgrade_cost()
