
extends Panel

var magic: Dictionary
var points: float

func _process(delta: float) -> void:
	magic = MagicManager.get_data()
	points = PointsManager.get_points()

func _on_upgrade_pressed() -> void:
	$click_sound.play()
	if points >= magic.upgrade_cost:
		PointsManager.spend_points(magic.upgrade_cost)
		MagicManager.add_damage(30)
		MagicManager.add_upgrade_cost()
