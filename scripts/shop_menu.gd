
extends Control

func _ready() -> void:
	$panel/points.text = "points: %d" % PointsManager.get_points()
	
	$panel/weapon.visible = false
	$panel/magic.visible = false

func _on_back_button_pressed() -> void:
	$click_sound.play()
	await  $click_sound.finished
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")

func _on_weapon_button_pressed() -> void:
	if !$click_sound.playing:
		$click_sound.play()
	$panel/weapon/damage_stats.text = "damage: %.1f" % WeaponManager._weapon.weapon_damage
	$panel/weapon/upgrade_cost_stats.text = "upgrade cost: %.1f" % WeaponManager._weapon.weapon_upgrade_cost
	$panel/weapon.visible = true
	$panel/magic.visible = false

func _on_magic_button_pressed() -> void:
	if !$click_sound.playing:
		$click_sound.play()
	$panel/magic/damage_stats.text = "damage: %.1f" % MagicManager._magic.magic_damage
	$panel/magic/upgrade_cost_stats.text = "upgrade cost: %.1f" % MagicManager._magic.magic_upgrade_cost
	$panel/magic.visible = true
	$panel/weapon.visible = false

func _process(delta: float) -> void:
	$panel/points.text = "points: %d" % PointsManager.get_points()
