
extends Control

func _ready() -> void:
	$panel/points.text = "points: %.1f" % PointsManager.get_points()
	
	$panel/weapon.visible = false
	$panel/magic.visible = false

func _on_back_button_pressed() -> void:
	$click_sound.play()
	await  $click_sound.finished
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")

func _on_weapon_button_pressed() -> void:
	$click_sound.play()
	if !$panel/weapon.visible:
		$panel/weapon.visible = true
	else:
		$panel/weapon.visible = false
	$panel/magic.visible = false

func _on_magic_button_pressed() -> void:
	$click_sound.play()
	if !$panel/magic.visible:
		$panel/magic.visible = true
	else:
		$panel/magic.visible = false
	$panel/weapon.visible = false

func _process(delta: float) -> void:
	
	var weapon = WeaponManager.get_data()
	var magic = MagicManager.get_data()
	
	$panel/points.text = "points: %.1f" % PointsManager.get_points()
	
	$panel/weapon/damage_stats.text = "damage: %.1f" % weapon.damage
	$panel/weapon/crit_chance_stats.text = "crit chance: %.1f" % weapon.crit_chance
	$panel/weapon/upgrade_cost_stats.text = "upgrade cost: %.1f" % weapon.upgrade_cost
	
	$panel/magic/damage_stats.text = "damage: %.1f" % magic.damage
	$panel/magic/upgrade_cost_stats.text = "upgrade cost: %.1f" % magic.upgrade_cost
